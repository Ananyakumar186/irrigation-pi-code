import pyrebase

class firebase:
  config = {     
  "apiKey": "AIzaSyDswl2wg0BBwZ93sVwDDd2rOuUeU29qdqM",
  "authDomain": "irrigation-a93de.firebaseapp.com",
  "databaseURL": "https://irrigation-a93de-default-rtdb.firebaseio.com/",
  "storageBucket": "irrigation-a93de.appspot.com"}

  def __init__(self):
    firebase = pyrebase.initialize_app(self.config)
    self.db= firebase.database()

  def getTrigger(self):
    trig =self.db.child("flags").child('trigger').get().val()
    return trig

  def getVavle(self):
    valve =self.db.child("flags").child('valve').get().val()
    return valve

  def setTrigger(self):
    trig =self.db.child("flags").child('trigger')
    trig.set(0)
  
  def setValve(self):
    v=self.db.child("flags").child('valve')
    v.set(0)

  def getWaterInput(self):  
    water =self.db.child("general").child('water_required').get().val()
    return water

  def setSensorValue(self,val):
    v=self.db.child("flags").child('sensor_value')
    v.set(val)

  def setRunning(self,val):
    r=self.db.child("flags").child('running')
    r.set(val)
  
  def getRunning(self):
    r =self.db.child("flags").child('running').get().val()
    return r
  
  def setLasercut(self,val):
    r=self.db.child("flags").child('lasercut')
    r.set(val)
  
  def getLaserStatus(self):
    s=self.db.child("flags").child('laserStatus').get().val()
    return s

  def setforceStop(self,val):
    r=self.db.child("flags").child('force_stop')
    r.set(val)
  
  def getForceStop(self):
    s=self.db.child("flags").child('force_stop').get().val()
    return s
  
  def getCrop(self):
    crop=self.db.child("general").child('crop').get().val()
    return str(crop)

  def getCropAge(self):
    cropage=self.db.child("general").child('cropage').get().val()
    return int(cropage)
  
  def getCropCount(self):
    cropcnt=self.db.child("general").child('cropcount').get().val()
    return int(cropcnt)

  def getSoiltexture(self):
    st=self.db.child("general").child('soil texture').get().val()
    return str(st)

 
      
  def writeSensorValues(self,l):
      print(l)
      ref=self.db.child("records")
      ref.child('recordDB').child(l[0]).set(
        {
          'temparature':l[1],
          'humidity':l[2],
          'soil moisture': l[3],
          'soil texture':l[4],
          'crop':l[5],
          'cropage':l[6],
          'cropcount':l[7],
          'water prediction':l[8]
        }
      )
      ref.child('records').child('current').set(
        {
          'temparature':l[1],
          'humidity':l[2],
          'soil moisture': l[3],
          'soil texture':l[4],
          'crop':l[5],
          'cropage':l[6],
          'cropcount':l[7],
          'water prediction':l[8]
        }
      )

  def writeLaserLog(self,time):
      ref=self.db.child("laserLog")
      ref.child('log').child(time).set(1)
      ref.child('laserLog').child('current').set(time)
