import py5
from vector.vec2d import Vec2D

# A simple Particle class, renders the particle as an image.
class Particle(object):

    def __init__(self, l, img):
        self.acc = Vec2D(0, 0)
        py5.random_seed(1111)
        self.vx = py5.random_gaussian() * 0.3
        self.vy = py5.random_gaussian() * 0.3 - 1.0
        self.vel = Vec2D(self.vx, self.vy)
        self.loc = l.copy()
        self.lifespan = 100.0
        self.img = img

    def run(self):
        self.update()
        self.render()

    # Method to apply a force vector to the Particle object
    # Note we are ignoring "mass" here.
    def apply_force(self, f):
        self.acc += f

    # Method to update location
    def update(self):
        self.vel += self.acc
        self.loc += self.vel
        self.lifespan -= 2.5
        self.acc *= 0 # clear Acceleration.

    # Method to display
    def render(self):
        py5.image_mode(py5.CENTER)
        py5.tint(255, self.lifespan)
        py5.image(self.img, self.loc.x, self.loc.y)
        # Drawing a circle instead.
        # fill(255,lifespan)
        # noStroke()
        # ellipse(self.loc.x,self.loc.y,self.img.width,self.img.height)

    # Is the particle still useful?
    def is_dead(self):
        return self.lifespan <= 0.0
