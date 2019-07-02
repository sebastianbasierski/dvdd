import os
import time
import subprocess
from libs.sender import *
from libs.parse_config import *
from libs.parse_interval import *

class Sensor:
    def __init__(self, sensor):
        self.sensor = sensor
        self.alive = True

    def hs_stop(self):
        self.alive = False

    def handle_sensor(self, one_time = None):
        one_time = one_time or False
        idx = get_sensor_idx(self.sensor)
        stype = get_sensor_type(self.sensor)
        interval = get_sensors_parse_interval(get_sensor_interval(self.sensor))

        ip = '172.16.2.40'
        port = '8080'
        sender = Sender(ip, port)
        sender.setup(idx)

        if int(interval) == None:
            return False

        script_dir = '/domoticz/'

        while self.alive:
            # send data
            sender.send()

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

