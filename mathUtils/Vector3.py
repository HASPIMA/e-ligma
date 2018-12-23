from math import *
from random import *
from .Vector2 import Vector2


class Vector3(Vector2):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        self.z = z

    def __iadd__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __isub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return super().__str__()[:-1] + ', ' + str(self.z) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __mul__(self, other):  # producto cruz
        return Vector3((self.y * other.z) - (self.z * other.y), -((self.x * other.z) - (self.z * other.x)),
                       (self.x * other.y) - (self.y * other.x))

    def __imul__(self, other):
        return Vector3((self.y * other.z) - (self.z * other.y), -((self.x * other.z) - (self.z * other.x)),
                       (self.x * other.y) - (self.y * other.x))

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def len(self):
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def cylindricLen(self):  # magnitud r en coordenadas cilindricas
        return super().len()

    def isUnit(self):
        return self.len() == 1

    def isZero(self):
        return self.len() == 0

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def setZero(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def angle(self, rads):  # ángulo phi util para coordenas cilíndricas y esféricas
        if self.x == 0 and self.y == 0:
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

    def angleTheta(self, rads):  # util para coordenadas esféricas definido entre 0 y pi
        if self.isZero():
            return 0
        result = 0.0
        if self.z > 0:
            if rads:
                result = atan(super().len() / self.z)
            else:
                result = degrees(atan(super().len() / self.z))
        elif self.z == 0:
            if rads:
                result = pi / 2
            else:
                result = 90
        else:
            if rads:
                result = atan(super().len() / self.z) + pi
            else:
                result = degrees(atan(super().len() / self.z)) + 180
        return result

    # el método angleRespect() no necesita sobreescritura y retorna al angulo phi entre 2 vectores
    def angleThetaRespect(self, other, rads):
        if self.angleTheta(rads) >= other.angleTheta(rads):
            return self.angleTheta(rads) - other.angleTheta(rads)
        else:
            return -self.angleTheta(rads) + other.angleTheta(rads)

    def limit(self, min, max):
        if self.x >= min.x and self.x <= max.x and self.y >= min.y and \
                self.y <= max.y and self.z >= min.z and self.z <= max.z:

            return self
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and \
                self.y <= max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(min.x, self.y, self.z)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and \
                self.y <= max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(max.x, self.y, self.z)
        elif self.x >= min.x and self.x > max.x and self.y < min.y and \
                self.y <= max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(max.x, min.y, self.z)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and \
                self.y > max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(max.x, max.y, self.z)
        elif self.x < min.x and self.x <= max.x and self.y < min.y and \
                self.y <= max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(min.x, min.y, self.z)
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and \
                self.y > max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(min.x, max.y, self.z)
        elif self.x >= min.x and self.x <= max.x and self.y < min.y and \
                self.y <= max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(self.x, min.y, self.z)
        elif self.x >= min.x and self.x <= max.x and self.y >= min.y and \
                self.y > max.y and self.z >= min.z and self.z <= max.z:

            return Vector3(self.x, max.y, self.z)
        elif self.x >= min.x and self.x <= max.x and self.y >= min.y and \
                self.y <= max.y and self.z < min.z and self.z <= max.z:

            return Vector3(self.x, self.y, min.z)
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and \
                self.y <= max.y and self.z < min.z and self.z <= max.z:

            return Vector3(min.x, self.y, min.z)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and \
                self.y <= max.y and self.z < min.z and self.z <= max.z:

            return Vector3(max.x, self.y, min.z)
        elif self.x >= min.x and self.x > max.x and self.y < min.y and \
                self.y <= max.y and self.z < min.z and self.z <= max.z:

            return Vector3(max.x, min.y, min.z)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and \
                self.y > max.y and self.z < min.z and self.z <= max.z:

            return Vector3(max.x, max.y, min.z)
        elif self.x < min.x and self.x <= max.x and self.y < min.y and \
                self.y <= max.y and self.z < min.z and self.z <= max.z:

            return Vector3(min.x, min.y, min.z)
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and \
                self.y > max.y and self.z < min.z and self.z <= max.z:

            return Vector3(min.x, max.y, min.z)
        elif self.x >= min.x and self.x <= max.x and self.y < min.y and \
                self.y <= max.y and self.z < min.z and self.z <= max.z:

            return Vector3(self.x, min.y, min.z)
        elif self.x >= min.x and self.x <= max.x and self.y >= min.y and \
                self.y > max.y and self.z < min.z and self.z <= max.z:

            return Vector3(self.x, max.y, min.z)
        if self.x >= min.x and self.x <= max.x and self.y >= min.y and \
                self.y <= max.y and self.z >= min.z and self.z > max.z:

            return Vector3(self.x, self.y, max.z)
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and \
                self.y <= max.y and self.z >= min.z and self.z > max.z:

            return Vector3(min.x, self.y, max.z)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and \
                self.y <= max.y and self.z >= min.z and self.z > max.z:

            return Vector3(max.x, self.y, max.z)
        elif self.x >= min.x and self.x > max.x and self.y < min.y and \
                self.y <= max.y and self.z >= min.z and self.z > max.z:

            return Vector3(max.x, min.y, max.z)
        elif self.x >= min.x and self.x > max.x and self.y >= min.y and \
                self.y > max.y and self.z >= min.z and self.z > max.z:

            return Vector3(max.x, max.y, max.z)
        elif self.x < min.x and self.x <= max.x and self.y < min.y and \
                self.y <= max.y and self.z >= min.z and self.z > max.z:

            return Vector3(min.x, min.y, max.z)
        elif self.x < min.x and self.x <= max.x and self.y >= min.y and \
                self.y > max.y and self.z >= min.z and self.z > max.z:

            return Vector3(min.x, max.y, max.z)
        elif self.x >= min.x and self.x <= max.x and self.y < min.y and \
                self.y <= max.y and self.z >= min.z and self.z > max.z:

            return Vector3(self.x, min.y, max.z)
        elif self.x >= min.x and self.x <= max.x and self.y >= min.y and \
                self.y > max.y and self.z >= min.z and self.z > max.z:

            return Vector3(self.x, max.y, max.z)

    def clamp(self, min, max):
        current = self.len()
        if current < min and current <= max:
            self.setLenght(min)
        elif current >= min and current > max:
            self.setLenght(max)

    def dst2(self, x, y, z):
        return ((self.x - x) ** 2) + ((self.y - y) ** 2) + ((self.z - z) ** 2)

    def dst(self, x, y, z):
        return sqrt(self.dst2(x, y, z))

    def isOpposing(self, other):
        return self.angle(True) == -other.angle(True) and self.angleTehta(True) == -other.angleTheta(True)

    def isSameDirection(self, other):
        return self.angle(True) == other.angle(True) and self.angleTehta(True) == other.angleTheta(True)

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
        self.z = self.z / norm

    def setAngle(self, angle, rads):  # se llama para cambiar el angulo phi
        norm = self.len()
        theta = self.angleTheta(rads)
        if rads:
            self.x = norm * cos(angle) * sin(theta)
            self.y = norm * sin(angle) * sin(theta)
        else:
            self.x = norm * cos(radians(angle)) * sin(radians(theta))
            self.y = norm * sin(radians(angle)) * sin(radians(theta))

    def setAngleTheta(self, angle, rads):
        norm = self.len()
        phi = self.angle(rads)
        if rads:
            self.x = norm * cos(phi) * sin(angle)
            self.y = norm * sin(phi) * sin(angle)
            self.z = norm * cos(angle)
        else:
            self.x = norm * cos(radians(phi)) * sin(radians(angle))
            self.y = norm * sin(radians(phi)) * sin(radians(angle))
            self.z = norm * cos(radians(angle))

    def rotate(self, angle, angleTheta, rads):
        oldPhi = self.angle(rads)
        oldTheta = self.angleTheta(rads)
        self.setAngle(angle + oldPhi, rads)
        self.setAngleTheta(angleTheta + oldTheta, rads)

    def rotate90(self):
        self.rotate(90, False)
        self.rotateTheta(90, False)

    def rotateAround(self, other):
        oldAngle = self.angle(True)
        otherAngle = other.angle(True)
        oldTheta = self.angleTheta(True)
        otherTheta = other.angleTheta(True)
        self.setAngle(otherAngle + oldAngle, True)
        self.setAngleTheta(otherTheta + oldTheta, True)

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def setRandomDirection(self):
        rand = random.random() * 360
        randTheta = random.random() * 180
        self.setAngle(rand, False)
        self.setAngleTheta(randTheta, False)

    def setLenght(self, norm):
        angle = self.angle(True)
        theta = self.angleTheta(True)
        self.x = norm * cos(angle) * sin(theta)
        self.y = norm * sin(angle) * sin(theta)
        self.z = norm * cos(theta)
