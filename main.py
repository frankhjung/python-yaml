#!/usr/bin/env python
# coding: utf-8
"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

import argparse
import logging
import os.path
import sys

from employees.employees import Employees

if __name__ == '__main__':

    __version__ = Employees.__version__
    PARSER = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage='%(prog)s [options] infile',
        description='a Python example program to show YAML processing',
        epilog='© 2014-2019 Frank H Jung mailto:frankhjung@linux.com')
    PARSER.add_argument('infile',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default='tests/test.yaml',
                        help='alternate YAML file to test')
    PARSER.add_argument('-v',
                        '--verbose',
                        help='verbose output',
                        action='count')
    PARSER.add_argument('--version', action='version', version=__version__)

    # process command line arguments
    ARGS = PARSER.parse_args()
    PROG = PARSER.prog
    INFILE = ARGS.infile
    VERBOSE = ARGS.verbose

    # show command parameters
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    LOGGER = logging.getLogger(__name__)
    if VERBOSE:
        LOGGER.setLevel(logging.DEBUG)

    # load employees from YAML
    E = Employees(INFILE)

    LOGGER.debug("infile ......................: %s", INFILE.name)
    LOGGER.debug("prog ........................: %s", PROG)
    LOGGER.debug("verbose .....................: %s", VERBOSE)
    LOGGER.debug("version .....................: %s", __version__)
    LOGGER.debug("employees ...................:")
    for n, t in E.employees.items():
        LOGGER.debug("\t%s\t%s", n, t)

    T = E.get_name(3)
    LOGGER.debug("name for id 3 ...............: %s", T)

    T = E.get_by_id(3)
    LOGGER.debug("turnover for 3 ..............: %i", T)

    T = E.get_by_name('frank')
    LOGGER.debug("turnover for frank ..........: %i", T)

    T = E.get_by_year(2012)
    LOGGER.debug("turnover for 2012 ...........: %i", T)

    T = list(E.list_by_id(3))
    LOGGER.debug("list turnover by id .........: %s", T)

    T = list(E.list_by_name('frank'))
    LOGGER.debug("list turnover by name .......: %s", T)

    T = list(E.list_by_year(2013))
    LOGGER.debug("list turnover by year .......: %s", T)

    if VERBOSE:
        print(E.dump())

    sys.exit(0)
