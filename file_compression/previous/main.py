import os
import shutil
from icecream import ic
import tempfile

def compress_folder(folder_path, output_path, log_file):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output_path = os.path.join(temp_dir, os.path.basename(output_path))
            shutil.make_archive(temp_output_path, "zip", folder_path)
            shutil.move(f"{temp_output_path}.zip", f"{output_path}.zip")
    except PermissionError as e:
        with open(log_file, "a") as log:
            log.write(f"Permission denied: {folder_path}\n")
        ic(f"Permission denied: {folder_path}")
    except Exception as e:
        with open(log_file, "a") as log:
            log.write(f"Error compressing {folder_path}: {e}\n")
        ic(f"Error compressing {folder_path}: {e}")


def compress_all_folders_in_drive(drive_path, log_file):
    for folder_name in os.listdir(drive_path):
        folder_path = os.path.join(drive_path, folder_name)
        if os.path.isdir(folder_path):
            output_path = os.path.join(drive_path, f"{folder_name}_compressed.zip")
            if os.path.exists(output_path):
                ic(f"Skipping {folder_path} as it is already compressed")
                continue
            compress_folder(folder_path, output_path, log_file)
            ic(f"Compressed {folder_path} to {output_path}")


drive_path = "p:\\"
log_file = "file_compression/compression_log.txt"
compress_all_folders_in_drive(drive_path, log_file)
