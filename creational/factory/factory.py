from car import Car
from van import Van
from jeep import Jeep
from enum import Enum


class VehicleType(Enum):
    car = "car"
    van = "van"
    jeep = "jeep"


class VehicleFactory:
    def __init__(self):
        self.car = Car
        self.van = Van
        self.jeep = Jeep

    def make_vehicle(self, vehicle_type, make, year, model):
        if vehicle_type == VehicleType.car:
            return Car(make, year, model)
        elif vehicle_type == "van":
            return Van(make, year, model)
        elif vehicle_type == "jeep":
            return Jeep(make, year, model)
        return None


factory = VehicleFactory()
car = factory.make_vehicle(VehicleType.car, "mazda", 2000, "rx8")

car.drive()

van = factory.make_vehicle("van", "merc", 2010, "c100")

van.drive()