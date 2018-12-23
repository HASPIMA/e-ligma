from math import *
from .Vector2 import Vector2


class Circle:
    def __init__(self, x=0.0, y=0.0, radius=0.0, center: Vector2 = None, edge: Vector2 = None):
        if center is None and edge is None:
            self.x = x
            self.y = y
            self.radius = radius
        elif center is not None and edge is None:
            self.x = center.x
            self.y = center.y
            self.radius = radius
        elif center is None and edge is not None:
            self.x = x
            self.y = y
            self.radius = edge.len()
        elif center is not None and edge is not None:
            self.x = center.x
            self.y = center.y
            self.radius = edge.len()

    def __str__(self):
        return "( " + str(self.x) + ', ' + str(self.y) + ") r= " + str(self.radius)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def set(self, x=0.0, y=0.0, radius=0.0, center: Vector2 = None, edge: Vector2 = None):
        if center is None and edge is None:
            self.x = x
            self.y = y
            self.radius = radius
        elif center is not None and edge is None:
            self.x = center.x
            self.y = center.y
            self.radius = radius
        elif center is None and edge is not None:
            self.x = x
            self.y = y
            self.radius = edge.len()
        elif center is not None and edge is not None:
            self.x = center.x
            self.y = center.y
            self.radius = edge.len()

    def setPosition(self, x=0.0, y=0.0, center: Vector2 = None):
        if center is None:
            self.x = x
            self.y = y
        else:
            self.x = center.x
            self.y = center.y

    def setRadius(self, radius):
        self.radius = radius

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def area(self):
        return pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.radius * pi

    def __contains__(self, other):
        return self.contains(other.x + other.radius, other.y) and self.contains(other.x - other.radius,
                                                                                other.y) and self.contains(other.x,
                                                                                                           other.y + other.radius) and self.contains(
            other.x, other.y - other.radius)

    def contains(self, x=0.0, y=0.0, dot: Vector2 = None):
        if dot is None:
            return ((x - self.x) ** 2) + ((y - self.y) ** 2) <= self.radius ** 2
        else:
            return ((dot.x - self.x) ** 2) + ((dot.y - self.y) ** 2) <= self.radius ** 2

    def overlaps(self, other):
        return self.contains(other.x + other.radius, other.y) or self.contains(other.x - other.radius,
                                                                               other.y) or self.contains(other.x,
                                                                                                         other.y + other.radius) or self.contains(
            other.x, other.y - other.radius)
