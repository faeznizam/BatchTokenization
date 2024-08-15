from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
import os


# Helper Functions

def batch_counter(file_path):
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    if os.path.exists(file_path):
        with open(file_path, 'r+') as file:
            data = file.readlines()
            last_date, last_count = data[0].strip().split(',')
            
            if last_date == current_date:
                new_count = int(last_count) + 1
            else:
                new_count = 1
            
            file.seek(0)
            file.write(f"{current_date},{new_count:02d}")
            file.truncate()
    else:
        with open(file_path, 'w') as file:
            new_count = 1
            file.write(f"{current_date},{new_count:02d}")
    
    return f"{new_count:02d}"


def get_current_date():
    return datetime.now().strftime('%Y%m%d')

def create_dataframe(data, columns=None):
    return pd.DataFrame([data], columns=columns)

def write_to_excel(writer, df, start_row):
    df.to_excel(writer, index=False, header=False, startrow=start_row)

def new_file_name():
    return f'To_CYB_Batch__{get_current_date()}.xlsx'

def get_creation_date():
    return datetime.now().strftime('%Y-%m-%d')




    

def main_template(folder_path):
    file_path = os.path.join(folder_path, 'batch_count.txt')


    # Data Definitions
    header_data = {
        'merchant_id': 'merchantID=unicef_malaysia',
        'batch_id': f'batchID={get_current_date()}{batch_counter(file_path)}',
        'creation_date': f'creationDate={get_creation_date()}',
        'record_count': 'recordCount=1',
        'template': 'Template=custom',
        'reference': 'reference=MY',
        'status_email': 'statusEmail=processing-mly@unicef.org',
        'target_api': 'targetAPIVersion=1.211'
    }

    field_names = [
        'paySubscriptionCreateService_run', 'ccAuthService_run', 'billTo_firstName', 
        'billTo_lastName', 'billTo_email', 'billTo_street1', 'billTo_city', 'billTo_state',
        'billTo_country', 'billTo_postalCode', 'card_accountNumber', 'card_expirationMonth',
        'card_expirationYear', 'card_cardType', 'purchaseTotals_currency', 
        'merchantReferenceCode', 'purchaseTotals_grandTotalAmount',
        'recurringSubscriptionInfo_amount', 'recurringSubscriptionInfo_frequency'
    ]

    footer_data = ['END', 'SUM=0.00']

    return header_data, field_names, footer_data

def file_creation(header_data, field_names, footer_data, df, folder_path):

    save_file_path = os.path.join(folder_path, new_file_name())


    # Create DataFrames
    first_row_data = create_dataframe(list(header_data.values()))
    third_row_data = create_dataframe(field_names)
    data_rows = df
    last_row_data = create_dataframe(footer_data, columns=[0, 1])

    # Write to Excel
    with pd.ExcelWriter(save_file_path, engine='openpyxl') as writer:
        write_to_excel(writer, first_row_data, start_row=0)
        write_to_excel(writer, third_row_data, start_row=2)
        write_to_excel(writer, data_rows, start_row=3)
        last_row_start = 3 + len(data_rows)
        write_to_excel(writer, last_row_data, start_row=last_row_start)
