#!/bin/bash

#mkdir reports
#touch reports/.coverage

python -m pytest tests/ --cov=libs --cov-report=html --cov-report=annotate
ret_val=$?

#rm -rf csg.tar.gz
#tar -zcvf csg.tar.gz reports/cover/*
#scp -i ~/.ssh/id_rsa_cov csg.tar.gz rumcajs@basierski.pl:
#coverage=$(cat htmlcov/cover/index.html | grep pc_cov | cut -d '>' -f 2 | cut -d '%' -f 1)
coverage=$(cat htmlcov/index.html | grep -A 5 Total | tail -n 1 | cut -d '>' -f 2 | cut -d '<' -f 1)
sudo cp htmlcov/* /var/www/html
echo "Total coverage $coverage"
exit $ret_val

