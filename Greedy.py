from Solver import Solver
import numpy as np


# Greedy class inherits from solver

class Greedy(Solver):

    def __init__(self, config, problem):
        self.services = problem.services
        self.buses = problem.buses
        self.drivers = problem.drivers
        self.overtime = []
        self.assignedBus = []
        self.overlapping_dict = self.computeOverlapping()

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
        sortedBuses = sorted(self.buses, key=lambda buss: buss.getEurosPerKm() + buss.getEurosPerMinute(), reverse=True)
        sortedServices = sorted(self.services, key=lambda serv: serv.getPassengerNumber(), reverse=True)

        # Assign buses to services
        for service in sortedServices:
            for bus in sortedBuses:
                if self.checkAssignment(service, bus):
                    service.assignBus(bus)
                    bus.appendService(service)
                    break

        sortedDrivers = sorted(self.buses, key=lambda d: d.getMaximumWorkingMinutes(), reverse=True)
        sortedServices = sorted(self.services, key=lambda serv: serv.getDurationMinutes(), reverse=True)

        # Assign drivers to services
        for service in sortedServices:
            for driver in sortedBuses:
                if self.checkDriverAssignment(service, driver):
                    service.assignDriver(driver.getId())
                    driver.appendService(service)
                    break

    def checkBusAssignment(self, service, bus):
        if service.getBusId() != '':
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
            if service.getBusId() == bus.getId():
                return False

        return True


    def checkDriverAssignment(self, service, driver):
        # Check if the service already have a driver
        if service.getDriverId() != '':
            return False

        # Constraint 3
        dur_services = service.getDurationMinutes()
        for s in driver.getServicesAssigned():
            dur_services += s.getDurationMinutes()
        if dur_services > driver.getMaximumWorkingMinutes():
            return False

        overlappingServices = self.overlapping_dict.get(service)
        for service in overlappingServices:
            if service.getDriverId() == driver.getId():
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

