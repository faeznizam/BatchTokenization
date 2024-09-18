# import module
from script import process_receive_file

import os
import pandas as pd


# extract data based on key value into dict, then turn into dataframe.
def process_file(file_path):
    
    desired_keys = {'merchantReferenceCode',
                    'decision',
                    'paySubscriptionCreateReply_subscriptionID',
                    'paySubscriptionCreateReply_instrumentIdentifierID'
                    }

    parsed_data = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Skip the first two rows if necessary
        if len(lines) > 2:
            lines = lines[2:]

        for line in lines:
            line = line.strip()
            if line:  # Skip empty lines
                items = line.split(',')
                parsed_dict = {}
                for item in items:
                    if '=' in item:
                        key, value = item.split('=', 1)  # Split only on the first '='
                        key = key.strip()
                        value = value.strip()
                        if key in desired_keys:
                            parsed_dict[key] = value
                parsed_data.append(parsed_dict)
    
    # Convert the parsed data to a DataFrame manually if needed
    parsed_df = pd.DataFrame(parsed_data)
    
    # Filter only 'ACCEPT' rows
    if 'decision' in parsed_df.columns:
        parsed_df = parsed_df[parsed_df['decision'] == 'ACCEPT']
    
    return parsed_df


def map_to_original_file(folder_path, parsed_df, batch_id):

    for file in os.listdir(folder_path):
    
        if 'MCO_UTS' in file:
            batch_id2 = file[15:-5]

            if batch_id == batch_id2:
                file_path = os.path.join(folder_path,file)
                original_df = pd.read_excel(file_path, dtype={'Post Code' : str, 'Card Number' : str, 
                                                        'Expiry Date': str, 'Payment Submethod': str,
                                                        'Membership No' : str})

                if 'Mobile Phone' in original_df.columns and 'merchantReferenceCode' in parsed_df.columns:
                    merged_df = original_df.merge(
                                                parsed_df[[
                                                    'merchantReferenceCode',
                                                    'paySubscriptionCreateReply_subscriptionID',
                                                    'paySubscriptionCreateReply_instrumentIdentifierID'
                                                    ]],
                                                left_on='Mobile Phone', 
                                                right_on='merchantReferenceCode', 
                                                how='left')
                    
                    
                    original_df['IPay88 Tokenized ID'] = merged_df['paySubscriptionCreateReply_subscriptionID']
                    original_df['Instrument Id'] = merged_df['paySubscriptionCreateReply_instrumentIdentifierID']


                original_df.to_excel(os.path.join(folder_path, f'{file[:-5]}{batch_id}_SF.xlsx'), index=False)





def receive_file_main():
    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\One Time Task\Batch Tokenization Test'

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path) and 'unicef_malaysia' in file and 'reply.all' in file:
                print(f"Processing file: {file}")
            
                batch_id = file[16:24]
                   
                

                parsed_df = process_file(file_path)

                

                
                map_to_original_file(folder_path, parsed_df, batch_id)

            

    



if __name__ == '__main__':
    receive_file_main()