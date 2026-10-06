# pylint: disable=C0111
# pylint: disable=R0904
# pylint: disable=W0621
"""Run unit tests for report utilities."""

import logging
from io import TextIOWrapper

import pytest

from utils.report import dump_employees, show_employees


def test_show_employees():
    with open("tests/test.yaml", "r", encoding="UTF-8") as file_handle:
        assert isinstance(file_handle, TextIOWrapper)
        show_employees(file_handle)


def test_dump_employees_debug(capsys: pytest.CaptureFixture[str]):
    logger = logging.getLogger("utils.report")
    old_level = logger.level
    try:
        logger.setLevel(logging.DEBUG)
        dump_employees("tests/test.yaml")
        captured = capsys.readouterr()
        assert "dumping file contents:" in captured.out
        assert "frank:" in captured.out
    finally:
        logger.setLevel(old_level)


def test_dump_employees_info(capsys: pytest.CaptureFixture[str]):
    logger = logging.getLogger("utils.report")
    old_level = logger.level
    try:
        logger.setLevel(logging.INFO)
        dump_employees("tests/test.yaml")
        captured = capsys.readouterr()
        assert "dumping file contents:" not in captured.out
    finally:
        logger.setLevel(old_level)
