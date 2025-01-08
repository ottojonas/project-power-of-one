import os
import shutil

from icecream import ic


def delete_common_directories(dir1, dir2):
    dirs_in_dir1 = set(os.listdir(dir1))
    dirs_in_dir2 = set(os.listdir(dir2))

    ic(dirs_in_dir1)
    ic(dirs_in_dir2)

    common_dirs = dirs_in_dir1.intersection(dirs_in_dir2)

    ic(common_dirs)

    for directory in common_dirs:
        dir_path = os.path.join(dir1, directory)

        if os.path.isdir(dir_path):

            try:
                shutil.rmtree(dir_path)
                ic(f"deleted {dir_path}")
            except PermissionError:
                ic(f"Permission denied: {dir_path}")
            except FileNotFoundError:
                ic(f"Directory not found: {dir_path}")
            except Exception as e:
                ic(f"Error deleting {dir_path}: {e}")


dir1 = "p:\\"
dir2 = "n:\\"
delete_common_directories(dir1, dir2)
