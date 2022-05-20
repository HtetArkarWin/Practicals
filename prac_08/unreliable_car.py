from prac_08.car import Car
from random import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
       super().__init__(name, fuel)
       self.reliability=reliability
       self.current_fare_distance = 0


    def drive(self, distance):
        r=random()
        if r<self.reliability:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
        else:
            distance_driven=0

        return distance_driven