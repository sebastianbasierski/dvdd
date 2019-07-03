#!/usr/bin/python
import sys
import urllib

class Sender():
    def __init__(self, ip, port, idx):
        self.ip = ip
        self.port = port
        self.idx = idx

    def send(self, json):

        if json == None:
            print "empty json passed"
            return False

        # parameters
        cmd = "http://172.16.2.40:8080/" + json
        verbose = 1  # set to 1 to print out information to the console

        # replace 1000.0 with 1000 to round to nearest degree   
        try:
            # use Domoticz JSON url to update
            hf = urllib.urlopen(cmd)
            if verbose > 0:
                print 'Uploaded to Pi: ' + cmd
                print 'Response: ' + hf.read()
            hf.close

            return True

        except:
            return False
