#!/bin/bash

python -m pytest tests/ --cov=libs --cov-report=html --cov-report=annotate
