import py5
from vector.vec2d import Vec2D

class Mover(object):

    def __init__(self):
        self.acceleration = None
        # Start in the center
        self.location = Vec2D(py5.width / 2, py5.height / 2)
        self.velocity = Vec2D()
        self.topspeed = 5

    def update(self):
        # Compute a vector that points from location to mouse
        mouse = Vec2D(py5.mouse_x, py5.mouse_y)
        self.acceleration = mouse - self.location
        # Set magnitude of acceleration
        self.acceleration.set_mag(0.2)
        # Velocity changes according to acceleration
        self.velocity += self.acceleration
        # Limit the velocity by topspeed
        self.velocity.limit(self.topspeed)
        # Location changes by velocity
        self.location += self.velocity

    def display(self):
        py5.stroke(255)
        py5.stroke_weight(2)
        py5.fill(127)
        py5.ellipse(self.location.x, self.location.y, 48, 48)

    def run(self):
        self.update()
        self.display()
