import click

from PIORemotly.device.commands.list import device_list_cmd


@click.group(
    "device",
    commands=[
        device_list_cmd,
    ],
    short_help="Manage devices",
)
def cli():
    pass
