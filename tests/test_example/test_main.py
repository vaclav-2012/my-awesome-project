# -*- coding: utf-8 -*-

from click.testing import CliRunner

from my_awesome_project.__main__ import main


def test_main():
    """Test of CLI call."""
    runner = CliRunner()
    cli_result = runner.invoke(main, ["1", "2"])
    assert cli_result.exit_code == 0
    assert cli_result.output == "3\n"
