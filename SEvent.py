import time

class SEvent:
  def __init__(self, startTime, endTime, host, name, eventdb, auxillaryMembers=[], joinedMembers=[], description="", setid=-1):
    if(setid == -1):
      self._id = time.time()
    else:
      self._id = setid
    self.startTime = startTime
    self.endTime = endTime
    self.host = host
    self.name = name
    self.auxillaryMembers = auxillaryMembers
    self.joinedMembers = joinedMembers
    self.description = description
    self.eventdb = eventdb
  
  def updateDBEntry(self):
    newDict = {
      "_id": self._id,
      "startTime": self.startTime,
      "endTime": self.endTime,
      "host": self.host,
      "name": self.name,
      "auxillaryMembers": self.auxillaryMembers,
      "joinedMembers": self.joinedMembers,
      "description": self.description
    }
    self.eventdb[self._id] = newDict

  @classmethod
  def getEventFromDBById(cls, db, eventId):
    pulledDb = db[eventId]
    return cls(pulledDb["startTime"], pulledDb["endTime"], pulledDb["host"], pulledDb["name"], db, pulledDb["auxillaryMembers"], pulledDb["joinedMembers"], pulledDb["description"], setid=pulledDb["_id"])

  @classmethod
  def getEventFromDBByName(cls, db, eventName):
    for entry in db.items():
      val = entry[1]
      if(val["name"] == eventName):
        return cls(val["startTime"], val["endTime"], val["host"], val["name"], db, val["auxillaryMembers"], val["joinedMembers"], val["description"], setid=pulledDb["_id"])