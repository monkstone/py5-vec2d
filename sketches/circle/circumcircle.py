import numpy as np
from vector.vec2d import Vec2D
# Circumcircle from 3 points
class Circumcircle:
    def __init__(self, points):
        self.points = points

    def calculate(self):
        vec = self.points[2]
        self.center = Vec2D(-(self.bx() / self.am()), -(self.by() / self.am()))
        self.radius = self.center.dist(vec) # points[2] = c

    # Matrix math see matrix_math.md and in detail
    # http://mathworld.wolfram.com/Circumcircle.html

    def am(self):
         pts = self.points
         a = [pts[0].x, pts[0].y, 1.0]
         b = [pts[1].x, pts[1].y, 1.0]
         c = [pts[2].x, pts[2].y, 1.0]
         matrix = np.array([a, b, c])
         return 2 * np.linalg.det(matrix)

    def bx(self):
        pts = self.points
        a = [pts[0].mag_sq(), pts[0].y, 1.0]
        b = [pts[1].mag_sq(), pts[1].y, 1.0]
        c = [pts[2].mag_sq(), pts[2].y, 1.0]
        matrix = np.array([a, b, c])
        return -np.linalg.det(matrix)

    def by(self):
        pts = self.points
        a = [pts[0].mag_sq(), pts[0].x, 1.0]
        b = [pts[1].mag_sq(), pts[1].x, 1.0]
        c = [pts[2].mag_sq(), pts[2].x, 1.0]
        matrix = np.array([a, b, c])
        return np.linalg.det(matrix)
