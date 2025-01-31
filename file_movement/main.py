import os
from icecream import ic
import shutil

# * Copying folders
def copy_folder(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, dirs_exist_ok=True)
            except Exception as e:
                ic(f"Error copying directory {s} to {d}: {e}")
        else:
            try:
                if not os.path.exists(d):
                    shutil.copy2(s, d)
                else:
                    ic(f"Skipping existing file {d}")
            except Exception as e:
                ic(f"Error copying file {s} to {d}: {e}")

source_drive = "p:\\"
destination_drive = "n:\\"

for folder_name in os.listdir(source_drive):
    folder_path = os.path.join(source_drive, folder_name)
    destination_path = os.path.join(destination_drive, folder_name)

    if os.path.isdir(folder_path):
        if os.path.exists(destination_path):
            ic(f"Skipping {folder_path} as it already exists within the new directory")
            continue
        copy_folder(folder_path, destination_path)
        ic(f"Copied {folder_path} to {destination_path}")