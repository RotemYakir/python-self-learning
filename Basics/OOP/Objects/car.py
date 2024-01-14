class Car:
    make = None
    model = None
    year = None
    color = None

    def __init__(self, make, model, year, color):  # constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} stopped")
