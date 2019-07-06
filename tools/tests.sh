#!/bin/bash

python -m pytest tests/ --cov=libs --cov-report=html --cov-report=annotate
ret_val=$?

coverage=$(cat htmlcov/index.html | grep -A 5 Total | tail -n 1 | cut -d '>' -f 2 | cut -d '<' -f 1)
sudo cp htmlcov/* /var/www/html
echo "Total coverage $coverage"
exit $ret_val

