#!/bin/bash

if [ "$EUID" -ne 0 ]
		then echo "Please run as root"
				exit
			fi

			apt update
			apt install python-pip -yq

			#pip install coverage
			pip install pytest
			pip install pytest-cov
			pip install pytest-xdist
			pip install pytest-bdd

