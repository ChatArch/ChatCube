from click.testing import CliRunner

from chatcube import __version__
from chatcube.cli import main, render_cli_tree


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatcube, version {__version__}" in result.output


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output


def test_tree_option_reports_registered_command_tree():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output.strip() == render_cli_tree(main)
    assert "chatcube  # ChatArch placeholder CLI for cube workflow packages." in result.output
    assert "├── --help  # Show this help message." in result.output
    assert "├── --version  # Show the installed package version." in result.output
    assert "└── --tree  # Print the registered command tree." in result.output
    assert "hello" not in result.output.lower()
