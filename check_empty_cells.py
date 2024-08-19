import pandas as pd
import numpy as np
import warnings

class ExcelInspector:
    def __init__(self, file_path, sheet_name='Sheet1'):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
   
    def find_empty_values(self):
        # Convert DataFrame to a NumPy array
        data = self.df.to_numpy()
       
        # Create a boolean mask for NaN values and empty strings
        is_nan = np.isnan(data)
        is_empty_string = (data == '')
       
        # Combine masks
        is_empty = is_nan | is_empty_string
       
        # Find the indices of empty cells
        empty_indices = np.argwhere(is_empty)
       
        # Convert indices to a list of tuples
        empty_locations = [(row, col) for row, col in empty_indices]
       
        # Issue warnings if there are empty cells
        if empty_locations:
            for row, col in empty_locations:
                warnings.warn(f"Warning: Empty value found at row {row + 1}, column {col + 1}")
        else:
            print("No empty values found.")
       
        return empty_locations
    