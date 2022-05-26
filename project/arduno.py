import serial


def getval():
  ser=serial.Serial("/dev/ttyUSB0",9600)
  b=ser.readline()
  o = b.decode('UTF-8')
  l=o.split()
  m=int(l[0])
  t=l[1]
  h=l[2]
  if t=='nan' and h=='nan':
    t=0
    h=0
  else:
    t=int(float(l[1]))
    h=int(float(l[2]))
  if m<0:
    m=0
  return [t,h,m]