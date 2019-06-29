# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

.DEFAULT_GOAL := help

.test PHONY: check clean dist doc help run test

SHELL	:= /bin/sh
COMMA	:= ,
EMPTY	:=
SPACE	:= $(EMPTY) $(EMPTY)

SRCS	:= main.py employees/employees.py tests/testemployees.py

all: check test dist doc run version

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
	@echo "Activate virtual environment (venv) with:"
	@echo
	@echo "pip3 install virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip3 install -r requirements.txt"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo
	@echo "TOOD"
	@echo "	- generate HTML version of unit tests"
	@echo "	- investigate why pylint slow on test classes"
	@echo "	- complete test coverage"

check:
	# format code to googles style
	yapf --style google --parallel -i $(SRCS) setup.py
	# check with pylint
	pylint3 $(SRCS)
	# check distutils
	python3 setup.py check

run:
	python3 -m main -v tests/test.yaml
	python3 -m main -h
	python3 -m main --version

test:
	# python3 -m unittest --verbose
	coverage3 run -m unittest --verbose
	coverage3 report employees/employees.py

dist:
	# copy readme for use in distribution
	# pandoc -t plain README.md > README
	# create source package and build distribution
	python3 setup.py clean
	python3 setup.py sdist --dist-dir=target/dist
	python3 setup.py build --build-base=target/build
	mv target/dist/*.tar.gz ./public/

doc:
	# unit test code coverage
	coverage3 report employees/employees.py
	coverage3 html -d cover employees/employees.py
	# create sphinx documentation
	(cd docs; make html)
	mv target/docs/html ./public

clean:
	# clean build distribution
	python setup.py clean
	# clean generated documents
	(cd docs; make clean)
	$(RM) -rf cover
	$(RM) -rf public
	$(RM) -rf __pycache__ employees/__pycache__ tests/__pycache__
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	$(RM) -v *.pyc *.pyo *.py,cover

version:
	python3 -m main --version

