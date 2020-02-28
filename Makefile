all: venv install hooks

venv:
	python3 -m venv .venv

hooks:
	.venv/bin/pre-commit install

test:
	.venv/bin/pytest

coverage:
	.venv/bin/coverage run -m pytest
	.venv/bin/coverage report

pip:
	.venv/bin/pip install -U pip

install:
	.venv/bin/pip install -e ".[dev]"

.PHONY: all venv hooks test coverage
