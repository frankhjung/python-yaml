"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

from collections.abc import Iterable
from io import IOBase
from typing import Any

from yaml import dump, safe_load

from employees.domain import (
    Employee,
    get_name_by_id,
    get_turnover_for_name_by_year,
    list_turnover_by_id,
    list_turnover_by_name,
    list_turnover_by_year,
    parse_employees,
    sum_turnover_by_id,
    sum_turnover_by_name,
    sum_turnover_by_year,
)


class Employees:
    """Read Employee data to return turnover information.
    Deprecated: Use pure functions in employees.domain instead.
    """

    __version__ = "2.0.0"

    def __init__(self, infile: IOBase | str | None = None):
        self.employees: Any = None
        self._domain_employees: tuple[Employee, ...] = ()
        if infile is not None:
            self.load(infile)

    def filter_by_id(self, eid: int) -> Iterable[int]:
        """Filter by employee id.
        :param eid: filter on this employee id
        """
        turnovers = list_turnover_by_id(self._domain_employees, eid)
        if turnovers is not None:
            yield from turnovers

    def filter_by_name(self, name: str) -> Iterable[int]:
        """Filter by employee name.
        :param name: filter on this employee name
        """
        turnovers = list_turnover_by_name(self._domain_employees, name)
        if turnovers is not None:
            yield from turnovers

    def filter_by_year(self, year: int) -> Iterable[int]:
        """Filter by year of employee turnover.
        :param year: filter on this turnover year
        """
        turnovers = list_turnover_by_year(self._domain_employees, year)
        if turnovers is not None:
            yield from turnovers

    def load(self, infile: IOBase | str):
        """Load YAML data from a file.
        :param infile: the YAML file to read
        """
        if isinstance(infile, IOBase):
            self.employees = safe_load(infile)
        else:
            with open(infile, "r", encoding="UTF-8") as file_handle:
                self.employees = safe_load(file_handle)

        self._domain_employees = parse_employees(self.employees)

    def dump(self):
        """
        Dump imported YAML.
        """
        return dump(self.employees)

    def get_name(self, eid: int) -> str:
        """Returns the name of employee by id.
        :param eid: the employee id
        """
        name = get_name_by_id(self._domain_employees, eid)
        if name is None:
            raise IndexError("list index out of range")
        return name

    def get_by_id(self, eid: int) -> int | None:
        """Returns the turnover for all years for an employee by id.
        :param eid: the employee id
        """
        return sum_turnover_by_id(self._domain_employees, eid)

    def get_by_name(self, name: str) -> int | None:
        """Returns turnover for all years for an employee by name.
        :param name: the employee name
        """
        return sum_turnover_by_name(self._domain_employees, name)

    def get_by_year(self, year: int) -> int:
        """Returns turnover for all employees by year.
        :param year: year of turnover
        """
        return sum_turnover_by_year(self._domain_employees, year)

    def get_for_name_by_year(self, name: str, year: int) -> int | None:
        """Returns turnover for an employee for a specific year.
        :param name: name of employee
        :param year: year of turnover
        """
        return get_turnover_for_name_by_year(self._domain_employees, name, year)

    def list_by_id(self, eid: int) -> Iterable[int] | None:
        """List turnover by id.
        :param eid: the employee id
        """
        return list_turnover_by_id(self._domain_employees, eid)

    def list_by_name(self, name: str) -> Iterable[int] | None:
        """List turnover by name.
        :param name: name of employee
        """
        return list_turnover_by_name(self._domain_employees, name)

    def list_by_year(self, year: int) -> Iterable[int] | None:
        """List turnover by year.
        :param year: year of turnover
        """
        return list_turnover_by_year(self._domain_employees, year)
