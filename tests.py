
import unittest
from program import *
from datetime import datetime

class ProgramTest(unittest.TestCase):

    #tests that returned list is not empty and is list
    def test_importFile(self):
        self.assertTrue(importFile('/Users/m31277/drone/drone_challenge/input.txt'))
        self.assertIsInstance(importFile('/Users/m31277/drone/drone_challenge/input.txt'), list)
    
    #tests that returned list is not empty and is list
    def test_createOrders(self):
        contents = importFile('/Users/m31277/drone/drone_challenge/input.txt')
        self.assertTrue(createOrders(contents))
        self.assertIsInstance(createOrders(contents), list)

    #tests that returned list is not empty and is list
    def test_createDrones(self):
        contents = importFile('/Users/m31277/drone/drone_challenge/input.txt')
        orders = createOrders(contents)
        self.assertTrue(createDrones(orders))
        self.assertIsInstance(createDrones(orders), list)

    #tests that returned list is not empty and is list
    def test_runDeliveries(self):
        contents = importFile('/Users/m31277/drone/drone_challenge/input.txt')
        orders = createOrders(contents)
        drones = createDrones(orders)
        timeFormat = '%H:%M:%S'
        droneStartTime = datetime.strptime('06:00:00', timeFormat)
        self.assertTrue(runDeliveries(drones,droneStartTime))
        self.assertIsInstance(runDeliveries(drones,droneStartTime),list)

    #tests that returned list is not empty
    def test_getNPS(self):
        contents = importFile('/Users/m31277/drone/drone_challenge/input.txt')
        orders = createOrders(contents)
        drones = createDrones(orders)
        self.assertIsInstance(getNPS(drones), int)

if __name__=="__main__":
    unittest.main()