import unittest
from class_2 import ExcelInspector

gui_output= {'sections': {'context': 'Yes', 'answers type': 'custom','item_file': 'C:/Users/abeer/OneDrive/שולחן העבודה/tests/demo_items_messing_c_and_cells.csv'} }
class TestExcelInspector(unittest.TestCase):

    def setUp(self):
        
        self.test_file_path = gui_output['sections'] ['item_file']

    def test_find_empty_values(self):

        inspector = ExcelInspector(file_path=self.test_file_path)
        
        # Expected warning messages
        expected_warnings = [
            "Warning: Empty value found at row 2, column 5",
            "Warning: Empty value found at row 2, column 10",
        ]

        # Capture warnings using the `assertWarns` context manager
        with self.assertWarns(UserWarning) as cm:
            inspector.find_empty_values()

        # Extract the actual warning messages
        actual_warnings = [str(warning.message) for warning in cm.warnings]

        # Check that the actual warnings match the expected warnings
        self.assertEqual(actual_warnings, expected_warnings)

if __name__ == '__main__':
    unittest.main()


