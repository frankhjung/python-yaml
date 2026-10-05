"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

from collections.abc import Iterable
from io import IOBase
from typing import Any

from yaml import dump, safe_load


class Employees:
    """Read Employee data to return turnover information."""

    __version__ = "1.5.0"

    def __init__(self, infile: IOBase | str | None = None):
        self.__class__ = Employees
        self.employees: Any = None
        if infile is not None:
            self.load(infile)

    def filter_by_id(self, eid: int) -> Iterable[int]:
        """Filter by employee id.
        :param eid: filter on this employee id
        """
        for employee in self.employees.values():
            if eid == employee.get("id"):
                for year in employee.get("turnover", {}):
                    yield employee.get("turnover").get(year)

    def filter_by_name(self, name: str):
        """Filter by employee name.
        :param name: filter on this employee name
        """
        for year in self.employees.get(name, {}).get("turnover", {}):
            yield self.employees.get(name).get("turnover").get(year)

    def filter_by_year(self, year: int):
        """Filter by year of employee turnover.
        :param year: filter on this turnover year
        """
        for employee in self.employees.values():
            if year in employee.get("turnover", {}):
                yield employee.get("turnover").get(year)

    def load(self, infile: IOBase | str):
        """Load YAML data from a file.
        :param infile: the YAML file to read
        """
        if isinstance(infile, IOBase):
            self.employees = safe_load(infile)
        else:
            with open(infile, "r", encoding="UTF-8") as file_handle:
                self.employees = safe_load(file_handle)

    def dump(self):
        """
        Dump imported YAML.
        """
        return dump(self.employees)

    def get_name(self, eid: int) -> str:
        """Returns the name of employee by id.
        :param eid: the employee id
        """
        names = [
            employee_name
            for employee_name, employee in self.employees.items()
            if eid == employee.get("id")
        ]
        return names[0]

    def get_by_id(self, eid: int) -> int | None:
        """Returns the turnover for all years for an employee by id.
        :param eid: the employee id
        """
        turnovers = list(self.filter_by_id(eid))
        return sum(turnovers) if turnovers else None

    def get_by_name(self, name: str) -> int | None:
        """Returns turnover for all years for an employee by name.
        :param name: the employee name
        """
        if name in self.employees:
            turnover = sum(self.filter_by_name(name))
        else:
            turnover = None
        return turnover

    def get_by_year(self, year: int) -> int:
        """Returns turnover for all employees by year.
        :param year: year of turnover
        """
        return sum(self.filter_by_year(year))

    def get_for_name_by_year(self, name: str, year: int) -> int | None:
        """Returns turnover for an employee for a specific year.
        :param name: name of employee
        :param year: year of turnover
        """
        turnovers = None
        if name in self.employees:
            turnovers = [
                self.employees.get(name).get("turnover").get(turnover_year)
                for turnover_year in self.employees.get(name).get("turnover")
                if turnover_year == year
            ]
        return sum(turnovers) if turnovers else None

    def list_by_id(self, eid: int) -> Iterable[int] | None:
        """List turnover by id.
        :param eid: the employee id
        """
        turnovers = list(self.filter_by_id(eid))
        return turnovers if turnovers else None

    def list_by_name(self, name: str) -> Iterable[int] | None:
        """List turnover by name.
        :param name: name of employee
        """
        if name in self.employees:
            turnovers = list(self.filter_by_name(name))
        else:
            turnovers = None
        return turnovers

    def list_by_year(self, year: int) -> Iterable[int] | None:
        """List turnover by year.
        :param year: year of turnover
        """
        turnovers = list(self.filter_by_year(year))
        return turnovers if turnovers else None
