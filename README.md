Domoticz Virtual Device Daemon
------------------------------

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9944bcf3ac45463782a51dc3d0af4eef)](https://www.codacy.com/app/sebastian_16/dvdd?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sebastianbasierski/dvdd&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/sebastianbasierski/dvdd/badge/master)](https://www.codefactor.io/repository/github/sebastianbasierski/dvdd/overview/master)
[![codecov](https://codecov.io/gh/sebastianbasierski/dvdd/branch/master/graph/badge.svg)](https://codecov.io/gh/sebastianbasierski/dvdd)
<br>
<br>
Domoticz Virtual Device Daemon is a project allowing to handle multiple<br>
Domoticz virtual devices on one physical linux board. It does not matter<br>
if this is a small board or regular desktop pc (of course some devices may<br>
not be supported on various platforms).
<br>

Installation
------------
Preffered way of installation is to use setup.sh script.<br>
``` bash
./setup.sh install
```
Please note, that installation should be executed as root user, <br>
since systemd service is added during this process.<br>

Configuration
-------------
DVDD's default config file is placed in /etc/domoticz/domoticz.conf.<br>
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

There are also sensors sections. User should set proper 'count' value.
```
[sensors]
count=1 # sensors count
sensor0=dummy_sensor

[dummy_sensor]
idx=0
type=dummy
interval=30s
```

There are some parameters to be set:
*   idx<br>
Parameter have to be retreived from domoticz instance.<br>

*   type<br>
Sensor type (explained below).<br>

*   interval<br>
Only for sensors that sends data to domoticz instance.<br>

*   gpio<br>
Only for I/O sensors.<br>

Sensor types:
*   dummy_sensor<br>
Sensor basically do nothing, except sending fixed value ('1') in given interval.<br>

*   temperature_rpi_cpu<br>
Sensor grabs raspberry pi cpu temperature.<br>

*   temperature_ds1820<br>
Sensor gets temperature from ds1820 sensor (for now only one sensor).<br>

*   io_input<br>
Sensor gets cpu I/O state.<br>
Only for raspberry pi and other SoCs, not applicable for x86 cpus.<br>
This sensor must have an 'gpio' parameter set.<br>

Start/Stop
----------
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

Domoticz Configuration
----------------------
|DVDD               |Domoticz    |
|:-----------------:|:----------:|
|dummy_sensor       |Dummy       |
|temperature_rpi_cpu|Temp        |
|temperature_ds1820 |Temp        |
|io_input           |General     |