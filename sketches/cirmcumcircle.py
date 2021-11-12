import py5
from vector.vec2d import Vec2D
from circle.t_points import TrianglePoints
from circle.circumcircle import Circumcircle

def settings():
    py5.size(800, 600, py5.P2D)

def setup():
    global points
    sketch_title('Circumcircle')
    py5.ellipse_mode(py5.RADIUS)
    py5.scale(1, -1)
    py5.translate(0, -py5.height)
    points = TrianglePoints()


def draw():
    global points
    py5.background(0)
    py5.no_stroke()
    pts = points.positions()
    for pt in pts:
        py5.fill(255, 255, 0)
        py5.ellipse(pt.x, pt.y, 5, 5)
        py5.fill(250)
        py5.text(str(pt), pt.x - 30, pt.y - 20)
    py5.no_fill()
    py5.stroke(200, 0, 0)
    if points.full():
        py5.triangle(pts[0].x, pts[0].y, pts[1].x, pts[1].y, pts[2].x, pts[2].y)
    draw_circle()

def mouse_pressed():
    global points
    points.append(Vec2D(py5.mouse_x, py5.mouse_y))

def draw_circle():
    global points
    circumcircle = Circumcircle(points.positions())
    if points.full():
        circumcircle.calculate()
        center_point = circumcircle.center
        radius = circumcircle.radius
        py5.no_fill()
        py5.stroke(255)
        if points.collinear():
            return
        py5.ellipse(center_point.x, center_point.y, radius, radius)

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
