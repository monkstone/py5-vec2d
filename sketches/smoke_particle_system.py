"""
Smoke Particle System
by Daniel Shiffman.

A basic smoke effect using a particle system. Each particle
is rendered as an alpha masked image.
"""
import py5
from vector.vec2d import Vec2D
from particle_system.particle import Particle
from particle_system.particle_system import ParticleSystem

ps = None

def settings():
    py5.size(640, 360)

def setup():
    global ps

    img = py5.load_image('texture.png')
    ps = ParticleSystem(0, Vec2D(py5.width / 2, py5.height - 60), img)


def draw():
    py5.background(0)
    # Calculate a "wind" force based on mouse horizontal position.
    dx = py5.remap(py5.mouse_x, 0, py5.width, -0.2, 0.2)
    wind = Vec2D(dx, 0)
    ps.apply_force(wind)
    ps.run()
    for i in range(2):
        ps.add_particle()
    # Draw an arrow representing the wind force.
    draw_vector(wind, Vec2D(py5.width / 2, 50), 500)


# Renders a vector object 'v' as an arrow and a location 'loc'.
def draw_vector(v, loc, scayl):
    with py5.push_matrix():
        arrowsize = 4
        # Translate to location to render vector.
        py5.translate(loc.x, loc.y)
        py5.stroke(255)
        # Call vector heading function to get direction (note that pointing up is
        # a heading of 0) and rotate.
        py5.rotate(v.heading())
        # Calculate length of vector & scale it to be bigger or smaller if
        # necessary.
        len = v.mag() * scayl
        # Draw three lines to make an arrow (draw pointing up since we've rotate
        # to the proper direction).
        py5.line(0, 0, len, 0)
        py5.line(len, 0, len - arrowsize, + arrowsize / 2)
        py5.line(len, 0, len - arrowsize, - arrowsize / 2)

py5.run_sketch()
