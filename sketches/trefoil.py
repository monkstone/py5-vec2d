"""
Trefoil, Andres Colubri
A parametric surface is textured procedurally
by drawing on an offscreen PGraphics surface.
"""
import py5
import math
from surface.surface import *
PI = math.pi

W = 1024
H = 768

def settings():
    py5.size(1024, 768, py5.P3D)

def setup():
    global pg, trefoil  # PGraphics, PShape
    sketch_title('Trefoil')
    py5.texture_mode(py5.NORMAL)
    py5.no_stroke()

    # Creating offscreen surface for 3D rendering.
    pg = py5.create_graphics(32, 512, py5.P3D)
    pg.begin_draw()
    pg.background(0, 0)
    pg.no_stroke()
    pg.fill(255, 0, 0, 200)
    pg.end_draw()

    # Saving trefoil surface into a PShape3D object
    trefoil = create_trefoil(350, 60, 15, pg)


def draw():
    py5.background(0)

    pg.begin_draw()
    pg.ellipse(py5.random(pg.width), py5.random(pg.height), 4, 4)
    pg.end_draw()

    py5.ambient(250, 250, 250)
    py5.point_light(255, 255, 255, 0, 0, 200)

    with py5.push_matrix():
        py5.translate(W / 2, H / 2, -200)
        py5.rotate_x(py5.frame_count * PI / 500)
        py5.rotate_y(py5.frame_count * PI / 500)
        py5.shape(trefoil)

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
