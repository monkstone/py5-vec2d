import py5
from vector.vec2d import Vec2D
import numpy as np

ALPHA = 45
OMEGA = 405
THETA = 9
state = False

def settings():
    py5.size(200, 200)

def setup():
    global circle, square, morph
    sketch_title('Morph')
    circle = []
    square = []
    morph = []
    angles = range(ALPHA, OMEGA, THETA)
    py5.frame_rate(15)
    for angle in angles:
        circle.append(Vec2D.from_angle(py5.radians(angle), 50))
        morph.append(Vec2D(0, 0))
    nvalues = -np.arange(-50, 50, 10)
    pvalues = np.arange(-50, 50, 10)
    for x in np.nditer(pvalues): # top
        square.append(Vec2D(x, -50))
    for y in np.nditer(pvalues): # right side
        square.append(Vec2D(50, y))
    for x in np.nditer(nvalues): # bottom
        square.append(Vec2D(x, 50))
    for y in np.nditer(nvalues): # left side
        square.append(Vec2D(-50, y))

def draw():
    global state
    py5.background(51)
    total_distance = 0
    for i in range(len(circle)):
        v1 = circle[i] if state else square[i]
        v2 = morph[i]
        v2 = v2.lerp(v1, 0.1)
        total_distance += v1.dist(v2)
    if (total_distance < 0.08):
        state = not(state)
    py5.translate(py5.width / 2.0, py5.height / 2.0)
    py5.no_fill()
    py5.stroke(255)
    py5.stroke_weight(4)
    py5.begin_shape()
    py5.vertices([v.tuple() for v in morph])
    py5.end_shape(py5.CLOSE)

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
