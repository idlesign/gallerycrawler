#!/usr/bin/env python
import logging
import sys

import click

from gallerycrawler import VERSION_STR
from gallerycrawler.toolbox import setup_logging


@click.group()
@click.version_option(version=VERSION_STR)
def entry_point():
    """gallerycrawler command line utilities."""


@entry_point.command()
@click.argument('module')
def dump(module):
    """Dumps gallery into a file using crawler definition from module."""

    setup_logging(logging.DEBUG)

    click.secho('Not implemented', fg='red', err=True)
    sys.exit(1)


def main():
    entry_point(obj={})


if __name__ == '__main__':
    main()
