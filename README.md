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