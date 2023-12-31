import os
import json

from pathlib import Path

default_config_file = Path(os.getenv("HOME")) / ".PIORemotly.json"


class Config:
    def __init__(self, username=None, token=None, config_file=default_config_file) -> None:
        self.username = username
        self.token = token
        self.config_file = config_file

    @staticmethod
    def file_exist(config_file=default_config_file) -> bool:
        return config_file.is_file()

    @staticmethod
    def load(config_file=default_config_file) -> 'Config':
        if not Config.file_exist():
            return Config()
        with open(config_file, "r", encoding="utf-8") as outfile:
            data = json.load(outfile)
            return Config(data['username'], data['token'])

    def save(self) -> None:
        data = {"username": self.username, "token": self.token}
        with open(self.config_file, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile)
