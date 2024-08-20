import unittest
from class_1 import HeadlineChecker

gui_output= {'sections': {'context': 'Yes', 'answers type': 'custom','item_file': 'C:/Users/abeer/OneDrive/שולחן העבודה/tests/warning_if_custom.csv', 'practice_file': 'C:/Users/abeer/OneDrive/שולחן העבודה/tests/demo_items_messing_c_and_cells.csv'} }

class TestExcelInspector(unittest.TestCase):

    def setUp(self):
        
        self.test_file_path1 = gui_output['sections'] ['item_file']
        self.test_file_path2 = gui_output['sections'] ['practice_file']
        self.context_answer = gui_output['sections']['context']
        self.answer_options=gui_output['sections']['answers type']
        
    def test_HeadlineChecker(self):

    
        inspector = HeadlineChecker(demo_items=self.test_file_path1,demo_practice=self.test_file_path2,include_context=self.context_answer,answers=self.answer_options)
        
        # Expected warning messages
        expected_warnings = [
            "Warning: The following essential headlines are not found in the item file: ['condition', 'context']",
"Warning: Please update the headlines according to the following list: ['group', 'set', 'condition', 'sentence', 'question', 'context']",
"Warning: The following essential headlines are not found in the item file: ['context']",
"Warning: Please update the headlines according to the following list: ['sentence', 'condition', 'question', 'context']",
"Warning: The file 'warning_if_custom.csv' does not match the expected name 'demo_items.csv'.",
"Warning: The file 'demo_items_messing_c_and_cells.csv' does not match the expected name 'demo_practice.csv'.",
"Warning: 'FIRST_answer' is essential but not found in the item file.",
"Warning: 'SECOND_answer' is essential but not found in the practice file."
,
        ]

        # Capture warnings using the `assertWarns` context manager
        with self.assertWarns(UserWarning) as cm:
           inspector._check_item_practice_headlines() 
           inspector.extract_filename ()
           inspector.check_if_noun_requires_answers()

        # Extract the actual warning messages
        actual_warnings = [str(warning.message) for warning in cm.warnings]

        # Check that the actual warnings match the expected warnings
        self.assertEqual(actual_warnings, expected_warnings)

if __name__ == '__main__':
    unittest.main()


