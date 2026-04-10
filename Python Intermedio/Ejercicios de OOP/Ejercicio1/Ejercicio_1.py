from math import pi
class Circle:
    def __init__(self, _radius):
        self.radius = _radius
    def get_area(self):
        return pi * self.radius ** 2