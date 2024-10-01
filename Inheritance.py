class Vehicle():
    def general_usage(self):
        print("Used for transportation")


class Car(Vehicle):
    def __init__(self):
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        self.general_usage()
        print(self.wheels, "wheeled car is used to commute")


class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels=2
        self.has_roof=False

    def specific_usage(self):
        self.general_usage()
        print(self.wheels, "wheeled car is used for racing")

c=Car()
c.specific_usage()
m=Motorcycle()
m.specific_usage()



