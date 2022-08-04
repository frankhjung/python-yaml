#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Read Employee data to return turnover information.
This is an example Python program to read and process YAML files.
"""

import argparse
import logging.config
import os.path
import sys
from io import TextIOWrapper

import employees.employees
import utils.files
from utils.report import dump_employees, show_employees


def main() -> None:
    """Example of YAML file processing."""

    __version__ = employees.employees.Employees.__version__
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage="%(prog)s [options] path",
        description="a Python example program to show YAML processing",
        epilog="© 2014-2021 Frank H Jung mailto:frankhjung@linux.com",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "path",
        type=utils.files.list_yamls,
        help="path to YAML files to test",
    )

    # set logger
    logging.config.fileConfig(
        fname="logger.properties", defaults={"log_file_name": "read_yaml.log"}
    )
    logger = logging.getLogger()

    # process command line arguments
    args = parser.parse_args()

    # log at debug level if verbose flag given
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("prog ........................: %s", parser.prog)
        logger.debug("version .....................: %s", __version__)
        logger.debug("path ........................: %s", args.path)

    # call helper function to show YAML file contents
    for file_path in args.path:
        with open(file_path, "r", encoding="UTF-8") as infile:
            logger.debug("processing file .............: %s", infile.name)
            assert isinstance(infile, TextIOWrapper)
            show_employees(infile)
            dump_employees(infile.name)


if __name__ == "__main__":
    main()
