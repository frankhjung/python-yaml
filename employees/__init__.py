"""Employees package."""

from .domain import (
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
from .employees import Employees

__version__ = "2.0.0"

__all__ = [
    "Employee",
    "Employees",
    "__version__",
    "get_name_by_id",
    "get_turnover_for_name_by_year",
    "list_turnover_by_id",
    "list_turnover_by_name",
    "list_turnover_by_year",
    "parse_employees",
    "sum_turnover_by_id",
    "sum_turnover_by_name",
    "sum_turnover_by_year",
]
