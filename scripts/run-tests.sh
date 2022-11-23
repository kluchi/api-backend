#!/bin/bash
set -e
export PYTHONPATH=src
coverage run -m pytest
coverage report
coverage xml
