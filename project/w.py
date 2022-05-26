import RPi.GPIO as gpio
import time,sys
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)

import time

gpio.output(11,True)
time.sleep(3)
gpio.output(11,False)

