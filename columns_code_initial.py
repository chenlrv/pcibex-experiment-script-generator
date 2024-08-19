import pandas as pd
final_dict=[]
df_items = pd.read_csv('demo_items.csv')

if final_dict['Practice'] == 'True': #if a practice file is found, read it too. 
    df_practice = pd.read_csv('demo_practice.csv')

headlines_items = df_items.columns.tolist()
headlines_practice = df_practice.columns.tolist()

essential_item_columns= ['group','set','condition','sentence','question']
essential_practice_columns=['sentence','condition','question']

# Find elements in headlines_items that are not in essential_column_names:
absent_in_items = [item for item in essential_item_columns if item not in headlines_items]

import warnings
if absent_in_items: #give a warning msg in case the there is no match between the headlines.
    warnings.warn(f"Warning: The following essential headlines are not found in the Excel file: {absent_in_items}", UserWarning)
    warnings.warn(f"Warning: Please update the headlines according to the following list: {essential_item_columns}", UserWarning)

# Do the same for the practice_demo: 
absent_in_practice = [item for item in essential_practice_columns if item not in headlines_practice]

if absent_in_practice: #give a warning msg in case the there is no match between the headlines.
    warnings.warn(f"Warning: The following essential headlines are not found in the Excel file: {absent_in_practice}", UserWarning)
    warnings.warn(f"Warning: Please update the headlines according to the following list: {essential_practice_columns}", UserWarning)
    

