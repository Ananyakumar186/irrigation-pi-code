
from firebase import firebase
from supports import DHT22,solenoid,laser_RM,laser_TM
import supports
import time
from ml import loadModel
db=firebase()
f=True
lr=laser_RM()
lr.listen()
lt=laser_TM()
lt.turnOn()
supports.db=db
print('server started')

while True:
    if db.getTrigger()==1:
        
        l=supports.getSensorvalues()
        l.insert(0,supports.getdate())
        l.append(db.getSoiltexture())
        l.append(db.getCrop())
        l.append(db.getCropAge())
        l.append(db.getCropCount())
        p=loadModel.predict(l)
        l.append(p)
        db.writeSensorValues(l)
        db.setSensorValue(1)
        db.setSensorValue(0)
        db.setTrigger()
    
    
    if db.getVavle()==1 and db.getRunning()==0:
        wq=db.getWaterInput()
        if wq>0:
            supports.irrigate(wq)
            print('solenoid triggered')
        else:
            db.setValve()
    else:
        db.setValve()

    ls=db.getLaserStatus()
    if ls==0 and lr.status==1:
        lr.removeListen()
        lt.turnOff()
    elif ls==1 and lr.status==0:
        lt.turnOn()
        lr.listen()

    if db.getForceStop()==1 and db.getRunning()==1:
        supports.forceStop()
    else:
        db.setforceStop(0)

    time.sleep(1)

#print(db.getWaterInput())

