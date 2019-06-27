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
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)

    def test_load_by_file(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)

    def test_dump(self):
        _e = Employees(self.TEST_FILE)
        dump = _e.dump()
        self.assertEqual(13, len(dump.split('\n')))
        self.assertIn('frank:', dump)
        self.assertIn('jo:', dump)

    def test_name(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertEqual('frank', _e.get_name(3))
        self.assertEqual('jo', _e.get_name(4))

    def test_by_name(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertEqual(440000, _e.get_by_name('frank'))
        self.assertEqual(560000, _e.get_by_name('jo'))

    def test_for_name_by_year(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertEqual(100000, _e.get_for_name_by_year(name='frank',
                                                         year=2011))
        self.assertEqual(140000, _e.get_for_name_by_year(name='frank',
                                                         year=2012))
        self.assertEqual(200000, _e.get_for_name_by_year(name='frank',
                                                         year=2013))
        self.assertEqual(130000, _e.get_for_name_by_year(name='jo', year=2012))
        self.assertEqual(220000, _e.get_for_name_by_year(name='jo', year=2013))
        self.assertEqual(210000, _e.get_for_name_by_year(name='jo', year=2014))

    def test_by_year(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertEqual(100000, _e.get_by_year(2011))
        self.assertEqual(270000, _e.get_by_year(2012))
        self.assertEqual(420000, _e.get_by_year(2013))
        self.assertEqual(210000, _e.get_by_year(2014))

    def test_list_by_id(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        turnovers = list(_e.list_by_id(3))
        self.assertEqual(3, len(turnovers))
        self.assertIn(100000, turnovers)
        self.assertIn(140000, turnovers)
        self.assertIn(200000, turnovers)
        self.assertNotIn(220000, turnovers)

    def test_list_by_name(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        turnovers = list(_e.list_by_name('frank'))
        self.assertEqual(3, len(turnovers))
        self.assertIn(100000, turnovers)
        self.assertIn(140000, turnovers)
        self.assertIn(200000, turnovers)
        self.assertNotIn(220000, turnovers)

    def test_list_by_year(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        turnover = list(_e.list_by_year(2013))
        self.assertEqual(2, len(turnover))
        self.assertIn(200000, turnover)
        self.assertIn(220000, turnover)
        self.assertNotIn(2013, turnover)

    def test_bad_id(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.get_name(1))

    def test_bad_by_id(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.get_by_id(1))

    def test_bad_by_name_(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.get_by_name('badname'))

    def test_bad_by_year(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertEqual(0, _e.get_by_year(1999))

    def test_bad_for_name_by_year(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.get_for_name_by_year('frank', 1999))
        self.assertIsNone(_e.get_for_name_by_year('jo', 1999))
        self.assertIsNone(_e.get_for_name_by_year('badname', 2011))
        self.assertIsNone(_e.get_for_name_by_year('badname', 2012))
        self.assertIsNone(_e.get_for_name_by_year('badname', 2013))
        self.assertIsNone(_e.get_for_name_by_year('badname', 2014))

    def test_bad_list_by_id(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.list_by_id(1))

    def test_bad_list_by_name(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.list_by_name('badname'))

    def test_bad_list_by_year(self):
        _e = Employees(self.TEST_FILE)
        self.assertIsNotNone(_e)
        self.assertIsNone(_e.list_by_year(1999))


#
# MAIN
#
if __name__ == '__main__':
    unittest.main()
