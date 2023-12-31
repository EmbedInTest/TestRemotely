import os
from zipfile import ZipFile
from pathlib import Path


def pack_zip_file(zip_file_name: Path, files: list[str]) -> Path:
    with ZipFile(zip_file_name, "w") as zip_object:
        for file_folder in files:
            file_folder = Path(file_folder)
            if file_folder.is_file():
                zip_object.write(file_folder)
            if file_folder.is_dir():
                for dirpath, _, filenames in os.walk(file_folder):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        zip_object.write(file_path)
    return zip_file_name
