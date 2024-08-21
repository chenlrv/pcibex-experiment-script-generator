#importing packages and classes
import unittest
from pathlib import Path
from check_empty_cells import FileInspector
import json


#Call the GUI output (which is the dictionary output of the gui.py code). 
with open("config.json", "r", encoding='utf-8') as config_file:
    gui_output = json.load(config_file)

class TestExcelInspector(unittest.TestCase):
    """
    Test case class for testing the FileInspector class.
    This class is responsible for testing whether the FileInspector class can correctly identify and warn about empty values
    in a CSV file provided through the 'test_file_path', a single case of a previously provided file.
    """

    def setUp(self):
        """
        Setting up the environment for the test.
        This method initializes the path to the CSV file that will be inspected for empty values.
        """
        self.test_file_path = Path('demo_items_messing_c_and_cells.csv') #defining the path to the test CSV file.

    def test_find_empty_values(self):
        """
        Test method to verify that the FileInspector correctly identifies empty values in the CSV file.
        This method uses the FileInspector to find empty values in the test file and checks that the warnings generated 
        by the FileInspector match the expected warnings.
        """
        inspector = FileInspector(file_path=self.test_file_path)
        
        #expected warning messages
        expected_warnings = [
            "Warning: Empty value found at row 2, column 5",
            "Warning: Empty value found at row 2, column 10",
        ]

        
        with self.assertWarns(UserWarning) as cm: #capturing warnings using the `assertWarns` context manager
            inspector.find_empty_values()
        actual_warnings = [str(warning.message) for warning in cm.warnings] #extracting the actual warning messages
        self.assertEqual(actual_warnings, expected_warnings) #checking that the actual warnings match the expected warnings.
    print("All generated warnings were found in the expected warnings list.")    

if __name__ == '__main__':
    unittest.main()
