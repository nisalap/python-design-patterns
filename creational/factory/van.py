class Van:
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model

    def drive(self):
        print("I am driving a {} {} {} Van".format(self.make, self.model, self.year))