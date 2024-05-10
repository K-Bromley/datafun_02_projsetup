''' This module provides functions for creating a series of project folders. '''

# Imports
import math
import statistics
import pathlib
import time
import kellybromley_utils


# Function 1 for creating folders for a range of years
def create_folders_for_range(start_year, end_year):

    for i in range(start_year, end_year):
        folder_name = f"Year_{i}"
    pathlib.Path(folder_name).mkdir(exist_ok=True)


# Function 2 for creating folders from a list of names
def create_folders_from_list(folder_list):
    folder_names = ['data-csv', 'data-excel', 'data-json']
    for folder_name in folder_names:
        pathlib.Path(folder_name).mkdir(exist_ok=True)


# Function 3 for creating folders with prefix
def create_prefixed_folders(folderlist, prefix):
    folder_names = ['data-csv', 'data-excel', 'data-json']
    prefix = 'data-'
    for folder_name in folder_names:
        prefixed_folder_name = prefix + folder_name
    pathlib.Path(prefixed_folder_name).mkdir(exist_ok=True)


# Function 4 for calling periodically
def create_folders_periodically(duration):
        time_date_stamp = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        pathlib.Path(time_date_stamp).mkdir(exist_ok=True)
        time.sleep(duration)

     

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"byline:{kellybromley_utils}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year= 2020, end_year=2025)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 for creating files periodically
    create_folders_periodically(duration=5)


if __name__ == '__main__':
        main()