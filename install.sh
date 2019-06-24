#!/bin/bash

source /rbin/common.sh

check_if_sudo

config_file="domoticz.conf"
service_file="domoticz-sensors.service"
local_dir="/domoticz"
settings_dir="/etc/domoticz"
settings_file_src="${local_dir}/${config_file}"
settings_file_dest="${settings_dir}/${config_file}"
service_file_src="${local_dir}/${service_file}"

if [ "$#" -eq 1 ]; then
	mode=$1
else
	echo "Nieprawidłowa ilość parametrów. Użycie $0 [tryb] [plik konfiguracyjny] [numer tunelu]"
	exit 1
fi

# check current dir
dir=$(pwd)

if [ "${dir}" != "${local_dir}" ]; then
	echo "Wrong directory. Please move scripts to ${local_dir}"
	exit 2
fi

case $mode in
	'install')
		sudo cp ${service_file} "/lib/systemd/system/${service_file}"
		sudo mkdir -p ${settings_dir}
		sudo cp ${settings_file_src} ${settings_file_dest}
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
