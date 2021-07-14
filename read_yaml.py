#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

import argparse
import logging.config
import os.path
import sys

from employees.employees import Employees
from utils.report import dump_employees, show_employees

if __name__ == "__main__":

    __version__ = Employees.__version__
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage="%(prog)s [options] infile",
        description="a Python example program to show YAML processing",
        epilog="© 2014-2021 Frank H Jung mailto:frankhjung@linux.com",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        help="alternate YAML file to test",
    )

    # process command line arguments
    args = parser.parse_args()
    program = parser.prog
    infile = args.infile
    verbose = args.verbose

    # set logger
    logging.config.fileConfig(
        fname="logger.properties", defaults={"log_file_name": "read_yaml.log"}
    )
    logger = logging.getLogger()

    # log at debug level if verbose flag given
    if verbose:
        logger.setLevel(logging.DEBUG)

    # show command parameters
    logger.debug("infile ......................: %s", infile.name)
    logger.debug("prog ........................: %s", program)
    logger.debug("verbose .....................: %s", verbose)
    logger.debug("version .....................: %s", __version__)

    # call helper function to show YAML file contents
    show_employees(infile)
    dump_employees(infile.name)

    sys.exit(0)
