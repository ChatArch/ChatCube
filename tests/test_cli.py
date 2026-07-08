from click.testing import CliRunner

from chatcube import __version__
from chatcube.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatcube, version {__version__}" in result.output
