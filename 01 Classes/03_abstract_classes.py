from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(2, 3)]
    for s in shapes:
        print(f"{s.__class__.__name__} area: {s.area()}")
