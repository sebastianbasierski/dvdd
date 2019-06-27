import os
import time
import subprocess
from libs.parse_config import *
from libs.parse_interval import *

def handle_sensor(sensor, one_time = None):
    one_time = one_time or False
    idx = get_sensor_idx(sensor)
    script = get_sensor_script(sensor)
    interval = get_sensors_parse_interval(get_sensor_interval(sensor))
    if int(interval) == None:
        return False

    script_dir = '/domoticz/'

    while True:
        # sleep
        time.sleep(int(interval))

        # execute script
        print("script " + script_dir + script)
        normal = subprocess.call([script_dir + script, ""])
        print("exit code " + str(normal))

        # call API

        # exit loop
        if one_time == True:
            return True

    return True

