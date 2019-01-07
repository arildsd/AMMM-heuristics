
import argparse
import sys

from DATParser import DATParser
from ValidateConfig import ValidateConfig
from Greedy import Greedy
from GRASP import GRASP
from Problem import Problem
#from Solution import Solution


def run():
    try:
        argp = argparse.ArgumentParser(description='AMMM Lab Heuristics')
        argp.add_argument('configFile', help='configuration file path')
        args = argp.parse_args()

        print 'AMMM Lab Heuristics'
        print '-------------------'

        print 'Reading Config file %s...' % args.configFile
        config = DATParser.parse(args.configFile)
        ValidateConfig.validate(config)

        print 'Reading Input Data file %s...' % config.inputDataFile
        inputData = DATParser.parse(config.inputDataFile)
        #  ValidateInputData.validate(inputData)

        print 'Creating Problem...'
        problem = Problem(inputData)

        if problem.checkInstance():
            print 'Solving Problem...'
            solver = None
            solution = None
            if config.solver == 'Greedy':
                greedySolver = Greedy(config, problem)
                candidates = greedySolver.computeCandidates()
                busCandidates = candidates[0]
                driverCandidates = candidates[1]
                solutionBuses = greedySolver.solveBuses(busCandidates)
                solutionDrivers = greedySolver.solveDrivers(driverCandidates)
            elif config.solver == 'GRASP':
                solver = GRASP()
                solution = solver.solve(config, problem)

            solution.saveToFile(config.solutionFile)
        else:
            print 'Instance is infeasible.'
            solution = Solution.createEmptySolution(config, problem)
            solution.makeInfeasible()
            solution.saveToFile(config.solutionFile)

        return (0)
    except Exception as e:
        print
        print 'Exception:', e
        print
        return (1)


if __name__ == '__main__':
    sys.exit(run())
