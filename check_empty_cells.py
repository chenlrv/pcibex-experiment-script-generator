# Import packages: 
import pandas as pd
import pandas
import numpy as np
import warnings
import json
from pathlib import Path

#Call the GUI output (which is the dictionary output of the gui.py code). 
with open("config.json", "r", encoding='utf-8') as config_file:
    gui_output = json.load(config_file)

# Define the path for demo items from the GUI output:
demo_items_path = Path(gui_output['files']['experiment_file'])

class FileInspector:
    """
    A class to inspect and analyze a CSV file (of the items) for empty values.

    Attributes:
        file_path (Path): The path to the CSV file to be inspected.
        df (pd.DataFrame): The DataFrame representation of the CSV file.

    Methods:
        find_empty_values():
            Identifies and warns about empty values in the CSV file.
            Returns:
                list of tuples: A list of (row, column) tuples indicating the positions of empty values.
    """

    def __init__(self, file_path=demo_items_path):
        """
        Initializes the FileInspector with the given file path.

        Args:
            file_path (Path): The path to the CSV file to be inspected.
        """
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
   
    def find_empty_values(self):
        """
        Finds and warns about empty values in the DataFrame.

        This method checks for NaN values and empty strings in the DataFrame, issues warnings for each empty cell,
        and prints a message if empty values are found.

        Returns:
            list of tuples: A list of (row, column) tuples indicating the positions of empty values in the DataFrame.
        """
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
