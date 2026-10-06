# pylint: disable=C0111
# pylint: disable=R0904
# pylint: disable=W0621
"""Run unit tests for read_yaml CLI entry point."""

import runpy
import sys

import pytest

import read_yaml


def test_main_default(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", ["read_yaml.py", "tests/test.yaml"])
    read_yaml.main()


def test_main_verbose(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", ["read_yaml.py", "-v", "tests/test.yaml"])
    read_yaml.main()


def test_main_version(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", ["read_yaml.py", "--version"])
    with pytest.raises(SystemExit) as exc_info:
        read_yaml.main()
    assert exc_info.value.code == 0


def test_main_help(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", ["read_yaml.py", "-h"])
    with pytest.raises(SystemExit) as exc_info:
        read_yaml.main()
    assert exc_info.value.code == 0


def test_main_run_as_script(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", ["read_yaml.py", "tests/test.yaml"])
    runpy.run_module("read_yaml", run_name="__main__")
