#!/usr/bin/env make

.DEFAULT_GOAL := default

.PHONY: check clean dist doc help run test

PYTHON   := uv run python
RUFF     := uv run ruff
PYLINT   := uv run pylint
PYTEST   := uv run pytest
YAMLLINT := uv run yamllint
CTAGS    := $(shell command -v ctags 2>/dev/null)

SRCS     := $(shell find . -name "*.py" -not -path "./.venv/*")
YAMLS    := $(wildcard tests/*.yaml)

default:	check test version ## default goal

all:	check test run doc dist ## check cover run test doc dist

help: ## display this help
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo
	@echo "To initialize and install dependencies managed by uv:"
	@echo
	@echo "uv sync"
	@echo
	@echo "To run commands in the virtual environment:"
	@echo
	@echo "uv run <command>"
	@echo
	$(PYTHON) -m read_yaml -h

check: ## check style and lint code
ifdef CTAGS
	# ctags for vim
	ctags --recurse -o tags $(SRCS)
endif
	# format and check code using ruff
	$(RUFF) check $(SRCS)
	$(RUFF) format --check $(SRCS)
	# check with pylint
	$(PYLINT) $(SRCS)
	# check yaml
	$(YAMLLINT) --strict $(YAMLS)

test: ## run unit tests
	$(PYTEST) -v --cov-report term-missing --cov=employees tests/

doc: ## create documentation including test coverage and results
	# create sphinx documentation
	$(PYTEST) -v --html=cover/report.html --cov=employees --cov-report=html:cover tests/
	$(MAKE) -C docs html

dist: ## create a distribution archive
	cp -pr target/docs/html public

run: ## run against test data
	$(PYTHON) -m read_yaml -v tests

version: ## display version information
	$(PYTHON) -m read_yaml --version

clean: ## delete all generated files
	# clean generated files
	$(MAKE) -C docs clean
	$(RM) -r tags MANIFEST *.log *.log.* build cover .coverage dist public target __pycache__ **/__pycache__
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover *.pyc *.pyo *.py,cover
