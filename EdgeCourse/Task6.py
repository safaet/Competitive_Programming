class Bird:

    pass


class FlyingBird(Bird):

    def fly(self):
        print("Flying....")


class Sparrow(FlyingBird):
    pass # Sparrow can fly


class Penguin(Bird):
    
    def fly(self):
        raise Exception("Penguins can't fly!")  #Violates LSP