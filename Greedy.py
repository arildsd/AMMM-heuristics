from Solver import Solver


# Greedy class inherits from solver

class Greedy(Solver):

    def __init__(self, config, problem):
        self.services = problem.services
        self.buses = problem.buses
        self.drivers = problem.drivers
        self.maxBuses = problem.maxBuses
        self.BM = problem.BM
        self.CBM = problem.CBM
        self.CEM = problem.CEM
        self.overtime = []
        self.assignedBus = []
        self.overlapping_dict = self.computeOverlapping()

    def switch_bus(self, service, new_bus):
        bus = service.getBus()
        bus.unassignService(service)
        new_bus.appendService(service)
        service.assignBus(new_bus)


    def switch_driver(self, service, new_driver):
        driver = service.getDriver()
        driver.unassignService(service)
        new_driver.appendService(service)
        service.assignDriver(new_driver)


    def isOverlapping(self, s1, s2):
        s1_start = s1.getStartTime()
        s1_dur = s1.getDurationMinutes()
        s2_start = s2.getStartTime()
        s2_dur = s2.getDurationMinutes()
        start_overlapping = (s1_start + s1_dur < s2_start + s2_dur) and (s1_start + s1_dur > s2_start)
        end_overlapping = (s1_start > s2_start) and (s1_start < s2_start + s2_dur)
        return start_overlapping or end_overlapping

    def computeOverlapping(self):
        overlapping_dict = {}
        for s1 in self.services:
            overlapping_dict[s1] = []
            for s2 in self.services:
                if self.isOverlapping(s1, s2):
                    overlapping_dict[s1].append(s2)
        return overlapping_dict

    def computeCandidates(self):
        sortedBuses = sorted(self.buses, key=lambda buss: buss.getCapacity(), reverse=False)
        sortedServices = sorted(self.services, key=lambda serv: serv.getPassengerNumber(), reverse=False)

        # Assign buses to services
        for service in sortedServices:
            for bus in sortedBuses:
                if self.checkBusAssignment(service, bus):
                    service.assignBus(bus)
                    bus.appendService(service)
                    break

        sortedDrivers = sorted(self.drivers, key=lambda d: d.getMaximumWorkingMinutes(), reverse=True)
        sortedServices = sorted(self.services, key=lambda serv: serv.getDurationMinutes(), reverse=True)

        # Assign drivers to services
        for service in sortedServices:
            for driver in sortedDrivers:
                if self.checkDriverAssignment(service, driver):
                    service.assignDriver(driver)
                    driver.appendService(service)
                    break

        self.validate_service_assignment()

        return [self.services, self.calculateCosts()]

    def checkBusAssignment(self, service, bus):
        if service.getBus() is not None:
            return False
        if bus.getCapacity() < service.getPassengerNumber():
            return False
        busServices = bus.getServicesAssigned()
        capacityUsed = 0
        for assignedService in busServices:
            capacityUsed += assignedService.getPassengerNumber()

        if capacityUsed + service.getPassengerNumber() > bus.getCapacity():
            return False

        overlappingServices = self.overlapping_dict.get(service)
        for service in overlappingServices:
            if service.getBus() == bus:
                return False

        busesAssigned = []
        for service in self.services:
            if service.getBus != '' and (service.getBus() not in busesAssigned):
                busesAssigned.append(service.getBus())
        if len(busesAssigned) + 1 > self.maxBuses:
            return False

        return True

    def validate_service_assignment(self):
        for service in self.services:
            if service.getBus() is None:
                raise Exception("A service does not have a bus assigned after the greedy step.")
            if service.getDriver() is None:
                raise Exception("A service does not have a driver assigned after the greedy step.")

    def calculateCosts(self):
        busCost = 0.0
        driverCost = 0.0
        for driver in self.drivers:
            totalWorkedMinutes = 0.0
            for s in driver.getServicesAssigned():
                totalWorkedMinutes += s.getDurationMinutes()
                if totalWorkedMinutes > self.BM:
                    driverCost += (totalWorkedMinutes - self.BM) * self.CEM
                    driverCost += self.BM * self.CBM
                else:
                    driverCost += self.CBM * totalWorkedMinutes
        for bus in self.buses:
            for s in bus.getServicesAssigned():
                busCost += bus.getEurosPerMinute() * s.getDurationMinutes() + bus.getEurosPerKm() * s.getDurationKm()

        return busCost + driverCost


    def checkDriverAssignment(self, service, driver):
        # Check if the service already have a driver
        if service.getDriver() is not None:
            return False

        # Constraint 3
        dur_services = service.getDurationMinutes()
        for s in driver.getServicesAssigned():
            dur_services += s.getDurationMinutes()
        if dur_services > driver.getMaximumWorkingMinutes():
            return False

        overlappingServices = self.overlapping_dict.get(service)
        for service in overlappingServices:
            if service.getDriver() == driver:
                return False
        return True


    def validBusCandidate(self, service, bus):
        if service.getPassengerNumber() > bus.getCapacity():
            return False
        return True

    def validDriverCandidate(self, service, driver):
        if service.getDurationMinutes() > driver.getMaximumWorkingMinutes():
            return False
        return True

    def solveBuses(self, busCandidates):
        busSolutionSet = []


    def solveDrivers(self, driverCandidates):
        pass

