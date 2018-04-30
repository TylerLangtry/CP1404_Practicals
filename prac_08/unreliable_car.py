from prac_07.car import Car
from random import randint

class UnreliableCar(Car):

    def __init__(self,name,fuel,reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability > randint(0,100):
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
