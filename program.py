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

def exportFile(lines, nps):
    lastLine = 'NPS '+ str(nps)
    lines.append(lastLine)
    with open('output.txt', 'w') as f:
        for line in lines:
            f.write("%s\n" % line)
    f.close()


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
    output = []
    startTime = 0
    for drone in drones:
        if drone == drones[0]:
            droneDeparture = droneStartTime
        else:
            droneDeparture = startTime
        drone.deliveryTime = drone.calculateDeliveryTime(droneDeparture)
        drone.nps = drone.calculateNPS()
        drone.returnTime = drone.calculateReturnTime()
        startTime = drone.returnTime
        formatDepartureTime = droneDeparture.strftime('%H:%M:%S')
        line = drone.orderNumber +' '+formatDepartureTime
        output.append(line)
    return output

def getNPS(drones):
    totalOrders = len(drones)
    npsScores = []
    for drone in drones:
        nps = drone.nps
        npsScores.append(nps)
    promotors = npsScores.count(1)
    detractors = npsScores.count(-1)
    score = int(((promotors/totalOrders)-(detractors/totalOrders))*100)
    return score
    

def run_program():
    droneStart = '06:00:00'
    droneEnd = '22:00:00'
    timeFormat = '%H:%M:%S'
    droneStartDatetime = datetime.strptime(droneStart, timeFormat)
    droneEndDatetime = datetime.strptime(droneEnd, timeFormat)

    content = importFile('/Users/m31277/drone/drone_challenge/input.txt')
    orders = createOrders(content)
    drones = createDrones(orders)
    lines = runDeliveries(drones, droneStartDatetime)
    nps = getNPS(drones)
    exportFile(lines, nps)


run_program()
