import pytest
from libs.parse_config import *

def test_set_file():
    config = Config()
    config.set_config('/domoticz/domoticz.conf')
    assert config.file == '/domoticz/domoticz.conf'

def test_get_sensors_count():
    config = Config()
    count = config.get_sensors_count()
    assert count == '2'
    assert int(count) == 2

def test_get_sensor_name():
    config = Config()
    name = config.get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    name = config.get_sensor_name(3)
    assert name == None

def test_get_sensor_idx():
    config = Config()
    idx = config.get_sensor_idx('rpi_cpu_temp')
    assert idx == '1'
    assert int(idx) == 1

    idx = config.get_sensor_idx('rpi_cppu_temp')
    assert int(idx) == -1

def test_get_sensor_type():
    config = Config()
    stype = config.get_sensor_type('rpi_cpu_temp')
    assert stype == 'temperature'

    stype = config.get_sensor_type('rpi_cppu_temp')
    assert stype == None

def test_get_sensor_interval():
    config = Config()
    interval = config.get_sensor_interval('rpi_cpu_temp')
    assert interval == '30s'

    interval = config.get_sensor_interval('rpi_cppu_temp')
    assert interval == None

def test_get_server_ip():
    config = Config()
    ip = config.get_server_ip()
    assert ip == '172.16.2.40'

def test_get_server_port():
    config = Config()
    port = config.get_server_port()
    assert port == '8080'

def test_get_debug():
    config = Config()
    debug = config.get_debug()
    assert debug == '1'

def test_set_file():
    config = Config()
    ret = config.set_config('/domoticz/x.conf')
    assert ret == False

    ret = config.set_config('/domoticz/domoticz.conf')
    assert ret == True
    fname = config.file
    assert fname == '/domoticz/domoticz.conf'
