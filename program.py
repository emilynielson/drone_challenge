from drone import Drone
from order import Order

import sys
import os
from datetime import datetime
import ipdb

from process import *

filePath = sys.argv[1]
    
#Run the program
def run_program(filePath):
    droneStart = '06:00:00'
    droneEnd = '22:00:00'
    timeFormat = '%H:%M:%S'
    droneStartDatetime = datetime.strptime(droneStart, timeFormat)
    droneEndDatetime = datetime.strptime(droneEnd, timeFormat)
    content = importFile(filePath)
    orders = createOrders(content)
    drones = createDrones(orders)
    lines = runDeliveries(drones, droneStartDatetime)
    nps = getNPS(drones)
    exportFile(lines, nps)


run_program(filePath)
