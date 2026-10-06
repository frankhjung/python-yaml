.. _main:

Main
====

This application demonstrates the following tools and packages (see also
:doc:`references`):

* build project using `GNU Make <https://www.gnu.org/software/make/>`_
* format and lint code using `Ruff <https://docs.astral.sh/ruff/>`_
* manage dependencies using `uv <https://docs.astral.sh/uv/>`_
* document using `Sphinx <https://www.sphinx-doc.org/>`_
* lint code using `PyLint <https://www.pylint.org/>`_ and `yamllint`_
* process a YAML file using `PyYAML <https://pyyaml.org/>`_
* read module help using `PyDoc`_
* report test coverage using `Coverage`_
* unit test using `PyTest <https://docs.pytest.org/>`_

.. _yamllint: https://yamllint.readthedocs.io/
.. _PyDoc: https://docs.python.org/3/library/pydoc.html
.. _Coverage: https://coverage.readthedocs.io/

Get help for this module with::

   ./read_yaml.py -h
   pydoc3 read_yaml
   python -m read_yaml -h

This provides usage information and command line parameters.

The module reads YAML employee data from the command line and outputs
turnover reports using the domain functions and report utilities.

Module
------

.. automodule:: read_yaml
   :members:

:download:`Source <../read_yaml.py>`

Project History & Resources
---------------------------

* :download:`Architecture Decision Record (REQ-001) <REQ-001-pure-functions.md>`
* :download:`Glossary <../GLOSSARY.md>`
* :download:`License <../LICENSE.txt>`

.. EOF
