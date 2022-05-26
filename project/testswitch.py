import RPi.GPIO as gpio
import time,sys
gpio.setmode(gpio.BOARD)
pinout=11
pinin=13
gpio.setup(pinout,gpio.OUT)
gpio.setup(pinin,gpio.IN,pull_up_down=gpio.PUD_DOWN)
ledflag = True


def setLED(channel):
  global ledflag
  if ledflag==True:
    gpio.output(pinout,ledflag)
    ledflag=False
  else:
    gpio.output(pinout,ledflag)
    ledflag=True

gpio.add_event_detect(pinin,gpio.RISING,callback=setLED,bouncetime=20)

time.sleep(50)
gpio.cleanup()

