class Car:
    def __init__(self, mileage):
        self._mileage = mileage

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage):
        if new_mileage > 0 and isinstance(new_mileage, int):
            self._mileage = new_mileage
        else:
            print("Please enter a valid number")

    @mileage.deleter
    def mileage(self):
        del self._mileage


car = Car(5000)
print(car.mileage)
car.mileage = 6000
print(car.mileage)
del car.mileage
print(car.mileage)