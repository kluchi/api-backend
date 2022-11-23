#!/bin/bash
set -e
export PYTHONPATH=src
pylint src tests
flake8 src tests

export MYPYPATH=src
mypy --explicit-package-bases src
