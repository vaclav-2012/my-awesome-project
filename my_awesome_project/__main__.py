# -*- coding: utf-8 -*-

import click

from my_awesome_project.example import some_function
from my_awesome_project.version import distribution_name, version


@click.command()
@click.argument("first", type=int)
@click.argument("second", type=int)
@click.version_option(version=version(), prog_name=distribution_name)
def main(first: int, second: int):
    """Main entry point."""
    some_number = some_function(first, second)
    click.echo(some_number)


if __name__ == "__main__":
    main()
