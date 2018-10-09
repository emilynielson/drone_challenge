from drone import Drone
from order import Order

import os
from datetime import datetime
import ipdb

filePath = '/Users/m31277/drone/drone_challenge/input.txt'

#Readlines in import file and return list of lines
def importFile(filePath):
    file = os.path.abspath(filePath)
    with open(file) as f:
        content = f.readlines()
        f.close()
    return content

#Write order number with departure time and NPS score to output textfile
def exportFile(lines, nps):
    lastLine = 'NPS '+ str(nps)
    lines.append(lastLine)
    with open('output.txt', 'w') as f:
        for line in lines:
            f.write("%s\n" % line)
    f.close()
    print(os.path.dirname(os.path.abspath(f.name))+'/'+f.name)

#Create Order objects and return in a list
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

#Create Drone objects and return in a list
def createDrones(orders):
    drones = []
    for order in orders:
        drone = Drone(order)
        drones.append(drone)
    return drones

#Calculate Drone departure times, nps and return times and return list of lines for the output file
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

#Calculate NPS score from saved Drone nps attributes
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
