"""CLI entrypoint for chatcube."""

import click

from chatcube import __version__


@click.group()
@click.version_option(__version__, prog_name="chatcube")
def main() -> None:
    """chatcube command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


if __name__ == "__main__":
    main()
