# A quick proof of concept, Vec2D-like class for use with my py5 sketches
# inspired by Villares PVector and Vec2D ruby-processing

import math
from numbers import Number
import copy

TWO_PI = math.tau

class Vec2D:

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        if len(args) == 1:
            self = copy.deepcopy(args[0])
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]

    def __add__(self, other):
        temp = Vec2D()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp

    def __sub__(self, other):
        temp = Vec2D()
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        return temp

    def __mul__(self, other):
        temp = Vec2D()
        temp.x = self.x * other
        temp.y = self.y * other
        return temp

    def mag(self):
        return math.sqrt(self.mag_sq())

    def to_array(self):
        return [self.x, self.y]

    def mag_sq(self):
        return self.x * self.x + self.y * self.y

    def set_mag(self, magnitude):
        return self.normalize().__mul__(magnitude)

    def normalize(self):
        magnitude = self.mag()
        if magnitude != 0:
            self.x *= (1 / magnitude)
            self.y *= (1 / magnitude)
        return self

    def dist(self, other):
        return math.sqrt(
        (self.x - other.x) * (self.x - other.x) +
        (self.y - other.y) * (self.y - other.y)
        )

    def set(self, *args):
        if len(args) == 2:
            self.x, self.y = args
        elif len(args) == 1:
            self.x, self.y = args[0]

    def lerp(self, other, t):
        self.set(
            self.x + (other.x - self.x) * t,
            self.y + (other.y - self.y) * t
            )
        return self

    def limit(self, max):
        if (self.mag_sq() > (max * max)):
            self.set_mag(max)

    def __str__(self):
        vec2d = "Vec2D({x:.3f}, {y:.3f})"
        return vec2d.format(x = self.x, y = self.y)

    @classmethod
    def from_angle(cls, angle, length=1):
        return Vec2D(length * math.cos(angle), length * math.sin(angle))
