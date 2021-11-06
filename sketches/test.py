from vector.vec2d import Vec2D

fred = Vec2D(2, 3)

ted = Vec2D(5, 7)

ted += fred

ted *= 10

print(ted.x)
print(ted.y)


print(fred)
