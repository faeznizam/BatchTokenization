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
    new_df['paySubscriptionCreateService_run'] = 'TRUE'
    new_df['ccAuthService_run'] = 'TRUE'
    new_df['billTo_firstName'] = df['First Name']
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
    new_df['merchantReferenceCode']	 = df['National Id']
    new_df['purchaseTotals_grandTotalAmount'] = '0'
    new_df['recurringSubscriptionInfo_amount'] = '0'
    new_df['recurringSubscriptionInfo_frequency'] = 'on-demand'

    return new_df