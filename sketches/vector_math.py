import py5
from vector.vec2d import Vec2D
# Vector
# by Daniel Shiffman.
# PVector was used in the original (instead of Vec2D)
# Demonstration some basic vector math: subtraction, normalization, scaling
# Normalizing a vector sets its length to 1.
w = 640
h = 360

def setup():
    sketch_title('Vector Math')

def draw():
    py5.background(0)
    # A vector that points to the mouse location
    mouse = Vec2D(py5.mouse_x, py5.mouse_y)
    # A vector that points to the center of the window
    center = Vec2D(w / 2, h / 2)
    # Subtract center from mouse which results in a vector that points from center to mouse
    mouse -= center
    # Normalize the vector
    mouse.normalize()
    # Multiply its length by 150 (Scaling its length)
    mouse *= 150
    py5.translate(w / 2, h / 2)
    # Draw the resulting vector
    py5.stroke(255)
    py5.stroke_weight(4)
    py5.line(0, 0, mouse.x, mouse.y)

def settings():
    py5.size(w, h)

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
