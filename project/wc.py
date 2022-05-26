import RPi.GPIO as gpio
import time,sys
gpio.setmode(gpio.BOARD)
waterflow=11
solenoid=13
gpio.setup(solenoid,gpio.OUT)
gpio.setup(waterflow,gpio.IN)
rate_cnt=0
flag=True

def setLED(channel):
  global rate_cnt,flag
  rate_cnt=rate_cnt+1
  if rate_cnt>=420:
    flag=False
    gpio.output(solenoid,False)

gpio.add_event_detect(waterflow,gpio.RISING,callback=setLED,bouncetime=20)

try:
  gpio.output(solenoid,True)
  while flag :
        pass

  print(rate_cnt)
except KeyboardInterrupt:
  gpio.cleanup()

gpio.cleanup()
