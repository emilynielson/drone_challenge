from datetime import datetime

import ipdb

class Order(object):

    # Initializer / Instance Attributes
    def __init__(self, number, location, time):
        self.number = number
        self.location = location
        self.time = self.datetimeTime(time)

    #convert string time to datetime
    def datetimeTime(self, time):
        timeFormat = '%H:%M:%S'
        newTime = datetime.strptime(time, timeFormat)
        return newTime

    

