import pandas as pd
import os

"""
1. file return in csv
2. rearrange data into column and row
3. drop unwanted column
4. map token to file
"""

def split_key_value(value):
    """Splits a key-value pair separated by '=' into a tuple (key, value)."""
    if isinstance(value, str) and '=' in value:
        key, val = value.split('=', 1)
        return key.strip(), val.strip()
    return None, None

def process_file():
    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Codes\task_batch_tokenization\test_data'

    for file in os.listdir(folder_path):
        if 'unicef_malaysia' in file and 'reply.all' in file:
            file_path = os.path.join(folder_path, file)

            df = pd.read_csv(file_path, header=None, delimiter= ' ')

            df = df[0].str.split(',', expand=True)

            # Extract the first row data
            first_row_data = df.iloc[0].dropna().tolist()

            # Remove the first row and reset index
            df = df.drop(0).reset_index(drop=True)
            
            # Expand each remaining row by adding the data from the first row
            combined_data = [first_row_data + row.dropna().tolist() for _, row in df.iterrows()]

            data = []
            for row in combined_data:
                row_dict = {}
                for item in row:
                    key, value = split_key_value(item)
                    if key:
                        row_dict[key] = value
                data.append(row_dict)

            # Create a DataFrame from the list of dictionaries
            df_combined = pd.DataFrame(data)
            
            df_combined.to_excel(os.path.join(folder_path, 'result.xlsx'), index=False)
            print('done')

            

    
if __name__ == '__main__':
    process_file()

