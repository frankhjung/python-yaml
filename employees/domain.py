"""
Pure functional domain logic for employees.
"""

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

type Year = int
type Turnover = int
type TurnoverMap = dict[Year, Turnover]
type EmployeeRoster = tuple[Employee, ...]


@dataclass(frozen=True, slots=True)
class Employee:
    """Immutable data structure representing an employee."""

    name: str
    id: int
    turnover: TurnoverMap


def parse_employees(data: dict[str, Any]) -> EmployeeRoster:
    """Parse raw dictionary into Employee datastructures."""
    return tuple(
        Employee(
            name=name, id=emp_data["id"], turnover=emp_data.get("turnover", {})
        )
        for name, emp_data in data.items()
    )


def get_name_by_id(employees: Iterable[Employee], eid: int) -> str | None:
    """Returns the name of employee by id."""
    return next((emp.name for emp in employees if emp.id == eid), None)


def sum_turnover_by_id(employees: Iterable[Employee], eid: int) -> int | None:
    """Returns the turnover for all years for an employee by id."""
    turnovers = list_turnover_by_id(employees, eid)
    return sum(turnovers) if turnovers is not None else None


def sum_turnover_by_name(
    employees: Iterable[Employee], name: str
) -> int | None:
    """Returns turnover for all years for an employee by name."""
    turnovers = list_turnover_by_name(employees, name)
    return sum(turnovers) if turnovers is not None else None


def sum_turnover_by_year(employees: Iterable[Employee], year: int) -> int:
    """Returns turnover for all employees by year."""
    turnovers = list_turnover_by_year(employees, year)
    return sum(turnovers) if turnovers else 0


def get_turnover_for_name_by_year(
    employees: Iterable[Employee], name: str, year: int
) -> int | None:
    """Returns turnover for an employee for a specific year."""
    return next(
        (emp.turnover.get(year) for emp in employees if emp.name == name),
        None,
    )


def list_turnover_by_id(
    employees: Iterable[Employee], eid: int
) -> list[int] | None:
    """List turnover by id."""
    return next(
        (list(emp.turnover.values()) for emp in employees if emp.id == eid),
        None,
    )


def list_turnover_by_name(
    employees: Iterable[Employee], name: str
) -> list[int] | None:
    """List turnover by name."""
    return next(
        (list(emp.turnover.values()) for emp in employees if emp.name == name),
        None,
    )


def list_turnover_by_year(
    employees: Iterable[Employee], year: int
) -> list[int] | None:
    """List turnover by year."""
    turnovers = [
        emp.turnover[year] for emp in employees if year in emp.turnover
    ]
    return turnovers if turnovers else None
