import copy
import random

class BusChange():
    def __init__(self, service, new_bus):
        self.service = service
        self.new_bus = new_bus


class DriverChange():
    def __init__(self, service, driver):
        self.service = service
        self.new_driver = driver


class LocalSearch():
    def __init__(self):
        pass

    def createNeighborSolution(self, solution, bus_change=None, driver_change=None):
        solution = copy.deepcopy(solution)
        if bus_change is not None:
            solution.switch_bus(bus_change.service, bus_change.new_bus)
        if driver_change is not None:
            solution.switch_driver(driver_change.service, driver_change.new_driver)
        return solution

    def exploreNeighborhoodDriver(self, solution):
        solution = copy.deepcopy(solution)
        best_solution_cost = solution.calculateCosts()
        services = solution.services
        drivers = solution.drivers
        # Explore in a first improvement method
        random.shuffle(services)
        random.shuffle(drivers)
        for service in services:
            for driver in drivers:
                new_solution = copy.deepcopy(solution)
                new_solution.checkDriverAssignment(service, driver)
                change = DriverChange(service, driver)
                new_solution = self.createNeighborSolution(new_solution, driver_change=change)
                if new_solution.calculateCosts() < best_solution_cost:
                    new_solution.validate_service_assignment()
                    return new_solution
        # No improvement was found
        return solution

    def exploreNeighborhoodBus(self, solution):
        copy_solution = copy.deepcopy(solution)
        best_solution_cost = copy_solution.calculateCosts()
        services = copy_solution.services
        buses = copy_solution.buses
        # Explore in a first improvement method
        random.shuffle(services)
        random.shuffle(buses)
        for service in services:
            for bus in buses:
                new_solution = copy.deepcopy(copy_solution)
                new_solution.checkBusAssignment(service, bus)
                change = BusChange(service, bus)
                new_solution = self.createNeighborSolution(new_solution, bus_change=change)
                if new_solution.calculateCosts() < best_solution_cost:
                    new_solution.validate_service_assignment()
                    return new_solution
        # No improvement was found
        return solution

    def exploreNeighborhoodMixed(self, solution):
        pick = random.randint(-1, 1)
        if pick == 0:
            return self.exploreNeighborhoodDriver(solution)
        else:
            return self.exploreNeighborhoodBus(solution)







