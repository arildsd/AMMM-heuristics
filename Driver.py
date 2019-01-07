class Driver(object):
    def __init__(self, driverId, maximumWorkingMinutes):
        self._driverId = driverId
        self._maximumWorkingMinutes = maximumWorkingMinutes
        self._servicesAssigned = []

    def getId(self):
        return (self._driverId)

    def getMaximumWorkingMinutes(self):
        return (self._maximumWorkingMinutes)

    def getServicesAssigned(self):
        return self._servicesAssigned

    def appendService(self, service):
        self._servicesAssigned.append(service)