# import module
import os
from .helper_for_return_file import process_file, map_to_original_file, analyze_result

def return_file_process_flow(folder_path):
    """
    What does this function do?
    1. Check if file already been processed.
    2. Get batch id and append to batch_id_list.
    3. Iterate over batch_id_list and get the file path for both send and return path
       that match the batch id.
    4. If both send and return file path available, then process file function will run. 
       If not, the function will tell which file path is not available and stop the process.
    5. Let user know process is complete or not.
    """
    
    batch_id_list = [] # initiate empty list

    # check for processed file
    for file in os.listdir(folder_path):
        if '_SF' in file:
            return '\nFile has already been Processed. Check your folder'
    
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
                    
                elif 'unicef_malaysia' in file and 'reply.all' in file and batch_id in file:
                    return_file_name = file
                    return_file_path = os.path.join(folder_path, file)

        # Check if both file path avalailable
        if not send_file_path:
            print('Batch id in filename starting with MCO_UTS is not match.')
        if not return_file_path:
            print('Batch id in filename starting with unicef_malaysia is not match')

        # check if both filr path available before process both files.
        if send_file_path and return_file_path:

            parsed_df = process_file(return_file_path)

            map_to_original_file(send_file_path, parsed_df, folder_path, send_file_name)

            analyze_result(folder_path)

            print("Process complete. Final file with suffix '_SF' has been created")
        else:
            print('Batch id in file name not match.')
            print('Make sure Batch id in file name for both file sent and file return match')
            
            
        
    



"""     
if __name__ == '__main__':
    return_file_process_flow()
"""         