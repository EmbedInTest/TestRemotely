import os
from pathlib import Path
import click

from PIORemotly import fs
from PIORemotly.account import User
from PIORemotly.api import API
from PIORemotly.config import Config
from PIORemotly.test import pack_zip_file


@click.command("test", help="Run a Unit Test")
@click.option(
    "-d",
    "--project-dir",
    default=os.getcwd,
    type=click.Path(exists=True, file_okay=True, dir_okay=True, writable=True),
)
@click.pass_context
def cli(ctx, project_dir):
    if not Config.file_exist():
        click.echo("you need to login first!")
        return
    config = Config.load()
    user = User(config.username, config.token)
    api = API(ctx.obj['SERVER'], user.token)
    with fs.cd(project_dir):
        zip_file_name = Path("/tmp/PIORemotly.zip")
        files = ["include", "lib", "src", "test", "platformio.ini"]
        zip_file = pack_zip_file(zip_file_name, files)
        api.create_run(zip_file)
