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
        i = 1
        for x in locationSplit:
            if i == len(locationSplit):
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
            i+=1
        movementTime = int(locationNumbers[0]) + int(locationNumbers[1])
        return movementTime
    
    #calculate delivery time
    def calculateDeliveryTime(self, droneDeparture):
        deliveryTime = droneDeparture + timedelta(minutes = self.movementTime)
        return deliveryTime

    #calculate return time
    def calculateReturnTime(self):
        returnTime = self.deliveryTime + timedelta(minutes = self.movementTime)
        return returnTime

    #calculate NPS score
    def calculateNPS(self,):
        deltaTime = self.deliveryTime - self.orderTime
        hours = deltaTime.seconds//3600
        if hours == 0 or hours == 1:
            nps = 1
        elif hours == 2 or hours == 3:
            nps = 0
        else:
            nps = -1
        return nps

