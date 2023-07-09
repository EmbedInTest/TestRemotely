import os
from typing import List
from zipfile import ZipFile
from pathlib import Path

from . import get_logger

logger = get_logger("TEST")
zip_file_name = Path("/tmp/PIORemotly.zip")


def dispatch_test():
    # first, pack the stuff together in a zip file
    files = [Path("include") / "lib" / "src" / "test" / "platformio.ini"]
    with ZipFile(zip_file_name, "w") as zip_object:
        for file_folder in files:
            if file_folder.is_file():
                zip_object.write(file_folder)
            if file_folder.is_dir():
                for dirpath, _, filenames in os.walk(file_folder):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        zip_object.write(file_path)
    logger.info(f"zip file create: {zip_file_name}")
    return zip_file_name
