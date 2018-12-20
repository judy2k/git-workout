"""
workout - A git plugin to shift your commits out of work hours.
"""

import click
from git import Repo

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


@click.command("git workout")
@click.version_option(version=__version__)
def main():
    """ Shift your commits out of work hours. """
    repo = Repo()
    print(repo.git.for_each_ref())


def unpushed_commits(repo: Repo):
    for c in repo.iter_commits("@{push}.."):
        print(c.committed_datetime, c.message)


if __name__ == "__main__":
    main()
