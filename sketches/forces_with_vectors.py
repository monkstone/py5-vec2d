"""
Acceleration with Vectors
by Daniel Shiffman.

Demonstration of the basics of motion with vector.
A "Mover" object stores location, velocity, and acceleration as vectors The
motion is controlled by affecting the acceleration (in this case towards the
mouse)
For more examples of simulating motion and physics with vectors, see
Simulate/ForcesWithVectors, Simulate/GravitationalAttraction3D
"""
import py5

from mover.mover import Mover

def settings():
    py5.size(640, 360)

def setup():
    global mover
    sketch_title('Acceleration with Vectors')
    mover = Mover()

def draw():
    py5.background(0)
    # Update the location
    mover.update()
    # Display the Mover
    mover.display()

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
