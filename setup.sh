#!/usr/bin/env bash
set -e
export PROJECT_NAME="palindromepal"
eval "$(conda shell.bash hook)"
conda create -y -n $PROJECT_NAME python==3.10
eval conda activate $PROJECT_NAME
which python
