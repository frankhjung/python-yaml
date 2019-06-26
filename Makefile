# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

.DEFAULT_GOAL := help

.PHONY: check clean doc help run test

COMMA	:= ,
EMPTY	:=
SPACE	:= $(EMPTY) $(EMPTY)

SRCS	:= main.py employees/employees.py tests/testemployees.py

all: check test run version

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: check style and lint code"
	@echo "  run:   run against test data"
	@echo "  test:  run unit tests"
	@echo "  clean: delete all generated files"
	@echo
	@echo "Activate virtual environment (venv) with:"
	@echo
	@echo "  pip3 install virtualenv"
	@echo "  python3 -m virtualenv venv"
	@echo "  source venv/bin/activate"
	@echo "  pip install -r requirements.txt"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "  deactivate"
	@echo
	@echo "TODO"
	@echo "  cover: run test coverage report"
	@echo "  dist:  create a distrbution archive"
	@echo "  doc:   create documentation including test converage and results"
	@echo

check:
	# format code to googles style
	yapf --style google -i $(SRCS) setup.py
	# check with pylint
	pylint3 $(SRCS)
	# check distutils
	python3 setup.py check

run:
	python3 -m main -v tests/test.yaml

test:
	coverage3 run -m unittest discover -s tests
	# python3 -m unittest --verbose discover -s tests
	coverage3 report employees/employees.py

doc:
	coverage3 html -d cover employees/employees.py

clean:
	# clean build distribution
	python setup.py clean
	# clean generated documents
	(cd docs; make clean)
	$(RM) -rf cover
	$(RM) -rf __pycache__ employees/__pycache__ tests/__pycache__
	$(RM) -rf target
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v README
	# $(RM) -v MANIFEST
	# $(RM) -f results.html
	# $(RM) -rf results/

version:
	python3 -m main --version

