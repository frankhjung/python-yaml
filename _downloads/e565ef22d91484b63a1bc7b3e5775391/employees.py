#!/usr/bin/env python
# coding: utf-8
"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

from collections.abc import Iterable
from io import IOBase
from typing import Any, Union

from yaml import dump, safe_load


class Employees:
    """Read Employee data to return turnover information."""

    __version__ = "1.4.0"

    def __init__(self, infile: Union[IOBase, str, None] = None):
        self.__class__ = Employees
        self.employees: Any = None
        if infile is not None:
            self.load(infile)

    def filter_by_id(self, eid: int) -> Iterable[int]:
        """Filter by employee id.
        :param eid: filter on this employee id
        """
        for _k in self.employees.keys():
            if eid == self.employees.get(_k).get("id"):
                for _t in self.employees.get(_k).get("turnover"):
                    yield self.employees.get(_k).get("turnover").get(_t)

    def filter_by_name(self, name: str):
        """Filter by employee name.
        :param name: filter on this employee name
        """
        for _t in self.employees.get(name).get("turnover"):
            yield self.employees.get(name).get("turnover").get(_t)

    def filter_by_year(self, year: int):
        """Filter by year of employee turnover.
        :param year: filter on this turnover year
        """
        for _n in self.employees.keys():
            if year in self.employees.get(_n).get("turnover"):
                yield self.employees.get(_n).get("turnover").get(year)

    def load(self, infile: Union[IOBase, str]):
        """Load YAML data from a file.
        :param infile: the YAML file to read
        """
        if isinstance(infile, IOBase):
            self.employees = safe_load(infile)
        else:
            with open(infile, "r", encoding="UTF-8") as _fh:
                self.employees = safe_load(_fh)

    def dump(self):
        """
        Dump imported YAML.
        """
        return dump(self.employees)

    def get_name(self, eid: int) -> str:
        """Returns the name of employee by id.
        :param eid: the employee id
        """
        names = list(
            filter(
                lambda x: eid == self.employees.get(x).get("id"),
                self.employees.keys(),  # noqa: E501
            )
        )
        return names[0]

    def get_by_id(self, eid: int) -> Union[int, None]:
        """Returns the turnover for all years for an employee by id.
        :param eid: the employee id
        """
        turnovers = list(self.filter_by_id(eid))
        return sum(turnovers) if turnovers else None

    def get_by_name(self, name: str) -> Union[int, None]:
        """Returns turnover for all years for an employee by name.
        :param name: the employee name
        """
        if name in self.employees.keys():
            turnover = sum(self.filter_by_name(name))
        else:
            turnover = None
        return turnover

    def get_by_year(self, year: int) -> int:
        """Returns turnover for all employees by year.
        :param year: year of turnover
        """
        return sum(self.filter_by_year(year))

    def get_for_name_by_year(self, name: str, year: int) -> Union[int, None]:
        """Returns turnover for an employee for a specific year.
        :param name: name of employee
        :param year: year of turnover
        """
        turnovers = None
        if name in self.employees.keys():
            turnovers = list(
                self.employees.get(name).get("turnover").get(_t)
                for _t in self.employees.get(name).get("turnover")
                if _t == year
            )
        return sum(turnovers) if turnovers else None

    def list_by_id(self, eid: int) -> Union[Iterable[int], None]:
        """List turnover by id.
        :param eid: the employee id
        """
        turnovers = list(self.filter_by_id(eid))
        return turnovers if turnovers else None

    def list_by_name(self, name: str) -> Union[Iterable[int], None]:
        """List turnover by name.
        :param name: name of employee
        """
        if name in self.employees.keys():
            turnovers = list(self.filter_by_name(name))
        else:
            turnovers = None
        return turnovers

    def list_by_year(self, year: int) -> Union[Iterable[int], None]:
        """List turnover by year.
        :param year: year of turnover
        """
        turnovers = list(self.filter_by_year(year))
        return turnovers if turnovers else None
