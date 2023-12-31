#!/usr/bin/env python

import click

from PIORemotly.cli import PIORemotlyCLI


@click.command(cls=PIORemotlyCLI, context_settings={"help_option_names": ['-h', '--help']})
@click.option("--server", default="localhost:5001", help="PIORemotly Server")
@click.pass_context
def cli(ctx, server):
    ctx.obj['SERVER'] = server


if __name__ == "__main__":
    cli(obj={})  # pylint: disable=no-value-for-parameter
