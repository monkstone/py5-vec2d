from vector.vec2d import Vec2D

MAX_POINT = 3
# A collection of a maximum of 3 points in the processing world
# includes a collinearity test using Vec2D
class TrianglePoints:
    def __init__(self):
        self.points = []

    def append(self, pt):
        self.points.append(pt)
        if len(self.points) > MAX_POINT:
            self.points.pop(0)

    def collinear(self):
        if not self.full():
            return False
        posns = self.positions()
        return (posns[0] - posns[1]).cross(posns[1] - posns[2]) == 0

    # returns positions as an array of Vec2D
    def positions(self):
        return self.points

    def full(self):
        return len(self.points) == MAX_POINT
