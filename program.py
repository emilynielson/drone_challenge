from drone import Drone
from order import Order

import os
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


content = importFile('/Users/m31277/drone/drone_challenge/input.txt')
orders = createOrders(content)