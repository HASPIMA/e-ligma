from .Circle import Circle
from .Vector2 import Vector2
from math import pi, sqrt


class Ellipse(Circle):

    def __init__(self, x=0, y=0, rX=0, rY=0, center: Vector2 = None, copy: Circle = None):
        if center is None and copy is None:
            super().__init__(x, y, rX)
            self.radiusY = rY
        elif center is not None and copy is None:
            super().__init__(center.x, center.y, rX)
            self.radiusY = rY
        elif center is None and copy is not None:
            super().__init__(copy.x, copy.y, copy.radius)
            self.radiusY = copy.radius

    def __str__(self):
        return "( " + str(self.x) + ', ' + str(self.y) + ") rx= " + str(self.radius) + " ry= " + str(self.radiusY)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.radius == other.radius and self.radiusY == other.radiusY

    def set(self, x=0, y=0, rX=0, rY=0, center: Vector2 = None, copy: Circle = None):
        if center is None and copy is None:
            super().set(x, y, rX)
            self.radiusY = rY
        elif center is not None and copy is None:
            super().set(center.x, center.y, rX)
            self.radiusY = rY
        elif center is None and copy is not None:
            super().set(copy.x, copy.y, copy.radius)
            self.radiusY = copy.radius

    # setPosition() no necesita sobreescritura
    def setSize(self, radiusX, radiusY):
        self.radius = radiusX
        self.radiusY = radiusY

    def area(self):
        return pi * self.radius * self.radiusY

    def circumference(self):
        return (3 * (self.radiusY + self.radius)) - sqrt(
            ((3 * self.radius) + self.radiusY) * ((3 * self.radiusY) + self.radius))

    def contains(self, x=0.0, y=0.0, dot: Vector2 = None):
        if dot is None:
            return (((x - self.x) ** 2) / (self.radius ** 2)) + (((y - self.y) ** 2) / (self.radiusY ** 2)) <= 1
        else:
            return (((dot.x - self.x) ** 2) / (self.radius ** 2)) + (((dot.y - self.y) ** 2) / (self.radiusY ** 2)) <= 1
