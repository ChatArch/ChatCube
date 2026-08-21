"""CLI entrypoint for chatcube."""

import click
from chatstyle import add_tree_option

from chatcube import __version__


@click.group(name="chatcube")
@click.version_option(__version__, prog_name="chatcube")
@add_tree_option
def main() -> None:
    """ChatArch placeholder CLI for cube workflow packages."""


if __name__ == "__main__":
    main()
