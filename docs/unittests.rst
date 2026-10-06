.. _unittests:

Unit Tests
==========

Unit tests are performed using `PyTest <https://docs.pytest.org/>`_.

Code coverage is reported by `Coverage <https://coverage.readthedocs.io/>`_.

Both reports are collated when the Sphinx documentation is built (see also
:doc:`references`). For module details, see :doc:`test_employees`.

Unit Test Results
-----------------

To run the unit tests::

   uv run pytest -v tests/ --cov=employees --cov=utils --cov=read_yaml

To generate an HTML report with coverage::

   uv run pytest -v --html=cover/report.html \
      --cov=employees --cov=utils --cov=read_yaml tests/

**Report** `Unit Tests <_static/report.html>`_

Unit Test Coverage
------------------

To generate a report on test coverage::

   uv run pytest -v \
      --cov=employees --cov=utils --cov=read_yaml tests/
   uv run coverage html -d cover

**Report** `Test Coverage <_static/index.html>`_

.. EOF
