from urllib.parse import SplitResult
import requests
from httmock import all_requests, response, HTTMock

from PIORemotly.api import API
from PIORemotly.device import Device


@all_requests
def response_content_token(url: SplitResult, request: requests.PreparedRequest):
    assert url.path == "/api-token-auth/"
    assert "karl" in request.body
    assert "any" in request.body
    content = {'token': '1234'}
    return response(content=content, request=request)


def test_api_token():
    api = API("test")
    with HTTMock(response_content_token):
        token = api.get_token("karl", "any")
    assert token == '1234'


@all_requests
def response_content_devices(url: SplitResult, request: requests.PreparedRequest):
    assert url.path == "/api/devices/"
    assert "Authorization" in request.headers
    assert "1234" in request.headers["Authorization"]
    content = [{'id': 1, 'name': "test_device",
                'owner': "owner", 'path': "/some/path"}]
    return response(content=content, request=request)


def test_api_devices():
    api = API("test", "1234")
    with HTTMock(response_content_devices):
        devices = api.get_devices()
    assert len(devices) == 1
    assert devices[0]['id'] == 1
    assert devices[0]['name'] == "test_device"
    assert devices[0]['owner'] == "owner"
    assert devices[0]['path'] == "/some/path"


def test_device():
    api = API("test", "1234")
    with HTTMock(response_content_devices):
        devices = list(Device.get_all(api))
    assert len(devices) == 1
    assert devices[0].id == 1
    assert devices[0].name == "test_device"
    assert devices[0].owner == "owner"
    assert devices[0].path == "/some/path"
