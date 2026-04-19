"""
Cree una clase abstracta de Shape que:
Tenga los metodos abstractos de calculate_perimeter y calculate_area.
Ahora cree las siguientes clases que hereden de Shape e implementen esos metodos: Circle, Square y Rectangle.
Cada una de estas necesita los atributos respectivos para poder calcular el area y el perimetro.
"""

from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_perimeter(self):
        return 2 * pi * self.radius
    def calculate_area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_perimeter(self):
        return 4 * self.side
    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_perimeter(self):
        return 2 * (self.base + self.height)
    def calculate_area(self):
        return self.base * self.height
