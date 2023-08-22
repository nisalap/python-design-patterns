class Car:
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model

    def drive(self):
        print("I am driving a {} {} {} Car".format(self.make, self.model, self.year))