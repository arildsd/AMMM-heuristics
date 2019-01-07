from Solver import Solver

# Greedy class inherits from solver

class Greedy(Solver):

    def __init__(self, config, problem):
        self.services = problem.services
        self.buses = problem.buses
        self.drivers = problem.drivers
        self.candidateDrivers = []
        self.candidateBuses = []

    def computeCandidates(self):
        for service in self.services:
            for bus in self.buses:
                if self.validBusCandidate(service, bus):
                    service.assignBus(bus)
                    self.candidateBuses.append(service)
            for driver in self.drivers:
                if self.validDriverCandidate(service, driver):
                    service.assignDriver(driver)
                    self.candidateDrivers.append(service)
        return [self.candidateBuses, self.candidateDrivers]


    def validBusCandidate(self, service, bus):
        if service.getPassengerNumber() > bus.getCapacity():
            return False
        return True

    def validDriverCandidate(self, service, driver):
        if service.getDurationMinutes() > driver.getMaximumWorkingMinutes()
            return False
        return True

    def solveBuses(self, busCandidates):
        busSolutionSet = []


    def solveDrivers(self, driverCandidates):


