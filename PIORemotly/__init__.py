import argparse
import logging
import os
import json
import socket
from pathlib import Path


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(name)s][%(levelname)s] %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


config_file = Path(os.getenv("HOME")) / ".PIORemotly.json"


def config_file_exist():
    return config_file.is_file()


def write_config_file(token):
    data = {"token": token}
    with open(config_file, "w") as outfile:
        json.dump(data, outfile)


def get_config_file():
    home = Path(os.getenv("HOME"))
    with open(config_file, "r") as outfile:
        return json.load(outfile)


def parse_args():
    parent_parser = argparse.ArgumentParser(add_help=False)
    # common args
    parent_parser.add_argument("--debug", default=False, required=False,
                               action="store_true", dest="debug", help="debug flag")
    parent_parser.add_argument("--server", default="localhost:8000", required=False,
                               help="define server server (default: 'localhost:8000')")

    # main arg parser
    main_parser = argparse.ArgumentParser()
    service_subparsers = main_parser.add_subparsers(title="command", dest="command")

    # login
    login_parser = service_subparsers.add_parser(
        "login", help="login into the server and store api key", parents=[parent_parser])
    login_parser.add_argument("username", help="Username to login (password will be asked later).")

    # devices
    devices_parser = service_subparsers.add_parser(
        "devices", help="list devices", parents=[parent_parser])

    # test
    test_parser = service_subparsers.add_parser(
        "test", help="dispatch test", parents=[parent_parser])
    test_parser.add_argument("--workdir", default=".",
                             help="work directory which is holding the PlatformIO project (default: '.')")

    # agent
    agent_parser = service_subparsers.add_parser("agent", help="run agent", parents=[parent_parser])
    agent_parser.add_argument("--name", default=socket.gethostname(),
                              help=f"name of the agent (default: '{socket.gethostname()}')")

    args = main_parser.parse_args()
    return args
