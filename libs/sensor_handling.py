import os
import time
import subprocess
from libs.parse_config import *
from libs.parse_interval import *

alive = True

def hs_stop():
    global alive

    alive = False

def handle_sensor(sensor, one_time = None):
    global alive

    one_time = one_time or False
    idx = get_sensor_idx(sensor)
    script = get_sensor_script(sensor)
    interval = get_sensors_parse_interval(get_sensor_interval(sensor))
    if int(interval) == None:
        return False

    script_dir = '/domoticz/'

    while alive:
        # execute script
        print("script " + script_dir + script)
        normal = subprocess.call([script_dir + script, ""])
        print("exit code " + str(normal))

        # sleep
        for i in range(int(interval)):
            # print alive value
            print "Alive " + str(alive)

            # sleep for a second
            time.sleep(1)

            # check exit condition
            if alive == False:
                return True

        # execute script
        print("script " + script_dir + script)
        normal = subprocess.call([script_dir + script, ""])
        print("exit code " + str(normal))

        # exit loop
        if one_time == True:
            return True

    return True

