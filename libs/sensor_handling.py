import os
import time
import subprocess
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
        script = get_sensor_script(self.sensor)
        interval = get_sensors_parse_interval(get_sensor_interval(self.sensor))

        if int(interval) == None:
            return False

        script_dir = '/domoticz/'

        while self.alive:
            # execute script
            print("script " + script_dir + script)
            normal = subprocess.call([script_dir + script, ""])
            print("exit code " + str(normal))

            # sleep
            for i in range(int(interval)):
                # print alive value
                print "Alive " + str(self.alive)

                # sleep for a second
                time.sleep(1)

                # check exit condition
                if self.alive == False:
                    return True

            # execute script
            print("script " + script_dir + script)
            normal = subprocess.call([script_dir + script, ""])
            print("exit code " + str(normal))

            # exit loop
            if one_time == True:
                return True

        return True

