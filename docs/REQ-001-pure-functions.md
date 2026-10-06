# REQ-001: Refactor Employees to Functional Core

## Context

The `Employees` class managed both file I/O and domain state, making unit
testing difficult and violating the separation of concerns. It exhibited low
leverage by repeating dictionary traversals for simple query methods.

## Decision

Adopt a **Data-Oriented** functional architecture.

1. Extract data structures into a frozen `Employee` dataclass.
2. Implement pure functions in `employees.domain` for all queries (e.g.,
   `sum_turnover_by_year`).
3. Retain the `Employees` class as a deprecated facade (Strangler Fig
   pattern) to ensure backward compatibility for existing callers like
   `utils/report.py`.

## Consequences

- **Positive**: High locality, trivial unit tests (no mocking file handles),
  decoupled I/O.
- **Negative**: Existing callers using the `Employees` object-oriented API
  will eventually need to migrate to the pure functional API.
