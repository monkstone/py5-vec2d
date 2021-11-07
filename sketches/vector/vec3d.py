# A quick proof of concept, Vec3D-like class for use with my py5 sketches
# inspired by Villares PVector and Vec3D ruby-processing

import math
import operator
from numbers import Number
import copy

TWO_PI = math.tau

class Vec3D:

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
            self.z = 0
        if len(args) == 1:
            self = args[0].copy()
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    def __add__(self, other):
        temp = Vec3D()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.z = self.z + other.z
        return temp

    def __sub__(self, other):
        temp = Vec3D()
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        temp.z = self.z - other.z
        return temp

    def __mul__(self, other):
        assert type(other) in (int, float)
        temp = Vec3D()
        temp.x = self.x * other
        temp.y = self.y * other
        temp.z = self.z * other
        return temp

    def __truediv__(self, other):
        temp = Vec3D()
        temp.x = self.x / other
        temp.y = self.y / other
        temp.z = self.z / other
        return temp

    def __itruediv__(self, other):
        temp = Vec3D()
        temp.x = self.x // other
        temp.y = self.y // other
        temp.z = self.z // other
        return temp

    def mag(self):
        return math.sqrt(self.mag_sq())

    def tuple(self):
        return (self.x, self.y, self.z)

    def mag_sq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def set_mag(self, magnitude):
        return self.normalize().__mul__(magnitude)

    def normalize(self):
        magnitude = self.mag()
        if magnitude != 0:
            self.x *= (1 / magnitude)
            self.y *= (1 / magnitude)
            self.z *= (1 / magnitude)
        return self

    def dist_squared(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2

    def dist(self, other):
        return math.sqrt(self.dist_squared(other))

    def set(self, *args):
        if len(args) == 3:
            self.x, self.y, self.z = args
        elif len(args) == 1:
            self.x, self.y, self.z = args[0]

    def lerp(self, other, t):
        self.set(
            self.x + (other.x - self.x) * t,
            self.y + (other.y - self.y) * t,
            self.z + (other.z - self.z) * t
            )
        return self

    def limit(self, max):
        if (self.mag_sq() > (max * max)):
            self.set_mag(max)

    def copy(self):
        return Vec3D(self.x, self.y, self.z)


    def __str__(self):
        Vec3D = "Vec3D({x:.3f}, {y:.3f}, {z:.3f})"
        return Vec3D.format(x = self.x, y = self.y, z = self.z)

    @classmethod
    def from_angles(theta, phi, length=1):
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        return Vec3D(length * sin_theta * sin_phi, -length * cos_theta, length * sin_theta * cos_phi)
