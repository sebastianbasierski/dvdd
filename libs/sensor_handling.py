import time
from libs.parse_config import *

def handle_sensor(sensor):
    idx = get_sensor_idx(sensor)
    script = get_sensor_script(sensor)
    interval = get_sensor_interval(sensor)

    while True:
        # sleep
        time.sleep(interval)

        # execute script


        # call API

    return True

