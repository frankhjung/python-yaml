#!/usr/bin/env make

.DEFAULT_GOAL := default

.PHONY: check clean dist doc help run test

SHELL	:= /bin/sh
COMMA	:= ,
EMPTY	:=
SPACE	:= $(EMPTY) $(EMPTY)
PYTHON	:= /usr/bin/python3

SRCS	:= read_yaml.py employees/*.py utils/*.py tests/*.py

default:	check test

all:	check test run doc dist

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: check style and lint code"
	@echo "  run:   run against test data"
	@echo "  test:  run unit tests"
	@echo "  dist:  create a distrbution archive"
	@echo "  doc:   create documentation including test converage and results"
	@echo "  clean: delete all generated files"
	@echo
	@echo "Initialise virtual environment (venv) with:"
	@echo
	@echo "pip install -U virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip install -Ur requirements.txt"
	@echo
	@echo "Start virtual environment (venv) with:"
	@echo
	@echo "source venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo

check:
	# ctags for vim
	ctags --recurse -o tags $(SRCS)
	# sort imports
	isort $(SRCS)
	# format code to googles style
	black -q $(SRCS) setup.py
	# check with pylint
	pylint $(SRCS)
	# check distutils
	$(PYTHON) setup.py check

test:
	pytest -v --cov-report term-missing --cov=employees tests/

doc:
	# create sphinx documentation
	pytest -v --html=cover/report.html --cov=employees --cov-report=html:cover tests/
	(cd docs; make html)

dist:
	# create source package and build distribution
	$(PYTHON) setup.py clean
	$(PYTHON) setup.py sdist --dist-dir=target/dist
	$(PYTHON) setup.py build --build-base=target/build
	cp -pr target/docs/html public
	cp -p target/dist/*.tar.gz public

run:
	$(PYTHON) -m read_yaml -v tests/test.yaml
	$(PYTHON) -m read_yaml -h
	$(PYTHON) -m read_yaml --version

version:
	$(PYTHON) -m main --version

clean:
	# clean build distribution
	$(PYTHON) setup.py clean
	# clean generated documents
	(cd docs; make clean)
	$(RM) -rf cover
	$(RM) -rf .coverage
	$(RM) -f  *.log *.log.*
	$(RM) -rf __pycache__ employees/__pycache__ tests/__pycache__
	$(RM) -rf public
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover

