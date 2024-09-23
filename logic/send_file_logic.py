# import module
from .helper_for_send_file import process_data_table 
from .helper_for_send_file2 import batch_counter, get_current_date, main_template, file_creation

import os
import pandas as pd

# main flow
def send_file_process_flow(folder_path):
    #folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Codes\task_batch_tokenization\test_data'

    for file in os.listdir(folder_path):
        if not 'MCO_UTS' in file:
            print('File starting with MCO_UTS is not available')

        else:
            file_path = os.path.join(folder_path, file)

            original_df = pd.read_excel(file_path, dtype={'Post Code' : str, 'Card Number' : str, 
                                                 'Expiry Date': str, 'Payment Submethod': str })
            
            df = process_data_table(original_df)

            batch_number = batch_counter(folder_path) # get batch number
            current_date = get_current_date()

            header_data, field_names, footer_data, empty_row = main_template(folder_path, df, batch_number) # reformat file

            file_creation(header_data,field_names, empty_row, footer_data, df, folder_path, batch_number) # create file with new format

            original_df.to_excel(os.path.join(folder_path, f'{file[:-5]}_{current_date}{batch_number}.xlsx'), index=False) # save original file with batch number in name

    print('Process complete.')
    
"""
if __name__ == '__main__':
    send_file_main()

"""