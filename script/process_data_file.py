import pandas as pd

def create_template_table():
    table_template = {
        'paySubscriptionCreateService_run' : [], 	
        'ccAuthService_run' : [], 
        'billTo_firstName' : [],	
        'billTo_lastName' : [],	
        'billTo_email' : [],	
        'billTo_street1' : [],	
        'billTo_city' : [],	
        'billTo_state' : [],	
        'billTo_country' : [],	
        'billTo_postalCode' : [],	
        'card_accountNumber' : [],	
        'card_expirationMonth' : [],	
        'card_expirationYear' : [],	
        'card_cardType' : [],	
        'purchaseTotals_currency' : [],	
        'merchantReferenceCode' : [],	
        'purchaseTotals_grandTotalAmount' : [],	
        'recurringSubscriptionInfo_amount' : [],	
        'recurringSubscriptionInfo_frequency' : [],
        }
    
    return pd.DataFrame(table_template)
    

def copy_data_into_table(new_df, df):
    new_df['billTo_firstName'] = df['First Name']
    new_df['paySubscriptionCreateService_run'] = 'TRUE'
    new_df['ccAuthService_run'] = 'TRUE'
    new_df['billTo_lastName'] = df['Last Name']
    new_df['billTo_email'] = df['Email']	
    new_df['billTo_street1'] = df['Street']	
    new_df['billTo_city'] = 'Malaysia'
    new_df['billTo_state'] = 'MY'
    new_df['billTo_country'] = 'MY'
    new_df['billTo_postalCode'] = df['Post Code']	
    new_df['card_accountNumber'] = df['Card Number']	
    new_df['card_expirationMonth'] = df['Expiry Month']
    new_df['card_expirationYear'] = df['Expiry Year']
    new_df['card_cardType'] = df['Payment Submethod']
    new_df['purchaseTotals_currency'] = 'MYR'
    new_df['merchantReferenceCode']	 = df['Mobile Phone']
    new_df['purchaseTotals_grandTotalAmount'] = '0'
    new_df['recurringSubscriptionInfo_amount'] = '0'
    new_df['recurringSubscriptionInfo_frequency'] = 'on-demand'

    return new_df

def process_street_data(df):
    # limit to 40 character only
    df['Street'] = df['Street'].apply(lambda x : x[:40] if isinstance(x,str) else x)

    return df

def create_expiry_month(df):
    # numerical 2 digit month
    df['Expiry Month'] = df['Expiry Date'].str[:2] 

    return df

def create_expiry_year(df):
    # numerical 4 digit for year
    year = df['Expiry Date'].str[-2:]
    df['Expiry Year'] = '20' + year

    return df

def convert_payment_submethod(df):
    # visa = 001, mastercard = 002, amex = 003
    df['Payment Submethod'].replace('MasterCard', '002', inplace=True)
    df['Payment Submethod'].replace('Visa', '001', inplace=True)
    df['Payment Submethod'].replace('Amex', '003', inplace=True)
     
    return df

def drop_columns(df):
    df = df.drop(columns=['Donor Id','Title','Ethnic','Gender','City','State','Country','Home Phone','Work Phone',
                          'Mobile Phone','Date of Birth','Last Pledge Amount',
                          'Last Cash Amount','Last Pledge Date','Last Cash Date','Pledge id',
                          'Pledge Date','Pledge Start Date','Pledge End Date','Donation Amount',
                          'Payment Method','Truncated CC',
                          'Frequency','Cardholder Name','Gift Date','Campaign',
                          'Campaign Name','Action','Bank Account Number','Bank Account Holder Name',
                          'Preferred Change Date','Description','DRTV Time','Bank','Unique Id',
                          'Membership No','IPay88 Tokenized ID',
                          'DRTV Channel','Creative'])

    return df


def process_data_table(df):
    df = drop_columns(df)
    df = process_street_data(df)
    df = create_expiry_month(df)
    df = create_expiry_year(df)
    df = convert_payment_submethod(df)

    new_df = create_template_table()
    new_df = copy_data_into_table(new_df, df)

    return new_df
           


            
