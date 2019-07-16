Domoticz Virtual Device Daemon
------------------------------

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9944bcf3ac45463782a51dc3d0af4eef)](https://www.codacy.com/app/sebastian_16/dvdd?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sebastianbasierski/dvdd&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/sebastianbasierski/dvdd/badge/master)](https://www.codefactor.io/repository/github/sebastianbasierski/dvdd/overview/master)
[![Coverage Status](https://coveralls.io/repos/github/sebastianbasierski/dvdd/badge.svg?branch=master)](https://coveralls.io/github/sebastianbasierski/dvdd?branch=master)
<br>
<br>
Domoticz Virtual Device Daemon is a project allowing to handle multiple Domoticz virtual devices on one physical linux board.<br>
It does not matter if this is a small board or regular desktop pc (of course some devices may not be supported on various platforms).
<br>

Installation
------------
Preffered way of installation is to use setup.sh script.<br>
``` bash
./setup.sh install
```
Please note, that installation should be executed as root user, <br>
since systemd service is added during this process.<br>

Configure
------------
DVDD's default config file is places in /etc/domoticz/domoticz.conf.<br>
It contains at least 3 sections:
```
[general]
debug=1 # prints debug message to log
local_port=8080 # sets local server port (for handling output devices)

[server]
ip=172.16.2.40 # domoticz server ip address
port=8080 # domoticz server port

[sensors]
count=0 # sensors count
```

There are also sensors sections
```
[dummy_sensor]
idx=0
type=dummy
interval=30s
```
Each devices should have set parameters :
* idx<br>
Parameter have to be get from domoticz instance.<br>

* type<br>
Sensor type (explained below).<br>

* interval<br>
Only for sensors that sends data to domoticz instance.<br>


Sensor type:
* dummy_sensor<br>
Sensor basically do nothing, except sensing fixed value ('1') in given interval.<br>

* temperature_rpi_cpu<br>
Sensor grabs raspberry pi cpu temperature.<br>

* temperature_ds1820<br>
Sensor gets temperature from ds1820 sensor (for now only one sensor per bus is
allowed).<br>

* io_input<br>
Sensor gets cpu I/O state.<br>
Only for raspberry pi and other SoCs, not applicable for x86 cpus.<br>
This sensor must have an 'gpio' parameter set.<br>

Start/Stop
------------
DVDD is controlled by systemd service, so can be started/stopped using <br>
standard commands<br>
``` bash
systemctl start domoticz-sensors.service
```
``` bash
systemctl stop domoticz-sensors.service
```
It can also be controlled using setup.sh script.<br>
``` bash
./setup.sh start
```
``` bash
./setup.sh stop
```

