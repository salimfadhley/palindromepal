#!/usr/bin/env bash
python -m pip install --upgrade -r src/requirements.txt -r src/requirements_dev.txt
python src/setup.py develop