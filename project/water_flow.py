import RPi.GPIO as gpio
import time,sys
gpio.setmode(gpio.BOARD)
pinin=11
gpio.setup(pinin,gpio.IN)
rate_cnt=0
total_cnt=0
min=0
const=0.10
time_new=0.0


def setLED(channel):
  global rate_cnt
  rate_cnt=rate_cnt+1
  print("1",end='') 

gpio.add_event_detect(pinin,gpio.RISING,callback=setLED,bouncetime=20)

try:
  while True:
    pass
except  KeyboardInterrupt:
  print(rate_cnt)
gpio.cleanup()




"""while True:
  time_new=time.time()+5
  rate_cnt=0
  while time.time()<time_new:
    if gpio.input(input)!=0:
        rate_cnt +=1
        total_cnt +=1
    try:
        print(gpio.input(input),end='')
    except KeyboardInterrupt:
        gpio.cleanup()
        print('exiting')
        sys.exit()
  min+=1
  print("\n L/min : ",round(rate_cnt,4))
  print("\n Liters : ",round(total_cnt*const,4))"""
