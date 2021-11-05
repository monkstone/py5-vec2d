import py5
from vector.vec2d import Vec2D
# Bouncing Ball with Vectors
# by Daniel Shiffman.
# PVector was used in the original (instead of Vec2D)
#
# Demonstration of using vectors to control motion of body
# This example is not object-oriented
# See AccelerationWithVectors for an example of how to simulate motion using vectors in an object
#

RADIUS = 24
W = 640
H = 360



def setup():
    global loc, velocity, gravity
    sketch_title('Bouncing Ball')
    loc = Vec2D(50, 100)
    velocity = Vec2D(1.5, 2.1)
    gravity = Vec2D(0, 0.2)

def draw():
    global loc, velocity, gravity
    py5.background(0)
    # Add velocity to the location.
    loc += velocity
    # Add gravity to velocity
    velocity += gravity
    # Bounce off edges

    if (off_limits(loc)):
        velocity.x *= -1.0
    if (loc.y > (H - RADIUS)):
        # We're reducing velocity ever so slightly
        # when it hits the bottom of the window
        velocity.y *= -0.95
        loc.y = H - RADIUS

    # Display circle at location vector
    py5.stroke(255)
    py5.stroke_weight(2)
    py5.fill(127)
    py5.ellipse(loc.x, loc.y, RADIUS * 2, RADIUS * 2)

def settings():
    py5.size(W, H)
    py5.smooth(4)

def sketch_title(name):
    py5.get_surface().set_title(name)

def off_limits(loc):
    return (loc.x < RADIUS or loc.x > W - RADIUS)


py5.run_sketch()
