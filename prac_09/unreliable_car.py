"""
CP1404/CP5632 Practical
Unreliable Car class
"""

from car import Car
import random


class UnreliableCar(Car):
    """Unreliable Car class"""

    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def is_able_to_drive(self):
        """Is able to drive if reliability < random number"""
        return self.reliability < random.randint(0, 100)

    def drive(self, distance):
        """Drives given distance if able to drive, return 0 if not"""
        if self.is_able_to_drive():
            return super().drive(distance)
        else:
            return 0
