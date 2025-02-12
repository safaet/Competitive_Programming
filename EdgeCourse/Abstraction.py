from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    pass
    
    # def area(self):
    #     return "Calculating circle area"
    
# class Rectangle(Shape):

#     def area(self):
#         return "Calcuating rectangle area"
    

circle = Circle()
# rectangle = Rectangle()


print(circle.area())
# print(rectangle.area())