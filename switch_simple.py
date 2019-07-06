import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    time.sleep(1)
    if(GPIO.input(22) == 1):
        print('Button 1 pressed')
    else:
        print('Button 1 released')
