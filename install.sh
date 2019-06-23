#!/bin/bash

source /rbin/common.sh

check_if_sudo

settings_file="/domoticz/domoticz.conf"

function prepare_mtun {
	# check if we have git installed
	# check if we have build-essential installed
	cd /tmp
	git clone git@gitlab.basierski.pl:LinuxSoftware/main.git
	cd main
	git checkout mtun
	git-manager clone
	./build.sh install
}

if [ "$#" -eq 2 ]; then
	mode=$1
	number=$2
elif [ "$#" -eq 3 ]; then
	mode=$1
	settings_file=$2
	number=$3
else
	echo "Nieprawidłowa ilość parametrów. Użycie $0 [tryb] [plik konfiguracyjny] [numer tunelu]"
	exit 1
fi

case $mode in
	'install-client')
		sudo cp /rbin/mtun-client.service "/lib/systemd/system/mtun-client_$number.service"
		sed -i "s:ExecStart=/rbin/mtun-client-start.sh:ExecStart=/rbin/mtun-client-start.sh $settings_file:g" "/lib/systemd/system/mtun-client_$number.service"
		sudo systemctl daemon-reload
		;;

	'install-server')
		sudo cp /rbin/mtun-server.service "/lib/systemd/system/mtun-server_$number.service"
		sed -i "s:ExecStart=/rbin/mtun-server-start.sh:ExecStart=/rbin/mtun-server-start.sh $settings_file:" "/lib/systemd/system/mtun-server_$number.service"
		sudo systemctl daemon-reload
		;;

	'remove')
		sudo rm "/lib/systemd/system/mtun-*_$number.service"
		sudo systemctl daemon-reload
		;;

	'start-client')
		sudo systemctl enable "mtun-client_$number.service"
		sudo systemctl start "mtun-client_$number.service"
		;;

	'start-server')
		sudo systemctl enable "mtun-server_$number.service"
		sudo systemctl start "mtun-server_$number.service"
		;;

	'stop-client')
		sudo systemctl disable "mtun-client_$number.service"
		sudo systemctl stop "mtun-client_$number.service"
		;;

	'stop-server')
		sudo systemctl disable "mtun-server_$number.service"
		sudo systemctl stop "mtun-server_$number.service"
		;;

	*)
		echo 'wrong parameter'
		;;

esac


exit 0
