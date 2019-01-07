'''
AMMM Instance Generator v1.0
Instance Generator class.
Copyright 2016 Luis Velasco and Lluis Gifre.

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

import os, random

# Generate instances based on read configuration. 
class InstanceGenerator(object):
    def __init__(self, config):
        self.config = config
    
    def generate(self):
        instancesDirectory = self.config.instancesDirectory
        fileNamePrefix = self.config.fileNamePrefix
        fileNameExtension = self.config.fileNameExtension
        numInstances = self.config.numInstances
        
        numServices = self.config.numServices
        minNumPassengersPerService = self.config.minNumPassengersPerService
        maxNumPassengersPerService = self.config.maxNumPassengersPerService
        earliestTimeStart = self.config.earliestTimeStart
        latestTimeStart = self.config.latestTimeStart
        minDurationMinutes = self.config.minDurationMinutes
        maxDurationMinutes = self.config.maxDurationMinutes
        minDurationKm = self.config.minDurationKm
        maxDurationKm = self.config.maxDurationKm

        numBuses = self.config.numBuses
        minCapacityPerBus = self.config.minCapacityPerBus
        maxCapacityPerBus = self.config.maxCapacityPerBus
        minEurosPerMin = self.config.minEurosPerMin
        maxEurosPerMin = self.config.maxEurosPerMin
        minEurosPerMin = self.config.minEurosPerMin
        minEurosPerKm = self.config.minEurosPerKm
        maxEurosPerKm = self.config.maxEurosPerKm
        maxBuses = self.config.maxBuses

        numDrivers = self.config.numDrivers
        minHighestNumberOfMinutesPerDriver = self.config.minHighestNumberOfMinutesPerDriver
        maxHighestNumberOfMinutesPerDriver = self.config.maxHighestNumberOfMinutesPerDriver
        CBM = self.config.CBM
        CEM = self.config.CEM
        BM = self.config.BM

        if(not os.path.isdir(instancesDirectory)):
            raise Exception('Directory(%s) does not exist' % instancesDirectory)

        for i in xrange(0, numInstances):
            instancePath = os.path.join(instancesDirectory, '%s_%d.%s' % (fileNamePrefix, i, fileNameExtension))
            fInstance = open(instancePath, 'w')


            time_start = []
            duration_min = []
            duration_km = []
            nPassengers = []

            for s in xrange(0, numServices):
                passengerNumber = random.randint(minNumPassengersPerService, maxNumPassengersPerService)
                nPassengers.append(passengerNumber)
                startTime = random.uniform(earliestTimeStart, latestTimeStart)
                time_start.append(startTime)
                durationInMinutes = random.uniform(minDurationMinutes, maxDurationMinutes)
                duration_min.append(durationInMinutes)
                durationInKm = random.uniform(minDurationKm, maxDurationKm)
                duration_km.append(durationInKm)

            
            numThreads = 0
            firstThreadIdPerTask = []
            numThreadsPerTask = []
            resourcesPerThread = []
            cap_b = []
            euros_min_b = []
            euros_km_b = []

            for b in xrange(0, numBuses):
                busCapacity = random.randint(minCapacityPerBus, maxCapacityPerBus)
                cap_b.append(busCapacity)
                eurosPerMin = random.uniform(minEurosPerMin, maxEurosPerMin)
                eurosPerKm = random.uniform(minEurosPerKm, maxEurosPerKm)
                euros_min_b.append(eurosPerMin)
                euros_km_b.append(eurosPerKm)

            max_d = []

            for d in xrange(0, numDrivers):
                maximumMinutesDriver = random.randint(minHighestNumberOfMinutesPerDriver,
                                                      maxHighestNumberOfMinutesPerDriver)
                max_d.append(maximumMinutesDriver)


            
            fInstance.write('nServices=%d;\n' % numServices)
            fInstance.write('nBuses=%d;\n' % numBuses)
            fInstance.write('nDrivers=%d;\n' % numDrivers)

            # translate vector of floats into vector of strings and concatenate that strings separating them by a single space character
            fInstance.write('time_start=[%s];\n' % (' '.join(map(str, time_start))))
            fInstance.write('duration_min=[%s];\n' % (' '.join(map(str, duration_min))))
            fInstance.write('duration_km=[%s];\n' % (' '.join(map(str, duration_km))))
            fInstance.write('nPassengers=[%s];\n' % (' '.join(map(str, nPassengers))))

            fInstance.write('cap_b=[%s];\n' % (' '.join(map(str, cap_b))))
            fInstance.write('euros_min_b=[%s];\n' % (' '.join(map(str, euros_min_b))))
            fInstance.write('euros_km_b=[%s];\n' % (' '.join(map(str, euros_km_b))))
            fInstance.write('maxBuses=%d;\n' % maxBuses)

            fInstance.write('max_d=[%s];\n' % (' '.join(map(str, max_d))))

            fInstance.write('CBM=%d;\n' % CBM)
            fInstance.write('CEM=%d;\n' % CEM)
            fInstance.write('BM=%d;\n' % BM)

            fInstance.close()
