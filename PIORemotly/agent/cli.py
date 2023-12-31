import click


@click.group(
    "agent",
    commands=[
        # device_list_cmd,
    ],
    short_help="Manage an Agent",
)
def cli():
    pass
