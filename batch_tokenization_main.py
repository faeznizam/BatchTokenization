# import from folder
from script import process_data_file, final_file_creation

import os
import pandas as pd

def main():
    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Codes\task_batch_tokenization\test_data'

    for file in os.listdir(folder_path):
        if 'MCO_UTS' in file:
            file_path = os.path.join(folder_path, file)

            df = pd.read_excel(file_path, dtype={'Post Code' : str, 'Card Number' : str, 
                                                 'Expiry Date': str, 'Payment Submethod': str })

            df = process_data_file.process_data_table(df)

            header_data, field_names, footer_data = final_file_creation.main_template(folder_path)

            final_file_creation.file_creation(header_data,field_names,footer_data, df, folder_path)

    
    print('done')
    

if __name__ == '__main__':
    main()