from typing import Optional
from urllib.request import HTTPBasicAuthHandler
import requests
import json

from . import get_logger

logger = get_logger("API")


class API:
    def __init__(self, server: str, token: Optional[str]) -> None:
        self.server = server
        if token:
            self.token = token
            self.headers = {"Authorization": f"Token {self.token}"}

    def __get_server_url(self) -> str:
        return f"http://{self.server}"

    def get_token(self, username, password) -> str:
        data = {
            "username": username,
            "password": password
        }
        url = f"{self.__get_server_url()}/api-token-auth/"
        response = requests.post(url, data=data)

        token = json.loads(response.text).get("token")
        assert token, "Token could not be received! Is the username and password correct?"

        return token

    def get_devices(self):
        url = f"{self.__get_server_url()}/api/devices/"
        response = requests.get(url, headers=self.headers)
        return json.loads(response.text)

    def get_board(self, url):
        response = requests.get(url, headers=self.headers)
        return json.loads(response.text)

    def create_run(self, zip_file):
        url = f"{self.__get_server_url()}/api/run/"
        files = {"file": open(zip_file, "rb")}
        r = requests.post(url, files=files, headers=self.headers)
        logger.info(r)
        logger.info(r.text)
