'''
AMMM Instance Generator v1.0
Config attributes validator.
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

# Validate config attributes read from a DAT file. 
class ValidateConfig(object):
    @staticmethod
    def validate(data):
        # Validate that mandatory input parameters were found
        for paramName in ['instancesDirectory', 'fileNamePrefix', 'fileNameExtension', 'numInstances',
                          'numServices', 'minNumPassengersPerService', 'maxNumPassengersPerService',
                          'earliestTimeStart', 'latestTimeStart', 'minDurationMinutes', 'maxDurationMinutes',
                          'minDurationKm', 'maxDurationKm', 'numBuses', 'minCapacityPerBus', 'maxCapacityPerBus',
                          'minEurosPerMin', 'maxEurosPerMin', 'minEurosPerKm', 'maxEurosPerKm', 'maxBuses',
                          'numDrivers', 'minHighestNumberOfMinutesPerDriver', 'maxHighestNumberOfMinutesPerDriver',
                          'CBM', 'CEM', 'BM']:
            if(not data.__dict__.has_key(paramName)):
                raise Exception('Parameter(%s) not contained in Configuration' % str(paramName))
        
        instancesDirectory = data.instancesDirectory
        if(len(instancesDirectory) == 0): raise Exception('Value for instancesDirectory is empty')

        fileNamePrefix = data.fileNamePrefix
        if(len(fileNamePrefix) == 0): raise Exception('Value for fileNamePrefix is empty')

        fileNameExtension = data.fileNameExtension
        if(len(fileNameExtension) == 0): raise Exception('Value for fileNameExtension is empty')
