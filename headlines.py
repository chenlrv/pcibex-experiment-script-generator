# Import packages: 
import pandas as pd
import warnings
import tkinter as tk
from pathlib import Path

from gui import PcibexScriptGeneratorApp #call the GUI output (which is the dictionary output of the gui.py code). 
root=tk.Tk()
app=PcibexScriptGeneratorApp(root)
root.mainloop()
configurations=app.configurations
gui_output=configurations

# Extract paths and settings from the GUI output
demo_items_path = Path(gui_output['sections'].get('item_file', '')) #extract the path of the items file. 
practice_file_path = Path(gui_output['sections'].get('practice_file', '')) #extract the path of the practice file.
if gui_output['sections']['context'] == 'Yes': #if a cotext is included create a cotext variable. 
    context_answer = gui_output['sections']['context'] 
if gui_output['sections']['answers type']== 'custom': #if 'noun' answers provided create relevant variable. 
    answer_options=gui_output['sections']['answers type']

class HeadlineChecker:
    """
    A class to verify the essential columns and filenames in the item and practice files.

    Attributes:
        demo_items (Path): Path to the CSV file containing demo items.
        demo_practice (Path): Path to the CSV file containing practice items.
        answers (str): Type of answers expected ('custom' or 'Yes/No').
        essential_item_columns (list): List of essential columns for the item file.
        essential_practice_columns (list): List of essential columns for the practice file.
        df_items (pd.DataFrame): DataFrame loaded from the demo items CSV file.
        df_practice (pd.DataFrame): DataFrame loaded from the practice CSV file.
    """
    def __init__(self, demo_items=demo_items_path, demo_practice=practice_file_path, include_context=context_answer,answers=answer_options):
        """
        Initializes the HeadlineChecker with file paths, context inclusion flag, and answer type.

        Args:
            demo_items (Path): Path to the CSV file containing demo items.
            demo_practice (Path): Path to the CSV file containing practice items.
            include_context (str): Whether to include 'context' in essential columns ('Yes').
            answers (str): Type of answers expected (whether it is 'custom').
        """
    
        self.demo_items = demo_items
        self.demo_practice = demo_practice
        self.answers= answers
        self.essential_item_columns = ['group', 'set', 'condition', 'sentence', 'question']
        self.essential_practice_columns = ['sentence', 'condition', 'question']
        
        # Include 'context' in essential columns if include_context is 'Yes':
        if include_context == "Yes":
            self.essential_item_columns.append('context')
            self.essential_practice_columns.append('context')
        
        # Load the item file
        self.df_items = pd.read_csv(demo_items)
        
        # Load the practice file
        self.df_practice = pd.read_csv(demo_practice)
  
    
    def check_if_noun_requires_answers(self):
        """
        Checks if 'FIRST_answer' and 'SECOND_answer' columns are required based on the answer type.
        Issues warnings if these columns are missing in the item file and adds them to the list of essential columns.
        """
        # If the GUI output is 'noun', then check if FIRST_answer and SECOND_answer columns exist:
        if self.answers == "custom":
            if 'FIRST_answer' not in self.df_items.columns:
                warnings.warn(f"Warning: 'FIRST_answer' is essential but not found in the item file.", UserWarning)
            if 'SECOND_answer' not in self.df_items.columns:
                warnings.warn(f"Warning: 'SECOND_answer' is essential but not found in the item file.", UserWarning)
            
            # Add them to the list of essential columns:
            self.essential_item_columns.append('FIRST_answer')
            self.essential_item_columns.append('SECOND_answer')
            self.essential_practice_columns.append('FIRST_answer')
            self.essential_practice_columns.append('SECOND_answer')


    def _check_item_practice_headlines(self):
        """
        Checks if all essential columns are present in both item and practice DataFrames.
        Issues warnings if any essential columns are missing.
        """

        #Check the existence of the essential column names: 
        headlines_items = self.df_items.columns.tolist()
        absent_in_items = [item for item in self.essential_item_columns if item not in headlines_items]

        headlines_practice = self.df_practice.columns.tolist()
        absent_in_practice = [item for item in self.essential_practice_columns if item not in headlines_practice]

        if absent_in_items:
            warnings.warn(f"Warning: The following essential headlines are not found in the item file: {absent_in_items}", UserWarning)
            warnings.warn(f"Warning: Please update the headlines according to the following list: {self.essential_item_columns}", UserWarning)

        if absent_in_practice:
            warnings.warn(f"Warning: The following essential headlines are not found in the item file: {absent_in_practice}", UserWarning)
            warnings.warn(f"Warning: Please update the headlines according to the following list: {self.essential_practice_columns}", UserWarning)

    def extract_filename(self):
       """
        Checks if the filenames of the demo items and practice files match the expected names.
        Issues warnings if the filenames do not match the expected names.
        """ 
       #Extract file names from the Path: 
       demo_items_name = Path(self.demo_items).name 
       demo_practice_name = Path(self.demo_practice).name
      
       if demo_items_name != "demo_items.csv":
            warnings.warn(f"Warning: The file '{demo_items_name}' does not match the expected name 'demo_items.csv'.", UserWarning)
       if demo_practice_name != "demo_prictice.csv":
            warnings.warn(f"Warning: The file '{demo_practice_name}' does not match the expected name 'demo_practice.csv'.", UserWarning)