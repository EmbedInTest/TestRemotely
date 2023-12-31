import click

from PIORemotly.api import API
from PIORemotly.config import Config
from PIORemotly.account import User
from PIORemotly.device import Device


@click.command("list", help="List Devices")
@click.pass_context
def device_list_cmd(ctx):
    if not Config.file_exist():
        click.echo("you need to login first!")
        return
    config = Config.load()
    user = User(config.username, config.token)
    api = API(ctx.obj['SERVER'], user.token)
    for device in Device.get_all(api):
        print(device)
