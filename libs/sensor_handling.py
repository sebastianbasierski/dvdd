import os
import time
import subprocess
import w1thermsensor
import RPi.GPIO as GPIO
from libs.sender import *
from libs.parse_config import *
from libs.parse_interval import *


class Sensor:
    def __init__(self, sensor, config):
        self.sensor = sensor
        self.config = config
        self.alive = True

    def stop(self):
        self.alive = False

    def get_simple_json(self, temp):
        idx_json = "json.htm?type=command&param=udevice&idx=" + str(self.idx)
        value_json = "&nvalue=0&svalue=" + str(temp)
        return idx_json + value_json

    def get_button_json(self):
        GPIO.setmode(GPIO.BCM)
        gpio = self.config.get_gpio(self.sensor)
        if gpio is None:
            return None

        GPIO.setup(int(gpio), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        val = GPIO.input(int(gpio))
        return self.get_simple_json(str(val))

    def get_cpu_temperature_json(self):
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())
        temp /= 1000.0
        return self.get_simple_json(temp)

    def get_ds1820_temperature_json(self):
        ds_sensor = w1thermsensor.W1ThermSensor()
        temp = ds_sensor.get_temperature()
        return self.get_simple_json(temp)

    def get_json(self):
        switcher = {
                "button": self.get_button_json,
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

        script_dir = '/domoticz/'

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
