.. _unittests:

Unit Tests
==========

Unit tests are performed using `PyTest <references.html>`_.

Code coverage is reported by `Coverage <references.html>`_.

Both reports are collated during when `Sphinx <references.html>`_ documentation
is built.

Unit Test Results
-----------------

To run the unit tests::

   pytest -v tests/test*.py

To generate a HTML report with coverage run::

   pytest -v --html=cover/report.html --cov=employees tests/test*.py

**Report** `Unit Tests <_static/report.html>`_

Unit Test Coverage
------------------

To generate a report on test coverage::

   pytest -v --cov=helloworld tests/test*.py
   coverage html -d cover helloworld/helloworld.py

**Report** `Test Coverage <_static/index.html>`_

.. EOF
