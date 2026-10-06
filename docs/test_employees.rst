.. _test_employees:

Unit Test Modules
=================

This section documents the unit test modules for both the pure functional
domain (``employees.domain``) and the backward-compatible ``Employees``
facade.

The unit test execution and coverage reports are available from
:doc:`unittests`.

Domain Unit Tests
-----------------

The ``tests.test_domain_employees`` module tests the pure domain functions
and data structures:

.. automodule:: tests.test_domain_employees
   :members:

:download:`Domain Tests Source <../tests/test_domain_employees.py>`

Employees Facade Unit Tests
---------------------------

The ``tests.test_employees`` module tests the ``Employees`` class facade and
YAML loading:

.. automodule:: tests.test_employees
   :members:

:download:`Facade Tests Source <../tests/test_employees.py>`

.. EOF
