import os
from icecream import ic
import shutil
from datetime import datetime


# * Selecting folders not modified since 2020
def folder_not_modified_since_2022(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(root, name)
            modification_time = os.path.getmtime(file_path)
            ic(f"file: {file_path}, modification: {modification_time}")
            if os.path.getmtime(file_path) > datetime(2022, 1, 1).timestamp():
                return False
    return True


# * Copying folders
def copy_folder(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)


source_drive = "p:\\"
destination_drive = "n:\\"

for folder_name in os.listdir(source_drive):
    folder_path = os.path.join(source_drive, folder_name)
    destination_path = os.path.join(destination_drive, folder_name)

    if os.path.isdir(folder_path) and folder_not_modified_since_2022(folder_path):
        if os.path.exists(destination_path):
            ic(f"skipping {folder_path} as already exists within new directory")
            continue
        copy_folder(folder_path, destination_path)
        ic(f"copied {folder_path} to {destination_path}")
