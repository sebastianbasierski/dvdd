import os
import time
import subprocess
from libs.sender import Sender
from libs.helpers import get_platform
from libs.parse_interval import *


class Sensor:
    def __init__(self, sensor, config):
        self.platform = get_platform()
        self.sensor = sensor
        self.config = config
        self.alive = True

        self.w1 = None
        self.rpi_gpio = None

        if self.platform != "arm":
            return

        try:
            import w1thermsensor as w1
            self.w1 = w1
        except ImportError:
            self.w1 = None

        try:
            import RPi.GPIO as GPIO
            self.rpi_gpio = GPIO
        except ImportError:
            self.rpi_gpio = None

    def stop(self):
        self.alive = False

    def get_simple_json(self, temp):
        idx_json = "json.htm?type=command&param=udevice&idx=" + str(self.idx)
        value_json = "&nvalue=0&svalue=" + str(temp)
        return idx_json + value_json

    def get_dummy_json(self):
        return self.get_simple_json('1')

    def get_io_input_json(self):
        if self.rpi_gpio is None:
            return "not supported"
        self.rpi_gpio.setmode(self.rpi_gpio.BCM)
        gpio = self.config.get_gpio(self.sensor)
        if gpio is None:
            return None

        self.rpi_gpio.setup(int(gpio),
                            self.rpi_gpio.IN,
                            pull_up_down=self.rpi_gpio.PUD_DOWN)
        val = self.rpi_gpio.input(int(gpio))
        return self.get_simple_json(str(val))

    def get_cpu_temperature_json(self):
        try:
            temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())
        except Exception:
            return "not supported"
        temp /= 1000.0
        return self.get_simple_json(temp)

    def get_ds1820_temperature_json(self):
        if self.w1 is None:
            return "not supported"
        ds_sensor = self.w1.W1ThermSensor()
        temp = ds_sensor.get_temperature()
        return self.get_simple_json(temp)

    def get_json(self):
        switcher = {
                "io_input": self.get_io_input_json,
                "dummy": self.get_dummy_json,
                "temperature": self.get_cpu_temperature_json,
                "temperature_ds1820": self.get_ds1820_temperature_json
        }

        func = switcher.get(self.stype, lambda: "Invalid sensor type")
        return func()

    def handle_sensor(self, one_time=None):
        one_time = one_time or False
        self.idx = self.config.get_sensor_idx(self.sensor)
        self.stype = self.config.get_sensor_type(self.sensor)
        interval = get_sensors_parse_interval(
                self.config.get_sensor_interval(self.sensor))

        ip = self.config.get_server_ip()
        port = self.config.get_server_port()
        sender = Sender(ip, port, self.idx)

        if int(interval) is None:
            return False

        while self.alive:
            # send data
            print "send data"
            json = self.get_json()
            if json is not None:
                sender.send(json)

            # sleep
            for i in range(int(interval)):
                # print alive value
                print "Alive " + str(self.alive)

                # sleep for a second
                time.sleep(1)

                # check exit condition
                if self.alive is False:
                    return True

            # exit loop
            if one_time is True:
                return True

        return True
