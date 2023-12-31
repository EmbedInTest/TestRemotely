import os
from typing import List
from zipfile import ZipFile
from pathlib import Path

from PIORemotly import get_logger
from PIORemotly.api import API

logger = get_logger("TEST")

class RunExecution:
  def __init__(self, zip_file_name=Path("/tmp/PIORemotly.zip")) -> None:
    self.zip_file_name = zip_file_name

  def _pack(self) -> Path:
    files = ["include", "lib", "src", "test", "platformio.ini"]
    with ZipFile(self.zip_file_name, "w") as zip_object:
      for file_folder in files:
        file_folder = Path(file_folder)
        if file_folder.is_file():
          zip_object.write(file_folder)
        if file_folder.is_dir():
          for dirpath, _, filenames in os.walk(file_folder):
            for filename in filenames:
              file_path = os.path.join(dirpath, filename)
              zip_object.write(file_path)
    logger.info(f"zip file create: {self.zip_file_name}")
    return self.zip_file_name
  
  def push(self, api: API):
    zip_file = self._pack()
    api.create_run(zip_file)

  def run(self) -> bool:
    pass
