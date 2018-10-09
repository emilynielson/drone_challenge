from datetime import datetime
from datetime import timedelta

import ipdb
class Drone(object):
    
    # Initializer / Instance Attributes
    def __init__(self, order):
        self.orderNumber = order.number
        self.orderTime = order.time
        self.movementTime = self.calculateMovementTime(order.location)
        self.deliveryTime = 0
        self.returnTime = 0
        self.nps = 0

    #calculate movement time in minutes
    def calculateMovementTime(self,location):
        locationSplit = list(location)
        locationSplit.pop(0)
        locationNumbers =[]
        newNumber = []
        for x in locationSplit:
            if x == locationSplit[-1]:
                int(x)
                newNumber.append(x)
                number = int(''.join(newNumber))
                locationNumbers.append(number)
                newNumber = []
            else:
                try:
                    int(x)
                    newNumber.append(x)
                except:
                    number = int(''.join(newNumber))
                    locationNumbers.append(number)
                    newNumber = []
        movementTime = int(locationNumbers[0]) + int(locationNumbers[1])
        return movementTime
    
    #calculate delivery time
    def calculateDeliveryTime(self, droneDeparture):
        ipdb.set_trace()
        deliveryTime = droneDeparture + timedelta(minutes = self.movementTime)
        return deliveryTime

    #calculate return time
    def calculateReturnTime():
        pass

    #calculate NPS score
    def calculateNPS(self):
        deltaTime = self.deiveryTime - self.orderTime
