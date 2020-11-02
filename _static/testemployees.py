#!/usr/bin/env python
# coding: utf-8
# pylint: disable=C0111
# pylint: disable=R0904
"""
Run unit tests for YAML file processing example.
"""

import os
import unittest
from employees.employees import Employees


class TestEmployees(unittest.TestCase):
    """ Tests for Employees. """

    __version__ = Employees.__version__

    TEST_FILE = 'tests/test.yaml'

    @classmethod
    def setUpClass(cls):
        print(cls.__name__, cls.__version__)

    def setUp(self):
        test_file = os.path.join(os.getcwd(), self.TEST_FILE)
        self.assertTrue(os.access(test_file, os.R_OK))

    def test_load_by_name(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)

    def test_load_by_file(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)

    def test_dump(self):
        employees = Employees(self.TEST_FILE)
        dump = employees.dump()
        self.assertIn('frank:', dump)
        self.assertIn('jo:', dump)

    def test_name(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual('frank', employees.get_name(3))
        self.assertEqual('jo', employees.get_name(4))

    def test_by_name(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual(440000, employees.get_by_name('frank'))
        self.assertEqual(560000, employees.get_by_name('jo'))

    def test_for_name_by_year(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual(
            100000, employees.get_for_name_by_year(name='frank', year=2011))
        self.assertEqual(
            140000, employees.get_for_name_by_year(name='frank', year=2012))
        self.assertEqual(
            200000, employees.get_for_name_by_year(name='frank', year=2013))
        self.assertEqual(130000,
                         employees.get_for_name_by_year(name='jo', year=2012))
        self.assertEqual(220000,
                         employees.get_for_name_by_year(name='jo', year=2013))
        self.assertEqual(210000,
                         employees.get_for_name_by_year(name='jo', year=2014))

    def test_by_year(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual(100000, employees.get_by_year(2011))
        self.assertEqual(270000, employees.get_by_year(2012))
        self.assertEqual(420000, employees.get_by_year(2013))
        self.assertEqual(210000, employees.get_by_year(2014))

    def test_list_by_id(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        turnovers = list(employees.list_by_id(3))
        self.assertEqual(3, len(turnovers))
        self.assertIn(100000, turnovers)
        self.assertIn(140000, turnovers)
        self.assertIn(200000, turnovers)
        self.assertNotIn(220000, turnovers)

    def test_list_by_name(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        turnovers = list(employees.list_by_name('frank'))
        self.assertEqual(3, len(turnovers))
        self.assertIn(100000, turnovers)
        self.assertIn(140000, turnovers)
        self.assertIn(200000, turnovers)
        self.assertNotIn(220000, turnovers)

    def test_list_by_year(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        turnover = list(employees.list_by_year(2013))
        self.assertEqual(2, len(turnover))
        self.assertIn(200000, turnover)
        self.assertIn(220000, turnover)
        self.assertNotIn(2013, turnover)

    def test_bad_id(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.get_name(1))

    def test_bad_by_id(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.get_by_id(1))

    def test_bad_by_name_(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.get_by_name('badname'))

    def test_bad_by_year(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual(0, employees.get_by_year(1999))

    def test_bad_for_name_by_year(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.get_for_name_by_year('frank', 1999))
        self.assertIsNone(employees.get_for_name_by_year('jo', 1999))
        self.assertIsNone(employees.get_for_name_by_year('badname', 2011))
        self.assertIsNone(employees.get_for_name_by_year('badname', 2012))
        self.assertIsNone(employees.get_for_name_by_year('badname', 2013))
        self.assertIsNone(employees.get_for_name_by_year('badname', 2014))

    def test_bad_list_by_id(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.list_by_id(1))

    def test_bad_list_by_name(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.list_by_name('badname'))

    def test_bad_list_by_year(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.list_by_year(1999))
