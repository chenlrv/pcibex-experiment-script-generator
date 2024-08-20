import pandas as pd
import pandas
import numpy as np
import warnings
import tkinter as tk
from pathlib import Path

from gui import PcibexScriptGeneratorApp #call the gui output
root=tk.Tk()
app=PcibexScriptGeneratorApp(root)
root.mainloop()
configurations=app.configurations
gui_output=configurations
    
demo_items_path = Path(gui_output['sections'].get('item_file', ''))

class ExcelInspector:
    def __init__(self, file_path=demo_items_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
   
    def find_empty_values(self):
        # Convert DataFrame to a NumPy array
        data = self.df.to_numpy()
       
        # Create a boolean mask for NaN values and empty strings
        is_nan = pandas.isna(data)
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
