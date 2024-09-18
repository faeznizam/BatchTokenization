import os
import pandas as pd

from script import helper_for_return_file


def return_file_process_flow():
    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Codes\task_batch_tokenization\test_data'

    batch_id_list = []

    # get batch id into batch id list
    for file in os.listdir(folder_path):
        if 'unicef_malaysia' in file and 'reply.all' in file:
            batch_id = file[16:24]
            batch_id_list.append(batch_id)

    # iterate over batch id list and process file
    for batch_id in batch_id_list:
        send_file_path = None
        return_file_path = None

        # get file path for both file based on batch id in file
        for file in os.listdir(folder_path):
            if batch_id in file:
                if 'MCO_UTS' in file and batch_id in file:
                    send_file_name = file
                    send_file_path = os.path.join(folder_path, file)
                elif 'unicef_malaysia' in file:
                    return_file_name = file
                    return_file_path = os.path.join(folder_path, file)

        if send_file_path and return_file_path:

            parsed_df = helper_for_return_file.process_file(return_file_path)

            helper_for_return_file.map_to_original_file(send_file_path, parsed_df, folder_path, send_file_name)

    print('Process Complete')

        
if __name__ == '__main__':
    return_file_process_flow()
            