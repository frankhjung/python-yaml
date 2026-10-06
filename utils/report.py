"""
Log employee YAML data.
"""

import logging
from io import TextIOWrapper

from employees import Employees

logger = logging.getLogger(__name__)


def show_employees(infile: TextIOWrapper) -> None:
    """Show employee data read from YAML file."""

    # load employees from YAML
    _e = Employees(infile)

    logger.debug("employees ...................:")
    for _n, _t in _e.employees.items():
        logger.debug("\t%s\t%s", _n, _t)

    _t = _e.get_name(3)
    logger.debug("name for id 3 ...............: %s", _t)

    _t = _e.get_by_id(3)
    logger.debug("turnover for 3 ..............: %i", _t)

    _t = _e.get_by_name("frank")
    logger.debug("turnover for frank ..........: %i", _t)

    _t = _e.get_by_year(2012)
    logger.debug("turnover for 2012 ...........: %i", _t)

    _t = _e.list_by_id(3)
    if _t is not None:
        logger.debug("list turnover by id .........: %s", list(_t))

    _t = _e.list_by_name("frank")
    if _t is not None:
        logger.debug("list turnover by name .......: %s", list(_t))

    _t = _e.list_by_year(2013)
    if _t is not None:
        logger.debug("list turnover by year .......: %s", list(_t))


def dump_employees(file: str) -> None:
    """Dump employee data."""

    if logger.getEffectiveLevel() == logging.DEBUG:
        print("dumping file contents:")
        print(Employees(file).dump())
