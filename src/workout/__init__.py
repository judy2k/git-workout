"""
workout - A git plugin to shift your commits out of work hours.
"""

import click


@click.command()
@click.version_option()
def main():
    print("Hello, World")


if __name__ == "__main__":
    main()
