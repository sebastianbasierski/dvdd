#!/usr/bin/python
import sys
import urllib

# parameters
sensor_idx  = 6
url_json = "http://172.16.2.40:8080/json.htm?type=command&param=udevice&idx="
verbose  = 1  # set to 1 to print out information to the console 

# read cpu temperature
# replace 1000.0 with 1000 to round to nearest degree
value = 1

# use Domoticz JSON url to updatea
cmd = url_json  + str(sensor_idx) + "&nvalue=0&svalue=" + str(value)
hf = urllib.urlopen(cmd)
if verbose > 0:
      print 'Sensor data: state = ' + str(value)
      print 'Uploaded to Pi: ' + cmd
      print 'Response: ' + hf.read()
hf.close
