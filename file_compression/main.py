from icecream import ic
import os
import shutil
import tempfile
import psutil

log_file = "file_compression/compression_log.txt"


def is_file_open(file_path):
    for proc in psutil.process_iter(["open_files"]):
        try:
            if file_path in [f.path for f in proc.info["open_files"] or []]:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


def compress_folder(folder_path, output_path):
    if is_file_open(folder_path):
        with open(log_file, "a") as log:
            log.write(f"folder open {folder_path} could not compress")
        ic(f"could not compress {folder_path} - folder was open")
        return
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output_path = os.path.join(temp_dir, os.path.basename(output_path))
            shutil.make_archive(temp_output_path, "zip", folder_path)
            shutil.move(f"{temp_output_path}.zip", f"{output_path}.zip")
    except PermissionError as pe:
        with open(log_file, "a") as log:
            log.write(f"permission denied: {folder_path}\n")
        ic(f"permission denied: {folder_path}")
    except Exception as e:
        with open(log_file, "a") as log:
            log.write(f"error compressing {folder_path}: {e}\n")
        ic(f"error compressing {folder_path}: {e}")


def compress_files(file_path, output_file_path):
    if is_file_open(file_path):
        with open(log_file, "a") as log:
            log.write(f"could not compress file {file_path} as file is open")
        ic(f"could not compress file {file_path} as file is open")
        return
    try:
        shutil.make_archive(
            output_file_path,
            "zip",
            os.path.dirname(file_path),
            os.path.basename(file_path),
        )
    except PermissionError as pe:
        with open(log_file, "a") as log:
            log.write(f"permission denied: {file_path}\n")
        ic(f"permission denied: {file_path}")
    except Exception as e:
        with open(log_file, "a"):
            log.write(f"error compressing {file_path}: {e}\n")
        ic(f"error compressing {file_path}: {e}\n")


def complete_compress(drive_path):
    for item_name in os.listdir(drive_path):
        item_path = os.path.join(drive_path, item_name)
        output_path = os.path.join(drive_path, f"{item_name}_compressed")
        compressed_file_name = f"{item_name}_compressed.zip"
        if item_name == compressed_file_name:
            ic(f"skipping {item_path} - already compressed")
        if os.path.exists(f"{output_path}.zip"):
            ic(f"skipping {item_path} - already compressed")
            continue
        if os.path.exists(f"{output_path}_compressed.zip"):
            ic(f"skipping {item_path} - already compressed")
        if os.path.isdir(item_path):
            compress_folder(item_path, output_path)
            ic(f"compressed folder {item_path} to {output_path}.zip")

        elif os.path.isfile(item_path):
            compress_files(item_path, output_path)
            ic(f"compressed file {item_path} to {output_path}.zip ")


drive_path = "p:\\"
complete_compress(drive_path)
