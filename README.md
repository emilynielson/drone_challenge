# drone_challenge

Drone Delivery Challenge solution

## Getting Started

* check out the code from this repo
* set up a virtual environment (This is just one way to do it)
* ```virtualenv env```
* ```source env/bin/activate```
* pip install -r requirements.txt
* Finally, run the program: ```python program.py '/path_to_file/input.txt'```

## Assumptions
### Deliveries
* Since all deliveries originate at the warehouse, it is assumed the drone must return to the warehouse between deliveries to get the next order item.
* Since the warehouse is in the center and all deliveries originate there, it is assumed the direction of the delivery is not relevant and is only used to calculate the total gride spaces the drone has to travel.
### Time to Delivery
* The customers do not know the drones hours of operation and thus the time to delivery is calculated as time between time of order to time of delivery.

### NPS 
* All promotors are all weighted as a 1 and all detractors are weighted as a -1 (a 10 hour detractor is the same as 4 hour detractor) when generating the NPS.
* NPS is calculated as a percentage and is then converated to a score out of 100.

## Running tests

* Run unittests ```python -m unittest tests.py```
* Run coverage ```coverage run -m unittest tests.py```
* View coverage report ```coverage report```
* Generate coverage html ```coverage html -i```


