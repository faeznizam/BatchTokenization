# import module
import os
from .helper_for_return_file import process_file, map_to_original_file

def return_file_process_flow(folder_path):
    
    batch_id_list = []

    for file in os.listdir(folder_path):
        if '_SF' in file:
            return '\nFile has already been Processed. Check your folder'
    
    #for file in os.listdir(folder_path):
        #if not 'unicef_malaysia' in file:
            #return '\nRequired file is not in the folder!'
 

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

            parsed_df = process_file(return_file_path)

            map_to_original_file(send_file_path, parsed_df, folder_path, send_file_name)

    return '\nProcess Completed!'



"""     
if __name__ == '__main__':
    return_file_process_flow()
"""         