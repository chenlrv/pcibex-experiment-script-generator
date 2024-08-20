# Import packages:
import json
from pathlib import Path

#call the GUI output
with open("config.json", "r", encoding='utf-8') as config_file:
    gui_output = json.load(config_file) #GUI's output

# Extract paths and settings from the GUI output
items_file_path = Path(gui_output['files']['experiment_file']) #extract the path of the item file.
practice_file_path = Path(gui_output['files']['practice_file']) #extract the path of the practice file.
if gui_output['sections']['context'] == 'yes': #if a cotext is included create a cotext variable. 
    context_answer = gui_output['sections']['context']
else: 
    context_answer = 'no' 
answer_options=gui_output['sections']['answers'] # create 'answer type 'variable as provided (yes/no or custom).

# Call (from 'headline.py' file) the HeadlineChecker class and apply the relevant inputs:  
from headlines import HeadlineChecker
HeadlineChecker(demo_items=items_file_path, demo_practice=practice_file_path, include_context=context_answer,answers=answer_options)
#Provide the warning messages: 
checker = HeadlineChecker()
checker._check_item_practice_headlines() 
checker.extract_filename ()
checker.check_if_noun_requires_answers()

# Extract path of the Items file from the GUI output
demo_items_path = Path(gui_output['files']['experiment_file'])

# Call (from 'check_empty_cells.py' file) the FileInspector class and apply the relevant inputs: 
from check_empty_cells import FileInspector
FileInspector(file_path=demo_items_path)

#Provide the warning messages: 
checker = FileInspector()
checker.find_empty_values() 

