#!/usr/bin/env python

import os
from pathlib import Path

from . import get_logger, parse_args, write_config_file, get_config_file, config_file_exist
from .api import API
from .test import dispatch_test

logger = get_logger("PIORemotly")


def main() -> None:
    args = parse_args()
    logger.debug(args)

    if args.command == "login":
        from getpass import getpass
        password = getpass("Password: ")
        api = API(args.server, None)
        token = api.get_token(args.username, password)
        write_config_file(token)
        logger.info("Success: Token written to config file.")
        return

    if not config_file_exist():
        logger.error("you need to login first!")
        exit(1)

    if args.command == "devices":
        token = get_config_file()['token']
        api = API(args.server, token)
        devices = api.get_devices()
        logger.info(devices)
        for device in devices:
            logger.info(f"id:    {device['id']}")
            logger.info(f"name:  {device['name']}")
            logger.info(f"owner: {device['owner']}")
            logger.info("boards:")
            for board_url in device['boards']:
                board = api.get_board(board_url)
                logger.info(f"    id:   {board['id']}")
                logger.info(f"    name: {board['name']}")
                logger.info(f"    path: {board['path']}")
                logger.info(f"    ------")

    if args.command == "test":
        workdir = Path(args.workdir)
        if not workdir.exists:
            logger.error("workdir does not exist!")
            exit(1)
        os.chdir(workdir)
        token = get_config_file()['token']
        api = API(args.server, token)
        zip_file_name = dispatch_test()
        api.create_run(zip_file_name)
        logger.info("waiting for board to catch the test...")
        # wait for board
        # print log


if __name__ == "__main__":
    main()
