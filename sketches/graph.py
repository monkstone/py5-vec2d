import py5
from vector.vec2d import Vec2D
import numpy as np
dim = 20


def settings():
    py5.size(600, 600)

def setup():
    graph_paper()

def graph_paper():
    py5.background(0)
    axis = np.arange(dim, 590, dim)
    py5.stroke(100, 100, 0)
    for x in np.nditer(axis):
        py5.line(x, py5.width - dim, x, dim)
    for y in np.nditer(axis):
        py5.line(py5.height - dim, y, dim, y)

py5.run_sketch()
