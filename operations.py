import os
import shutil
from datetime import datetime

def backup_files(src_dir, backup_dir) -> None:
    """This Method Will Check Before Backup If The Source Directory And Backup Direction Exists
        And Copy All Files And Subdirectories."""

    if not os.path.isdir(src_dir):
        print('-' * 50)
        print("The Source Directory Does Not Exist.")
        print('-' * 50)

        return

    if not os.path.isdir(backup_dir):
        print('-' * 50)
        print("The Backup Directory Does Not Exist.")
        print('-' * 50)
        return

    date = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    
    clean_name = os.path.normpath(src_dir)
    
    folder_name = os.path.basename(clean_name)

    formatted_backup_folder =  f"{folder_name}_{date}"

    backup_path = os.path.join(backup_dir, formatted_backup_folder)

    print('-' * 50)
    print("Please Wait\nWorking...")

    shutil.copytree(src_dir, backup_path)

    file_counter = 0
    dir_counter = 0

    for root, dirs, names in os.walk(backup_path):

        for name in names:
            print(f"Copied File: {os.path.join(root, name)}")
            file_counter += 1

        for name in dirs:
            dir_counter += 1

    if file_counter or dir_counter:

        print('-' * 50)
        print("- Backup Completed Successfully.")
        print('-' * 50)
        print(f"- {file_counter} Files Copied.")
        print(f"- {dir_counter} Directories Copied.")
        print(f"- {dir_counter + file_counter} Total Files And Directories Copied.")
        print('-' * 50)
    
    else:
        print('-' * 50)
        print("- No Files Were Copied.")
        print('-' * 50)

    print("Created By Dark Knight:-")

    return

# Created By Dark Knight:-