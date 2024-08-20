# Import packages:
import tkinter as tk
from pathlib import Path

from gui import PcibexScriptGeneratorApp #call the GUI output

root=tk.Tk()
app=PcibexScriptGeneratorApp(root)
root.mainloop()
configurations=app.configurations
gui_output=configurations #GUI's output

# Extract paths and settings from the GUI output
demo_items_path = Path(gui_output['sections'].get('item_file', '')) #extract the path of the items file. 
practice_file_path = Path(gui_output['sections'].get('practice_file', '')) #extract the path of the practice file.
if gui_output['sections']['context'] == 'Yes': #if a cotext is included create a cotext variable. 
    context_answer = gui_output['sections']['context'] 
if gui_output['sections']['answers type']== 'custom': #if 'noun' answers provided create relevant variable. 
    answer_options=gui_output['sections']['answers type']

# Call (from 'headline.py' file) the HeadlineChecker class and apply the relevant inputs:  
from headlines import HeadlineChecker
HeadlineChecker(demo_items=demo_items_path, demo_practice=practice_file_path, include_context=context_answer,answers=answer_options)

# Extract path of the Items file from the GUI output
demo_items_path = Path(gui_output['sections'].get('item_file', ''))

# Call (from 'check_empty_cells.py' file) the FileInspector class and apply the relevant inputs: 
from check_empty_cells import FileInspector
FileInspector(file_path=demo_items_path)


