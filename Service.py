class Service(object):
    def __init__(self, serviceId, passengerNumber, startTime, durationMinutes, durationKm):
        self._serviceId = serviceId
        self._bus = None
        self._driver = None
        self._passengerNumber = passengerNumber
        self._startTime = startTime
        self._durationMinutes = durationMinutes
        self._durationKm = durationKm

    def assignBus(self, bus):
        self._bus = bus

    def assignDriver(self, driver):
        self._driver = driver

    def getBus(self):
        return (self._bus)

    def getDriver(self):
        return self._driver

    def getPassengerNumber(self):
        return(self._passengerNumber)

    def getStartTime(self):
        return (self._startTime)

    def getDurationMinutes(self):
        return (self._durationMinutes)

    def getDurationKm(self):
        return (self._durationKm)
