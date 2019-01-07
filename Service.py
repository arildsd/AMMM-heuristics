class Service(object):
    def __init__(self, serviceId, passengerNumber, startTime, durationMinutes, durationKm):
        self._serviceId = serviceId
        self._busId = ''
        self._driverId = ''
        self._passengerNumber = passengerNumber
        self._startTime = startTime
        self._durationMinutes = durationMinutes
        self._durationKm = durationKm

    def assignBus(self, busId):
        self._busId.append(busId)

    def assignDriver(self, driverId):
        self._driverId.append(driverId)

    def getBusId(self):
        return (self._busId)

    def getDriverId(self):
        return (self._driverId)

    def getPassengerNumber(self):
        return(self._passengerNumber)

    def getStartTime(self):
        return (self._startTime)

    def getDurationMinutes(self):
        return (self._durationMinutes)

    def getDurationKm(self):
        return (self._durationKm)
