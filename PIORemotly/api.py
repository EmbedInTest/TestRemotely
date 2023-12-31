from typing import Optional
from urllib.request import HTTPBasicAuthHandler
import requests

from . import get_logger

logger = get_logger("API")


class API:
    def __init__(self, server: str, token: Optional[str] = None) -> None:
        self.server = server
        if token:
            self.token = token
            self.headers = {"Authorization": f"Token {self.token}"}

    def __get_server_url(self) -> str:
        return f"http://{self.server}"

    def _post(self, path, data=None, files=None):
        url = f"{self.__get_server_url()}/{path}/"
        if files:
            files = {"file": open(files, "rb")}
        response = requests.post(url, data=data, files=files)
        return response.json()

    def _get(self, path):
        url = f"{self.__get_server_url()}/{path}/"
        response = requests.get(url, headers=self.headers)
        assert response.status_code == 200, f"status code is: {response.status_code}, but should be 200!\nurl: {url}"
        return response.json()

    def get_token(self, username, password) -> str:
        data = {
            "username": username,
            "password": password
        }
        token = self._post("api-token-auth", data=data).get("token")
        assert token, "Token could not be received! Is the username and password correct?"
        return token

    def get_devices(self):
        return self._get("api/devices")

    def set_device_status(self, id, status):
        pass

    def get_device_status(self, id):
        return self._get(f"api/devicestatus/{id}")

    def create_run(self, zip_file):
        self._post("api/run", files=zip_file)

    def check_for_run(self) -> bool:
        pass

    def set_run_status(self, url, status):
        pass

    def get_run_status(self, url):
        pass
