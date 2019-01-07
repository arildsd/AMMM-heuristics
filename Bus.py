class Bus(object):
    def __init__(self, busId, capacity, eurosPerMinute, eurosPerKm):
        self._busId = busId
        self._capacity = capacity
        self._eurosPerMinute = eurosPerMinute
        self._eurosPerKm = eurosPerKm
        self._servicesAssigned = []

    def getId(self):
        return (self._busId)

    def getCapacity(self):
        return (self._capacity)

    def getEurosPerMinute(self):
        return (self._eurosPerMinute)

    def getEurosPerKm(self):
        return (self._eurosPerKm)

    def appendService(self, service):
        self._servicesAssigned.append(service)

    def getServicesAssigned(self):
        return self._servicesAssigned

    def unassignService(self, service):
        self._servicesAssigned.remove(service)