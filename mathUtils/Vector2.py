from math import *
from random import *


class Vector2:
    def __init__(self, x=0, y=0, copy=None, xy: tuple = None):

        if copy is not None:
            if type(copy).__name__ == 'Vector2':
                self.x = copy.x
                self.y = copy.y
            else:
                raise TypeError('Must be a Vector2 object')

        elif xy is not None and len(xy) == 2:
            self.x, self.y = xy
        else:
            self.x, self.y = (x, y)

    def __iadd__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "(" + str(self.x) + ', ' + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def len(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def isUnit(self):
        return self.len() == 1

    def isZero(self):
        return self.len() == 0

    def set(self, x, y):
        self.x = x
        self.y = y

    def setZero(self):
        self.x = 0
        self.y = 0

    def angle(self, rads):
        if self.isZero():
            return 0
        result = 0.0
        if self.x > 0:
            if rads:
                result = atan(self.y / self.x)
            else:
                result = degrees(atan(self.y / self.x))
        elif self.x == 0 and self.y > 0:
            if rads:
                result = pi / 2
            else:
                result = 90
        elif self.x == 0 and self.y < 0:
            if rads:
                result = pi * 3 / 2
            else:
                result = 270
        else:
            if rads:
                result = atan(self.y / self.x) + pi
            else:
                result = degrees(atan(self.y / self.x)) + 180
        if result < 0:
            result += 360
        return result

    def angleRespect(self, other, rads):
        if self.angle(rads) >= other.angle(rads):
            return self.angle(rads) - other.angle(rads)
        else:
            return -self.angle(rads) + other.angle(rads)

    def limit(self, min, max):
        if min.x <= self.x <= max.x and min.y <= self.y <= max.y:
            return self
        elif self.x < min.x and self.x <= max.x and min.y <= self.y <= max.y:
            return Vector2(min.x, self.y)
        elif self.x >= min.x and self.x > max.x and min.y <= self.y <= max.y:
            return Vector2(max.x, self.y)
        elif self.x >= min.x and self.x > max.x and self.y < min.y and self.y <= max.y:
            return Vector2(max.x, min.y)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and self.y > max.y:
            return Vector2(max.x, max.y)
        elif self.x < min.x and self.x <= max.x and self.y < min.y and self.y <= max.y:
            return Vector2(min.x, min.y)
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and self.y > max.y:
            return Vector2(min.x, max.y)
        elif min.x <= self.x <= max.x and self.y < min.y and self.y <= max.y:
            return Vector2(self.x, min.y)
        else:
            return Vector2(self.x, max.y)

    def clamp(self, min, max):
        current = self.len()
        if current < min and current <= max:
            self.setLenght(min)
        elif current >= min and current > max:
            self.setLenght(max)

    def dst2(self, x, y):
        return ((self.x - x) ** 2) + ((self.y - y) ** 2)

    def dst(self, x, y):
        return sqrt(self.dst2(x, y))

    def isOpposing(self, other):
        return self.angle(True) == -other.angle(True)

    def isSameDirection(self, other):
        return self.angle(True) == other.angle(True)

    def isCollinear(self, other):
        return self.isOpposing(other) or self.isSameDirection(other)

    def isOrthogonal(self, other):
        return self.dot(other) == 0

    def normalize(self):
        if self.isZero():
            return
        norm = self.len()
        self.x = self.x / norm
        self.y = self.y / norm

    def setAngle(self, angle, rads):
        norm = self.len()
        if rads:
            self.x = norm * cos(angle)
            self.y = norm * sin(angle)
        else:
            self.x = norm * cos(radians(angle))
            self.y = norm * sin(radians(angle))

    def rotate(self, angle, rads):
        oldAngle = self.angle(rads)
        self.setAngle(angle + oldAngle, rads)

    def rotate90(self):
        self.rotate(90, False)

    def rotateAround(self, other):
        oldAngle = self.angle(True)
        otherAngle = other.angle(True)
        self.setAngle(otherAngle + oldAngle, True)

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def setRandomDirection(self):
        rand = random.random() * 360
        self.setAngle(rand, False)

    def setLenght(self, norm):
        angle = self.angle(True)
        self.x = norm * cos(angle)
        self.y = norm * sin(angle)
