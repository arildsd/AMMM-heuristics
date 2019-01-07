
import argparse
import sys

from DATParser import DATParser
from ValidateConfig import ValidateConfig
from Greedy import Greedy
#from GRASP import GRASP
from Problem import Problem
#from Solution import Solution
from LocalSearch import LocalSearch
import time


def run():
    argp = argparse.ArgumentParser(description='AMMM Lab Heuristics')
    argp.add_argument('configFile', help='configuration file path')
    args = argp.parse_args()
    start_time = time.time()


    print 'AMMM Lab Heuristics'
    print '-------------------'

    print 'Reading Config file %s...' % args.configFile
    config = DATParser.parse(args.configFile)

    #ValidateConfig.validate(config)

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
            print 'Greedy solving'
            greedySolver = Greedy(config, problem)
            solutionGreedy = greedySolver.computeCandidates()
            candidates = solutionGreedy[0]
            cost = solutionGreedy[1]
            for candService in candidates:
                print candService.getBus()
                print candService.getDriver()
            print cost

            # Start local search
            local_search = LocalSearch()
            solution_log = []
            solution = greedySolver
            for i in xrange(1000):
                solution_log.append(solution)
                solution = local_search.exploreNeighborhoodMixed(solution)
                print "Iteration %d with cost %f" % (i+1, solution.calculateCosts())

            print "Best solution had %f cost" % solution.calculateCosts()
            print "Time: %f" % (time.time() - start_time)

        elif config.solver == 'GRASP':
            #solver = GRASP()
            solution = solver.solve(config, problem)

        #solution.saveToFile(config.solutionFile)
    else:
        print 'Instance is infeasible.'
        #solution = Solution.createEmptySolution(config, problem)
        #solution.makeInfeasible()
        #solution.saveToFile(config.solutionFile)

    return (0)



if __name__ == '__main__':
    sys.exit(run())
