"""
Capture the abstraction in an interface, bury implementation details in derived classes
"""

from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_number_of_wheels(self):
        pass

