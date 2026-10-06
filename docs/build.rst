.. _build:

How to build the project using GNU make
=======================================

Get help on `GNU Make <https://www.gnu.org/software/make/>`_ targets using::

   make help

Dependencies are synchronised using `uv`_::

   uv sync

Build everything, including PyDoc documentation, by running::

   make clean all

See :download:`Makefile <../Makefile>` for details.

.. _uv: https://docs.astral.sh/uv/

.. EOF
