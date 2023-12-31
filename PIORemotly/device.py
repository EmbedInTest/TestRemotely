from typing import Iterator

from PIORemotly.api import API


class Device:
    def __init__(self, id: int, name: str, owner: str, path: str) -> None:
        self.id = id
        self.name = name
        self.owner = owner
        self.path = path

    def __str__(self) -> str:
        return f"Device: id={self.id}, name={self.name}, owner={self.owner}, path={self.path}"

    @staticmethod
    def get_all(api: API) -> Iterator['Device']:
        devices = api.get_devices()
        for device in devices:
            yield Device(device['id'], device['name'], device['owner'], device['path'])

    def last_status(self, api: API):
        status = api.get_device_status(self.id)
