import click

from PIORemotly.api import API
from PIORemotly.config import Config
from PIORemotly.account import User


@click.command("login", help="Login into PIORemotly Server")
@click.pass_context
def account_login_cmd(ctx):
    api = API(ctx.obj['SERVER'])
    User.login(api, Config.load())
    click.echo("Success: Token written to config file.")
