#!/bin/bash

python -m pytest tests/ --cov=libs --cov-report term  --cov-report=annotate
