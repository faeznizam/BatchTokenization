# import module
from .helper_for_send_file import process_data_table 
from .helper_for_send_file2 import batch_counter, get_current_date, main_template, file_creation

import os
import pandas as pd


def check_file_has_been_processed(folder_path):
    """ To check if file has been processed or not by checking prefix in the file name.
        It will return True or False """
    for file in os.listdir(folder_path):
        if 'To_CYB' in file:
            return True
    return False


def check_if_required_file_available(folder_path):
    """ To check if the required file available by checking prefix in the file name.
        Return True or False
    """
    for file in os.listdir(folder_path):
        if file.startswith('MCO_UTS'):
            return True
    return False


def send_file_process_flow(folder_path):

    is_file_has_been_processed = check_file_has_been_processed(folder_path)
    is_required_file_available = check_if_required_file_available(folder_path)

    if is_file_has_been_processed:
        return '\nFile already processed, check the folder!'
    
    if not is_required_file_available:
        return '\nRequired file is not in the folder!'
    
    for file in os.listdir(folder_path):
        if file.startswith('MCO_UTS'):

            file_path = os.path.join(folder_path, file)
            try:
                original_df = pd.read_excel(file_path, dtype={'Post Code' : str, 'Card Number' : str, 
                                                    'Expiry Date': str, 'Payment Submethod': str })
                
                df = process_data_table(original_df)

                batch_number = batch_counter(folder_path) # get batch number
                current_date = get_current_date()

                header_data, field_names, footer_data, empty_row = main_template(folder_path, df, batch_number) # reformat file

                file_creation(header_data,field_names, empty_row, footer_data, df, folder_path, batch_number) # create file with new format

                original_df.to_excel(os.path.join(folder_path, f'{file[:-5]}_{current_date}{batch_number}.xlsx'), index=False) # save original file with batch number in name
            except Exception as e:
                return f'\nAn error occurred while processing {file}: {e}'

    return '\nFile successfully processed!'

    


        






"""
if __name__ == '__main__':
    send_file_main()

"""