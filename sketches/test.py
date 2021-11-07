from vector.vec2d import Vec2D
from vector.vec3d import Vec3D

fred = Vec2D()

ted = Vec2D(1, 1)

jo = Vec3D(0, 7, 8)
jim = Vec3D(3, 2, 1)

#ted /= 10.0
jim *= 3

print(jo.dist(jim))

for i in ted.tuple():
    print(i)
