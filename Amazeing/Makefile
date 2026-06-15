# Variables
PYTHON = python3
PIP = pip3
VENV = .venv
ACTIVATE = . $(VENV)/bin/activate

.PHONY: install run debug clean lint

install:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) && $(PIP) install --upgrade pip setuptools build flake8 mypy

run:
	$(ACTIVATE) && $(PYTHON) amaze_ing.py config.txt

debug:
	$(ACTIVATE) && $(PYTHON) -m pdb amaze_ing.py config.txt

lint:
	$(ACTIVATE) && flake8 src/ amaze_ing.py
	$(ACTIVATE) && mypy src/ amaze_ing.py --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

# Chapter VI Package Building Rule
build-package:
	$(ACTIVATE) && $(PYTHON) -m build
	mv dist/mazegen-1.0.0-py3-none-any.whl .
	mv dist/mazegen-1.0.0.tar.gz .
	rm -rf dist build *.egg-info

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
	rm -rf src/**/__pycache__ src/**/*.pyc
	rm -rf $(VENV) build dist *.egg-info
	rm -f mazegen-1.0.0*