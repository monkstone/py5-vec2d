# After a toxiclibs "MeshDoodle" sketch by Karsten Schmidt
# Adapted to use JRubyArt Vec2D and Vec3D classes by Martin Prout
# Note: The extension of Vec3D class to support rotations, and the ruby Struct
# Face for triangle 'mesh'. Also an example of AppRenderer for Vec3D => vertex
import py5
import math
from vector.vec2d import Vec2D
from vector.vec3d import Vec3D

W = 600
H = 600
faces = []

def settings():
    py5.size(600, 600, py5.P3D)

def setup():
    global weight, prev, p, q, rotation
    sketch_title('Ribbon Doodle')
    weight = 0
    prev = Vec3D()
    p = Vec3D()
    q = Vec3D()
    rotation = Vec2D()

def draw():
    global rotation, faces
    py5.background(0)
    py5.lights()
    py5.translate(W / 2, H / 2, 0)
    py5.rotate_x(rotation.x)
    py5.rotate_y(rotation.y)
    py5.no_stroke()
    py5.begin_shape(py5.TRIANGLES)
    # iterate over all faces/triangles of the 'mesh'
    for face in faces:
        py5.vertices([v.tuple() for v in face])
    py5.end_shape()
    # update rotation
    rotation += Vec2D(0.014, 0.0237)

def mouse_moved():
    global pos, prev, p, q, weight
    # get 3D rotated mouse position
    pos = Vec3D(py5.mouse_x - W / 2, py5.mouse_y - H / 2, 0)
    pos.rotate_x(rotation.x)
    pos.rotate_y(rotation.y)
    # use distance to previous point as target stroke weight
    weight += (math.sqrt(pos.dist(prev)) * 2 - weight) * 0.1
    # define offset points for the triangle strip
    a = pos + Vec3D(0, 0, weight)
    b = pos + Vec3D(0, 0, -weight)
    # add 2 faces to the mesh
    faces.append(tuple([p, b, q]))
    faces.append(tuple([p, a, b]))
    # store current points for next iteration
    prev = pos
    p = a
    q = b

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
