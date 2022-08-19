#!/usr/bin/env bash
python -m pip install --upgrade -r src/requirements.txt -r src/requirements_dev.txt
cd src
python setup.py develop