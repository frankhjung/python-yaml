# pylint: disable=C0111
# pylint: disable=R0904
# pylint: disable=W0621
"""
Run unit tests for YAML file utilities.
"""

from utils.files import list_yamls


def test_files():
    assert "tests/test.yaml" in list_yamls("tests")


def test_no_files():
    assert not list_yamls("utils")
