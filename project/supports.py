
import RPi.GPIO as gpio
import time,sys
import pigpio as pig
from dht import DHT
import spidev
import ntplib
import datetime
import pytz
import arduno

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

db=None

# Hardware classes
class PinConfig:
  solenoid=13
  waterflow=11
  dht22=0
  laser_TM=15
  laser_RM=16
  soil_moisture=0

class solenoid:
  pinout=PinConfig.solenoid
  def __init__(self):
    gpio.setup(solenoid.pinout,gpio.OUT)
  def turnOn(self):
    gpio.output(solenoid.pinout,True)
  def turnOff(self):
    gpio.output(solenoid.pinout,False)
  
class laser_RM:
  pinin=PinConfig.laser_RM
  def __init__(self):
    gpio.setup(laser_RM.pinin,gpio.IN,gpio.PUD_DOWN)
    self.status=0
  def listen(self):
    self.status=1
    gpio.add_event_detect(laser_RM.pinin,gpio.FALLING,callback=lasercut,bouncetime=20)
  def removeListen(self):
    self.status=0
    gpio.remove_event_detect(laser_RM.pinin)

class laser_TM:
  pinout=PinConfig.laser_TM
  def __init__(self):
    gpio.setup(laser_TM.pinout,gpio.OUT)
  def turnOn(self):
    gpio.output(laser_TM.pinout,True)
  def turnOff(self):
    gpio.output(laser_TM.pinout,False)
    
def lasercut(channel):
  db.writeLaserLog(getdate())
  db.setLasercut(1)
  db.setLasercut(0)


class waterflow:
  pinin=PinConfig.waterflow
  def __init__(self):
    gpio.setup(waterflow.pinin,gpio.IN)
  def listen(self):
    gpio.add_event_detect(waterflow.pinin,gpio.RISING,callback=onPulse,bouncetime=20)
  def removeListen(self):
    gpio.remove_event_detect(waterflow.pinin)

class DHT22:
  pinin=4
  #sudo pigpiod
  def read(self):
     pi=pig.pi()
     dht=DHT.sensor(pi,self.pinin)
     i=0
     l=[]
     while i<20:
       dht._trigger()
       l=dht.read()
       if l[3]>0 and l[4]>0 :
         break
       i=i+1
       time.sleep(0.5)
     temparature=l[3]
     humidity=l[4]
     return temparature,humidity


class soil_moisture():
  def __init__(self):
    self.spi = spidev.SpiDev()
    self.spi.open(0,0)
    self.spi.max_speed_hz=1000000
  def  readChannel(self):
    channel=0
    val = self.spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3) << 8) + val[2]
    return data
  def getMoisture(self):
    data=self.readChannel()
    return data

rate_cnt=0
stopval=0

def irrigate(water):
  global rate_cnt,stopval
  rate_cnt=0
  cons=420
  stopval=cons*water
  valve=solenoid()
  flowmeter=waterflow()
  gpio.remove_event_detect(PinConfig.waterflow)
  flowmeter.listen()
  valve.turnOn()
  db.setRunning(1)
  db.setValve()

  
def onPulse(channel):
  global rate_cnt,flag,stopval
  rate_cnt=rate_cnt+1
  if rate_cnt>=stopval:
    gpio.output(PinConfig.solenoid,False)
    gpio.remove_event_detect(PinConfig.waterflow)
    db.setRunning(0)
    gpio.cleanup([PinConfig.solenoid,PinConfig.waterflow])

def forceStop():
    gpio.output(PinConfig.solenoid,False)
    gpio.remove_event_detect(PinConfig.waterflow)
    db.setRunning(0)
    gpio.cleanup([PinConfig.solenoid,PinConfig.waterflow])
    db.setforceStop(0)
  

def getSensorvalues():
  '''dht=DHT22()
  soilMoisture=soil_moisture()
  temp,humid=dht.read()
  moisture=soilMoisture.getMoisture()
  list=[]
  list.append(int(temp))
  list.append(int(humid))
  list.append(int(moisture))'''
  return arduno.getval()

def getdate():  
      UTC = pytz.utc
      IST = pytz.timezone('Asia/Kolkata')
      date=datetime.datetime.now(IST)
      date_time_str = date.strftime("%d-%m-%Y %I:%M %p")
      return date_time_str

def gpioclean():
  gpio.cleanup()