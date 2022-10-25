#!/bin/bash
set -e
pylint src
flake8 src
mypy src
