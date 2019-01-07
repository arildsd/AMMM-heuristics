class Driver(object):
    def __init__(self, driverId, maximumWorkingMinutes):
        self._driverId = driverId
        self._maximumWorkingMinutes = maximumWorkingMinutes

    def getId(self):
        return (self._driverId)

    def getMaximumWorkingMinutes(self):
        return (self._maximumWorkingMinutes)
