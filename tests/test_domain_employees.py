# pylint: disable=C0111
"""
Unit tests for the new pure functional employees domain.
"""

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

RAW_DATA = {
    "frank": {"id": 3, "turnover": {2011: 100000, 2012: 140000, 2013: 200000}},
    "jo": {"id": 4, "turnover": {2012: 130000, 2013: 220000, 2014: 210000}},
}


def test_parse_employees():
    employees = parse_employees(RAW_DATA)
    assert len(employees) == 2
    assert employees[0] == Employee(
        name="frank", id=3, turnover={2011: 100000, 2012: 140000, 2013: 200000}
    )


def test_get_name_by_id():
    employees = parse_employees(RAW_DATA)
    assert get_name_by_id(employees, 3) == "frank"
    assert get_name_by_id(employees, 999) is None


def test_sum_turnover_by_id():
    employees = parse_employees(RAW_DATA)
    assert sum_turnover_by_id(employees, 3) == 440000
    assert sum_turnover_by_id(employees, 999) is None


def test_sum_turnover_by_name():
    employees = parse_employees(RAW_DATA)
    assert sum_turnover_by_name(employees, "frank") == 440000
    assert sum_turnover_by_name(employees, "badname") is None


def test_sum_turnover_by_year():
    employees = parse_employees(RAW_DATA)
    assert sum_turnover_by_year(employees, 2012) == 270000
    assert sum_turnover_by_year(employees, 1999) == 0


def test_get_turnover_for_name_by_year():
    employees = parse_employees(RAW_DATA)
    assert get_turnover_for_name_by_year(employees, "frank", 2012) == 140000
    assert get_turnover_for_name_by_year(employees, "badname", 2012) is None
    assert get_turnover_for_name_by_year(employees, "frank", 1999) is None


def test_list_turnover_by_id():
    employees = parse_employees(RAW_DATA)
    assert list_turnover_by_id(employees, 3) == [100000, 140000, 200000]
    assert list_turnover_by_id(employees, 999) is None


def test_list_turnover_by_name():
    employees = parse_employees(RAW_DATA)
    assert list_turnover_by_name(employees, "frank") == [100000, 140000, 200000]
    assert list_turnover_by_name(employees, "badname") is None


def test_list_turnover_by_year():
    employees = parse_employees(RAW_DATA)
    assert list_turnover_by_year(employees, 2013) == [200000, 220000]
    assert list_turnover_by_year(employees, 1999) is None
