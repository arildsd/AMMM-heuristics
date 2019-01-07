import copy
import random

class BusChange():
    def __init__(self, service, new_bus):
        self.service = service
        self.new_bus = new_bus


class DriverChange():
    def __init__(self, service, driver):
        self.service = service
        self.new_bus = driver


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
        for service in random.shuffle(services):
            for driver in random.shuffle(drivers):
                new_solution = copy.deepcopy(solution)
                new_solution.checkDriverAssignment(service, driver)
                change = DriverChange(service, driver)
                new_solution.switch_driver(change)
                if new_solution.calculateCosts() < best_solution_cost:
                    return new_solution
        # No improvement was found
        return solution








