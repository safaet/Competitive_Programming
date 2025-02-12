class Drivable:

    def drive(self):
        pass

class Flyable:
    def fly(self):
        pass

class Car(Drivable):
    def drive(self):
        print("Driving on the road.")

class Airplane(Flyable):
    def fly(self):
        print("Flying in the sky.")