#!/usr/bin/env python

import os
from pathlib import Path

from PIORemotly import get_logger
from PIORemotly.config import Config
from PIORemotly.api import API
from PIORemotly.run_execution import RunExecution
from PIORemotly.user import User
from PIORemotly.device import Device

logger = get_logger("PIORemotly")


def main() -> None:
    logger.debug(args)

    config = Config.load()

    if args.command == "login":
        api = API(args.server)
        User.login(api, config)

    if not Config.file_exist():
        logger.error("you need to login first!")
        exit(1)

    user = User(config.username, config.token)
    api = API(args.server, user.token)

    if args.command == "devices":
        for device in Device.get_all(api):
            print(device)

    if args.command == "test":
        workdir = Path(args.workdir)
        if not workdir.exists:
            logger.error("workdir does not exist!")
            exit(1)
        os.chdir(workdir)
        unittest = RunExecution()
        unittest.push(api)
        logger.info("waiting for board to catch the test...")
        # wait for board
        # print log

    if args.command == "agent":
        pass


if __name__ == "__main__":
    main()
