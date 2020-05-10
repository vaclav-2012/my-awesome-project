# -*- coding: utf-8 -*-

from click.testing import CliRunner

from my_awesome_project.__main__ import main


def test_main_default():
    """Test default CLI call."""
    runner = CliRunner()
    cli_result = runner.invoke(main, ["1", "2"])
    assert cli_result.exit_code == 0
    assert cli_result.output == "3\n"


def test_main_version():
    """Test CLI call with `--version` option."""
    runner = CliRunner()
    cli_result = runner.invoke(main, ["--version"])
    assert cli_result.exit_code == 0
    assert "version" in cli_result.output
