'''
AMMM Lab Heuristics v1.2
Representation of a problem instance.
Copyright 2018 Luis Velasco.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from Bus import Bus
from Driver import Driver
from Service import Service


class Problem(object):
    def __init__(self, inputData):
        self.inputData = inputData

        nServices = self.inputData.nServices
        nBuses = self.inputData.nBuses
        nDrivers = self.inputData.nDrivers

        time_start = self.inputData.time_start
        duration_min = self.inputData.duration_min
        duration_km = self.inputData.duration_km
        nPassengers = self.inputData.nPassengers

        cap_b = self.inputData.cap_b
        euros_min_b = self.inputData.euros_min_b
        euros_km_b = self.inputData.euros_km_b
        max_d = self.inputData.max_d

        maxBuses = self.inputData.maxBuses
        CBM = self.inputData.CBM
        CEM = self.inputData.CEM
        BM = self.inputData.BM

        self.maxBuses = maxBuses
        self.CBM = CBM
        self.CEM = CEM
        self.BM = BM

        self.services = []

        for sId in xrange(0, nServices):  # sId = 0..(nServices-1)
            service = Service(sId, nPassengers[sId], time_start[sId], duration_min[sId], duration_km[sId])
            self.services.append(service)

        self.buses = []
        for bId in xrange(0, nBuses):  # bId = 0..(nBuses-1)
            bus = Bus(bId, cap_b[bId], euros_min_b[bId], euros_km_b[bId])
            self.buses.append(bus)

        self.drivers = []
        for dId in xrange(0, nDrivers):  # dId = 0..(nDrivers-1)
            driver = Driver(dId, max_d[dId])
            self.drivers.append(driver)

    def getServices(self):
        return self.services

    def getBuses(self):
        return self.buses

    def getDrivers(self):
        return self.drivers

    def checkInstance(self):
        maximumAmountWorkingMinutes = 0.0
        serviceMinutesDemand = 0.0
        passengerDemand = 0.0
        busesCapacity = 0.0
        maximumBusCapacity = 0.0
        minimumBusCapacity = self.buses[0].getCapacity()
        maximumPassengerDemand = 0.0
        minimumPassengerDemand = self.services[0].getPassengerNumber()

        for bus in self.buses:
            busCapacity = bus.getCapacity()
            if busCapacity > maximumBusCapacity:
                maximumBusCapacity = busCapacity
            if busCapacity < minimumBusCapacity:
                minimumBusCapacity = busCapacity
            busesCapacity += busCapacity

        for service in self.services:
            serviceDemand = service.getDurationMinutes()
            serviceMinutesDemand += serviceDemand
            passengers = service.getPassengerNumber()
            if passengers > maximumPassengerDemand:
                maximumPassengerDemand = passengers
            if passengers < minimumPassengerDemand:
                minimumPassengerDemand = passengers
            if passengers > busesCapacity:  # If there are more passengers in a single
                                            # service than there is total bus capacity, it is infeasible
                return False
            passengerDemand += passengers

        if minimumPassengerDemand > maximumBusCapacity:  # None of the service demands can be met
            return False

        for driver in self.drivers:
            maxWorkingMinutes = driver.getMaximumWorkingMinutes()
            maximumAmountWorkingMinutes += maxWorkingMinutes

        return True
