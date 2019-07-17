import os
from libs.parse_config import *


def get_config_file_path():
    return os.getcwd() + '/tools/domoticz.conf'


def test_set_file():
    config = Config()
    ret = config.set_config('/domoticz/x.conf')
    assert ret is False

    port = config.get_gpio('rpi_button')
    assert port is None

    ret = config.set_config(get_config_file_path())
    assert ret is True


def test_get_sensors_count():
    config = Config()
    config.set_config(get_config_file_path())
    count = config.get_sensors_count()
    assert count == '4'
    assert int(count) == 4


def test_get_sensor_name():
    config = Config()
    config.set_config(get_config_file_path())
    name = config.get_sensor_name(0)
    assert name == 'dummy_sensor'

    name = config.get_sensor_name(5)
    assert name is None


def test_get_sensor_idx():
    config = Config()
    config.set_config(get_config_file_path())
    idx = config.get_sensor_idx('dummy_sensor')
    assert idx == '0'
    assert int(idx) == 0

    idx = config.get_sensor_idx('rpi_cppu_temp')
    assert int(idx) == -1


def test_get_sensor_type():
    config = Config()
    config.set_config(get_config_file_path())
    stype = config.get_sensor_type('dummy_sensor')
    assert stype == 'dummy'

    stype = config.get_sensor_type('rpi_cppu_temp')
    assert stype is None


def test_get_sensor_interval():
    config = Config()
    config.set_config(get_config_file_path())
    interval = config.get_sensor_interval('dummy_sensor')
    assert interval == '30s'

    interval = config.get_sensor_interval('rpi_cppu_temp')
    assert interval is None


def test_get_server_ip():
    config = Config()
    config.set_config(get_config_file_path())
    ip = config.get_server_ip()
    assert ip == '172.16.2.40'


def test_get_server_port():
    config = Config()
    config.set_config(get_config_file_path())
    port = config.get_server_port()
    assert port == '8080'


def test_get_debug():
    config = Config()
    config.set_config(get_config_file_path())
    debug = config.get_debug()
    assert debug == '1'


def test_get_local_port():
    config = Config()
    config.set_config(get_config_file_path())
    port = config.get_local_port()
    assert port == '8079'


def test_get_gpio():
    config = Config()
    config.set_config(get_config_file_path())
    gpio = config.get_gpio('dummy')
    assert gpio is None
