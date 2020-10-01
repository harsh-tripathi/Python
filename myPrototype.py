
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
    
    def perimeter(self):
        return 4

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())


'''
Documentation

Abstract method: These methods are not implemented rather overwritted by child class.
We also have methods like @abstractstatic and @abstractclassmethod.


Concrete class provide an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super().
Like in above example we can also write as given below
'''
class Square(Shape):
    previous = super.perimeter(self) # This calls the perimeter function of Shape class
    
    def perimeter(self):
        print(f"ans is {previous*10}")
