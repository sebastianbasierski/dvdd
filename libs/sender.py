#!/usr/bin/python
import sys
import urllib

class Sender():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.idx = 0

    def setup(self, idx):
        self.idx = idx

    def send(self):
        # parameters
        url_json = "http://172.16.2.40:8080/json.htm?type=command&param=udevice&idx="
        verbose  = 1  # set to 1 to print out information to the console 

        # read cpu temperature
        # replace 1000.0 with 1000 to round to nearest degree   
        try:
            cpuTemp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000.0

            # use Domoticz JSON url to update
            cmd = url_json + str(self.idx) + "&nvalue=0&svalue=" + str(cpuTemp)
            hf = urllib.urlopen(cmd)
            if verbose > 0:
                print 'Sensor data: temperature = {0:0.1f}C'.format(cpuTemp)
                print 'Uploaded to Pi: ' + cmd
                print 'Response: ' + hf.read()
            hf.close

            return True

        except:
            return False
