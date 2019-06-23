#!/bin/bash

source /rbin/common.sh

check_if_sudo

settings_file_src="/domoticz/domoticz.conf"
settings_file_dest="/etc/domoticz/domoticz.conf"
service_file="/domoticz/domoticz-sensors.service"

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
	'install')
		sudo cp ${service_file} "/lib/systemd/system/${service_file}"
		sudo cp ${settings_file_src} ${setting_file_dest}
		sudo systemctl daemon-reload
		;;

	'remove')
		sudo rm ${service_file}
		sudo systemctl daemon-reload
		;;

	'start')
		sudo systemctl enable ${service_file}
		sudo systemctl start ${service_file}
		;;

	'stop')
		sudo systemctl disable ${service_file}
		sudo systemctl stop ${service_file}
		;;

	*)
		echo 'wrong parameter'
		;;

esac


exit 0
