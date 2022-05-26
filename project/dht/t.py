import pigpio as pig
import DHT
import time
pi=pig.pi()
dht=DHT.sensor(pi,4)
dht._trigger()
i=0
while i<20:
 dht._trigger()
 print(dht.read())
 i=i+1
 time.sleep(2)
