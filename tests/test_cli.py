import click
from click.testing import CliRunner

from chatcube import __version__
from chatcube.cli import main


EXPECTED_ROOT_TREE = """\
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit."""


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatcube, version {__version__}" in result.output


def test_help_mentions_tree_options():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_tree_option_reports_shared_registered_command_tree():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output.strip() == EXPECTED_ROOT_TREE
    assert "hello" not in result.output.lower()


def test_tree_modes_include_and_omit_command_parameter_signatures(monkeypatch):
    @click.command(name="inspect", help="Inspect a cube.")
    @click.argument("cube")
    @click.option("--format", "output_format", metavar="FORMAT")
    def inspect_cube(cube, output_format):
        pass

    monkeypatch.setitem(main.commands, "inspect", inspect_cube)

    detailed = CliRunner().invoke(main, ["--tree"])
    brief = CliRunner().invoke(main, ["--tree-brief"])

    assert detailed.exit_code == 0
    assert brief.exit_code == 0
    assert "inspect <CUBE> [--format OUTPUT-FORMAT]  # Inspect a cube." in detailed.output
    assert "inspect  # Inspect a cube." in brief.output
    assert "<CUBE>" not in brief.output
    assert "[--format OUTPUT-FORMAT]" not in brief.output
