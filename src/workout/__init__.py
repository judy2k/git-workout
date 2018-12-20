"""
workout - A git plugin to shift your commits out of work hours.
"""

import click

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


@click.command("git workout")
@click.version_option(version=__version__)
def main():
    """ Shift your commits out of work hours. """
    print("Hello, World")


if __name__ == "__main__":
    main()
