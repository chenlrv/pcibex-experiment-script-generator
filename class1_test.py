import pandas as pd
import warnings
from pathlib import Path

gui_output= {'sections': {'context': 'Yes', 'answers type': 'custom','item_file': 'C:/Users/abeer/OneDrive/שולחן העבודה/tests/demo_items.csv', 'practice_file': 'C:/Users/abeer/OneDrive/שולחן העבודה/tests/demo_practicessss.csv'} }


demo_items_path = Path(gui_output['sections'].get('item_file', ''))
practice_file_path = Path(gui_output['sections'].get('practice_file', ''))
context_answer = gui_output['sections']['context']
answer_options=gui_output['sections']['answers type']

class HeadlineChecker:
    def __init__(self, demo_items=demo_items_path, demo_practice=practice_file_path, include_context=context_answer,answers=answer_options):
        self.demo_items = demo_items
        self.demo_practice = demo_practice
        self.answers= answers
        self.essential_item_columns = ['group', 'set', 'condition', 'sentence', 'question']
        self.essential_practice_columns = ['sentence', 'condition', 'question']
        
        # Include 'context' in essential columns if include_context is True
        if include_context == "Yes":
            self.essential_item_columns.append('context')
            self.essential_practice_columns.append('context')
        
        # Load the item file
        self.df_items = pd.read_csv(demo_items)
        
        # Load the practice file
        self.df_practice = pd.read_csv(demo_practice)
  
    
    def check_if_noun_requires_answers(self):
        # If the GUI output is 'noun', then check if FIRST_answer and SECOND_answer columns exist
        if self.answers == "custom":
            if 'FIRST_answer' not in self.df_items.columns:
                warnings.warn(f"Warning: 'FIRST_answer' is essential but not found in the item file.", UserWarning)
            if 'SECOND_answer' not in self.df_items.columns:
                warnings.warn(f"Warning: 'SECOND_answer' is essential but not found in the item file.", UserWarning)
            # Add them to the list of essential columns
            self.essential_item_columns.append('FIRST_answer')
            self.essential_item_columns.append('SECOND_answer')
            self.essential_practice_columns.append('FIRST_answer')
            self.essential_practice_columns.append('SECOND_answer')


    def _check_item_practice_headlines(self):
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
       demo_items_name = Path(self.demo_items).name
       demo_practice_name = Path(self.demo_practice).name
      
       if demo_items_name != "demo_items.csv":
            warnings.warn(f"Warning: The file '{demo_items_name}' does not match the expected name 'demo_items.csv'.", UserWarning)
       if demo_practice_name != "demo_prictice.csv":
            warnings.warn(f"Warning: The file '{demo_practice_name}' does not match the expected name 'demo_practice.csv'.", UserWarning)


checker = HeadlineChecker()
checker._check_item_practice_headlines() 
checker.extract_filename ()
checker.check_if_noun_requires_answers()
    