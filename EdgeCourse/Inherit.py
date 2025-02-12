class Vehicle():
    
    def __init__(self, model, year, wheels):
        self.model = model
        self.year = year
        self.wheels = wheels


class Car(Vehicle):

    def __init__(self,model, year, wheel, doors):
        super().__init__(model, year, wheel)
        self.doors = doors


class Bike(Vehicle):

    def __init__(self, model, year, wheels, cornering_angle):
        super().__init__(model, year, wheels)
        self.cornering_angle = cornering_angle



vehicle = Vehicle('r15', 2001, 4)
car = Car(2)
bike = Bike(1)