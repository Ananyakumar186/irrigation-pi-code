import spidev
import os
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
def readChannel():
  channel=0
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data

def getMoisture():
    data=readChannel()
    return data
while True:
 print(getMoisture())
 time.sleep(1)
