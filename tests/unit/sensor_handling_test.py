import os
import pytest
from libs.parse_config import Config
from libs.sensor_handling import Sensor


def get_config_file_path():
    return os.getcwd() + '/tools/domoticz.conf'


def test_handle_sensor():
    config = Config()
    config.set_config(get_config_file_path())
    count = config.get_sensors_count()
    assert count == '4'
    assert int(count) == 4

    name = config.get_sensor_name(0)
    assert name == 'dummy_sensor'

    sensor = Sensor(name, config)
    assert sensor is not None

    done = sensor.handle_sensor(True)
    assert done is True


def test_get_json():
    config = Config()
    config.set_config(get_config_file_path())
    count = config.get_sensors_count()
    assert count == '4'
    assert int(count) == 4

    name = config.get_sensor_name(0)
    assert name == 'dummy_sensor'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 0
    sensor.stype = "dummy"
    json = sensor.get_json()
    assert json is not None


def test_get_ds1820_json():
    config = Config()
    config.set_config(get_config_file_path())
    count = config.get_sensors_count()
    assert count == '4'
    assert int(count) == 4

    name = config.get_sensor_name(2)
    assert name == 'rpi_ds1820'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 0
    json = sensor.get_ds1820_temperature_json()
    assert json is not None


def test_get_cpu_temperature_json():
    config = Config()
    config.set_config(get_config_file_path())
    count = config.get_sensors_count()
    assert count == '4'
    assert int(count) == 4

    name = config.get_sensor_name(1)
    assert name == 'rpi_cpu_temp'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 1
    json = sensor.get_rpi_cpu_temperature_json()
    assert json is not None


def test_get_io_input_json():
    config = Config()
    config.set_config(get_config_file_path())
    count = config.get_sensors_count()
    assert count == '4'
    assert int(count) == 4

    name = config.get_sensor_name(3)
    assert name == 'rpi_button'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 6
    json = sensor.get_io_input_json()
    assert json is not None
