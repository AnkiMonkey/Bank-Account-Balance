# This script creates a folder within the current directory with the name formatted as MM-YY (where MM is the current month and YY is the current year). 
# It then asks the user to confirm if this is the correct folder name. If not, the user can input the correct month and year, and a new folder will be created with the updated name.

import os
import datetime

def create_folder():
    now = datetime.datetime.now()
    month = now.strftime("%m")
    year = now.strftime("%y")
    folder_name = f"{month}-{year}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def check_folder(folder_name):
    user_input = input(f"Is '{folder_name}' the correct folder name? (y/n): ").lower()
    if user_input == 'y':
        print("Folder creation confirmed.")
    elif user_input == 'n':
        new_month = input("Enter the correct month (MM): ")
        new_year = input("Enter the correct year (YY): ")
        folder_name = f"{new_month}-{new_year}"
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        check_folder(folder_name)

if __name__ == "__main__":
    folder_name = create_folder()
    check_folder(folder_name)
