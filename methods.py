class Car:
    number_of_wheels: int = 4

    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model
        print("car object init")

    def __new__(cls, *args, **kwargs):
        print("new car object created")
        return super().__new__(cls)

    def __del__(self):
        print("object deleted")

    def __repr__(self):
        return "Class for car"

    @classmethod
    def get_number_of_wheels(cls):
        return Car.number_of_wheels

    @staticmethod
    def get_vehicle_type():
        return Car.__name__

    def get_car_make(self):
        return self.make


# Static methods, doesnt need to create an object -> Car instead of Car()
print(Car.get_vehicle_type())


# Class methods, still not need to instantiate
print(Car.get_number_of_wheels())

car = Car("Toyota", 2000, "Corolla")
print(car)
print(hex(id(car)))

# Object or usual methods
print(car.get_car_make())
