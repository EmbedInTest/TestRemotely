import click

from PIORemotly.account.commands.login import account_login_cmd


@click.group(
    "account",
    commands=[
        account_login_cmd,
    ],
    short_help="Manage PIORemotly account",
)
def cli():
    pass
