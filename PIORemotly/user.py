from getpass import getpass

from PIORemotly import get_logger
from PIORemotly.api import API
from PIORemotly.config import Config

logger = get_logger("PIORemotly::User")

class User:
  def __init__(self, username, token) -> None:
    self.username = username
    self.token = token

  @staticmethod
  def login(api: API, config: Config) -> None:
    username = input("Username: ")
    password = getpass("Password: ")
    config.username = username
    config.token = api.get_token(username, password)
    config.save()
    logger.info("Success: Token written to config file.")
