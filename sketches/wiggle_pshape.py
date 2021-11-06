import py5
from wiggler.wiggler import Wiggler

# WigglePShape. Demonstrates initialization and use of ShapeRender,
# that allows us to send Vec2D to PShape vertex
#
# How to move the individual vertices of a PShape

def setup():
    global wiggle_object
    sketch_title('Wiggle PShape')
    wiggle_object = Wiggler()

def draw():
    py5.background(255)
    wiggle_object.display()
    wiggle_object.wiggle()

def sketch_title(name):
    py5.get_surface().set_title(name)

def settings():
    py5.size(640, 480, py5.P2D)

py5.run_sketch()
