from drone import Drone
from order import Order

import os
from datetime import datetime
import ipdb


def importFile(filePath):
    file = os.path.abspath(filePath)
    with open(file) as f:
        content = f.readlines()
        f.close()
    return content

def createOrders(content):
    orders =[]
    for i in content:
        line = i.strip('\n')
        items = line.split(' ')
        number = items[0]
        location = items[1]
        time = items[2]
        order = Order(number, location, time)
        orders.append(order)
    return orders

def createDrones(orders):
    drones = []
    for order in orders:
        drone = Drone(order)
        drones.append(drone)
    return drones

def runDeliveries(drones, droneStartTime):
    ipdb.set_trace()
    output = {}
    startTime = 0
    for drone in drones:
        if drone == drones[0]:
            droneDeparture = droneStartTime
        else:
            droneDeparture = startTime
        drone.deliveryTime = drone.calculateDeliveryTime(droneDeparture)
        drone.nps = drone.calculateNPS(drone.deliveryTime)


def run_program():
    droneStart = '06:00:00'
    droneEnd = '22:00:00'
    timeFormat = '%H:%M:%S'
    droneStartDatetime = datetime.strptime(droneStart, timeFormat)
    droneEndDatetime = datetime.strptime(droneEnd, timeFormat)

    content = importFile('/Users/m31277/drone/drone_challenge/input.txt')
    orders = createOrders(content)
    drones = createDrones(orders)
    runDeliveries(drones, droneStartDatetime)




run_program()
