#!/usr/bin/python
import sys
import urllib


class Sender():
    def __init__(self, ip, port, idx):
        self.ip = ip
        self.port = port
        self.idx = idx

    def send(self, msg):
        if msg is None:
            return -1

        # parameters
        cmd = "http://" + str(self.ip) + ":" + str(self.port) + "/" + msg
        verbose = 1  # set to 1 to print out information to the console

        # replace 1000.0 with 1000 to round to nearest degree
        try:
            # use Domoticz JSON url to update
            hf = urllib.urlopen(cmd)
            if verbose > 0:
                print 'Uploaded to Pi: ' + cmd
                print 'Response: ' + hf.read()
            hf.close

            return 0

        except:
            return -2
