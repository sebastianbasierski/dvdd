import os
import time
import subprocess
import w1thermsensor
from libs.sender import *
from libs.parse_config import *
from libs.parse_interval import *

class Sensor:
    def __init__(self, sensor):
        self.sensor = sensor
        self.alive = True

    def stop(self):
        self.alive = False

    def get_temperature_json(self, temp):
        return "json.htm?type=command&param=udevice&idx=" + str(self.idx) + "&nvalue=0&svalue=" + str(temp)

    def get_cpu_temperature_json(self):
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000.0
        return self.get_temperature_json(temp)

    def get_ds1820_temperature_json(self):
        ds_sensor = w1thermsensor.W1ThermSensor()
        temp = ds_sensor.get_temperature()
        return self.get_temperature_json(temp)

    def get_json(self):
        switcher = {
                "temperature": self.get_cpu_temperature_json,
                "temperature_ds1820": self.get_ds1820_temperature_json
        }

        func = switcher.get(self.stype, lambda: "Invalid sensor type")
        return func()

    def handle_sensor(self, one_time = None):
        one_time = one_time or False
        self.idx = get_sensor_idx(self.sensor)
        self.stype = get_sensor_type(self.sensor)
        interval = get_sensors_parse_interval(get_sensor_interval(self.sensor))

        ip = get_server_ip()
        port = get_server_port()
        sender = Sender(ip, port, self.idx)

        if int(interval) == None:
            return False

        script_dir = '/domoticz/'

        while self.alive:
            # send data
            print "send data"
            json = self.get_json()
            sender.send(json)

            # sleep
            for i in range(int(interval)):
                # print alive value
                print "Alive " + str(self.alive)

                # sleep for a second
                time.sleep(1)

                # check exit condition
                if self.alive == False:
                    return True

            # exit loop
            if one_time == True:
                return True

        return True

