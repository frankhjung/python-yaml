#!/usr/bin/env python
# coding: utf-8
"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""


class Employees():
    """ Read Employee data to return turnover information. """

    __version__ = '0.6.0'

    def __init__(self, infile=None):
        self.__class__ = Employees
        self.employees = None
        if infile is not None:
            self.load(infile)

    def filter_by_id(self, eid):
        """ filter by id
        :param eid:
        """
        for _k in self.employees.keys():
            if eid == self.employees.get(_k).get('id'):
                for _t in self.employees.get(_k).get('turnover'):
                    yield self.employees.get(_k).get('turnover').get(_t)

    def filter_by_name(self, name):
        """ filter by name
        :param name:
        """
        for _t in self.employees.get(name).get('turnover'):
            yield self.employees.get(name).get('turnover').get(_t)

    def filter_by_year(self, year):
        """ filter by year
        :param year:
        """
        for _n in self.employees.keys():
            if year in self.employees.get(_n).get('turnover'):
                yield self.employees.get(_n).get('turnover').get(year)

    def load(self, infile):
        """ load yaml data from a file
        :param infile:
        """
        from io import IOBase
        from yaml import safe_load
        if isinstance(infile, IOBase):
            self.employees = safe_load(infile)
        else:
            _fh = open(infile, 'r')
            self.employees = safe_load(_fh)
            _fh.close()

    def dump(self):
        """
        dump imported yaml
        """
        from yaml import dump
        return dump(self.employees)

    def get_name(self, eid):
        """ Returns name of employee by id.
        :param eid:
        """
        name = None
        for _n in self.employees.keys():
            if eid == self.employees.get(_n).get('id'):
                name = _n
                break
        return name

    def get_by_id(self, eid):
        """ Returns turnover for all years for an employee by id.
        :param eid:
        """
        turnovers = list(self.filter_by_id(eid))
        if turnovers:
            total = sum(turnovers)
        else:
            total = None
        return total

    def get_by_name(self, name):
        """ Returns turnover for all years for an employee by name.
        :param name:
        """
        if name in self.employees.keys():
            total = sum(self.filter_by_name(name))
        else:
            total = None
        return total

    def get_by_year(self, year):
        """ Returns turnover for all employees by year.
        :param year:
        """
        total = sum(self.filter_by_year(year))
        return total

    def get_for_name_by_year(self, name, year):
        """ Returns turnover for an employee for a specific year.
        :param year:
        :param name:
        """
        if name in self.employees.keys():
            turnovers = list(
                self.employees.get(name).get('turnover').get(_t)
                for _t in self.employees.get(name).get('turnover')
                if _t == year)
            if turnovers:
                total = sum(turnovers)
            else:
                total = None
        else:
            total = None
        return total

    def list_by_id(self, eid):
        """ List turnover by id.
        :param eid:
        """
        turnovers = list(self.filter_by_id(eid))
        if turnovers:
            pass
        else:
            turnovers = None
        return turnovers

    def list_by_name(self, name):
        """ List turnover by name.
        :param name:
        """
        if name in self.employees.keys():
            turnovers = list(self.filter_by_name(name))
        else:
            turnovers = None
        return turnovers

    def list_by_year(self, year):
        """ List turnover by year.
        :param year:
        """
        turnovers = list(self.filter_by_year(year))
        if turnovers:
            pass
        else:
            turnovers = None
        return turnovers
