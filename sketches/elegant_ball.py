import py5
import math
from vector.vec3d import Vec3D
# elegant_ball.rb
# After a vanilla processing sketch by
# Ben Notorianni aka lazydog
#
# elegant.rb
W = 800
H = 800

def setup():
    # sketch_title('Elegant Ball')
    py5.color_mode(py5.RGB, 1)
    sketch_title('Elegant Ball')

def draw():
    py5.background(0)
    # Move the origin so that the scene is centered on the screen.
    py5.translate(W / 2, H / 2, 0.0)
    # Set up the lighting.
    setup_lights()
    # Rotate the local coordinate system.
    smooth_rotation(5.0, 6.7, 7.3)
    # Draw the inner object.
    py5.no_stroke()
    py5.fill(smooth_colour(10.0, 12.0, 7.0))
    draw_icosahedron(5, 60.0, False)
    # Rotate the local coordinate system again.
    smooth_rotation(4.5, 3.7, 7.3)
    # Draw the outer object.
    py5.stroke(0.2)
    py5.fill(smooth_colour(6.0, 9.2, 0.7))
    draw_icosahedron(5, 200.0, True)

def setup_lights():
    py5.ambient_light(0.025, 0.025, 0.025)
    py5.directional_light(0.2, 0.2, 0.2, -1, -1, -1)
    py5.spot_light(1.0, 1.0, 1.0, -200, 0, 300, 1, 0, -1, py5.PI / 4, 20)


# Generate a vector whose components change smoothly over time in the range
# (0..1). Each component uses a math.sin function to map the current time in
# milliseconds in the range (0..1).A 'speed' factor is specified for each
# component.
def smooth_vector(s1, s2, s3):
    mills = py5.millis() * 0.00003 ## Lazydogs factor
    # mills = millis * 0.0000001 ## worked for me a bit slower!!
    x = 0.5 * math.sin(mills * s1) + 0.5
    y = 0.5 * math.sin(mills * s2) + 0.5
    z = 0.5 * math.sin(mills * s3) + 0.5
    return Vec3D(x, y, z)

# Generate a colour which smoothly changes over time.
# The speed of each component is controlled by the parameters s1, s2 and s3.
def smooth_colour(s1, s2, s3):
    v = smooth_vector(s1, s2, s3)
    return py5.color(v.x, v.y, v.z)

# Rotate the current coordinate system.
# Uses smooth_vector to smoothly animate the rotation.
def smooth_rotation(s1, s2, s3):
    r1 = smooth_vector(s1, s2, s3)
    py5.rotate_x(py5.PI * 2 * r1.x)
    py5.rotate_y(py5.PI * 2 * r1.y)
    py5.rotate_x(py5.PI * 2 * r1.z)

# Draw an icosahedron defined by a radius r and recursive depth d.
# Geometry data will be saved into dst. If spherical is True then the
# icosahedron is projected onto the sphere with radius r.
def draw_icosahedron(depth, r, spherical):
    # Calculate the vertex data for an icosahedron inscribed by a sphere radius
    # 'r'. Use 4 Golden Ratio rectangles as the basis.
    gr = (1.0 + math.sqrt(5.0)) / 2.0
    h = r / math.sqrt(1.0 + gr * gr)
    v = [Vec3D(0, -h, h * gr),
    Vec3D(0, -h, -h * gr),
    Vec3D(0, h, -h * gr),
    Vec3D(0, h, h * gr),
    Vec3D(h, -h * gr, 0),
    Vec3D(h, h * gr, 0),
    Vec3D(-h, h * gr, 0),
    Vec3D(-h, -h * gr, 0),
    Vec3D(-h * gr, 0, h),
    Vec3D(-h * gr, 0, -h),
    Vec3D(h * gr, 0, -h),
    Vec3D(h * gr, 0, h)
    ]
    # Draw the 20 triangular faces of the icosahedron.
    if not spherical:
        r = 0.0
    py5.begin_shape(py5.TRIANGLES)
    draw_triangle(depth, r, v[0], v[7], v[4])
    draw_triangle(depth, r, v[0], v[4], v[11])
    draw_triangle(depth, r, v[0], v[11], v[3])
    draw_triangle(depth, r, v[0], v[3], v[8])
    draw_triangle(depth, r, v[0], v[8], v[7])
    draw_triangle(depth, r, v[1], v[4], v[7])
    draw_triangle(depth, r, v[1], v[10], v[4])
    draw_triangle(depth, r, v[10], v[11], v[4])
    draw_triangle(depth, r, v[11], v[5], v[10])
    draw_triangle(depth, r, v[5], v[3], v[11])
    draw_triangle(depth, r, v[3], v[6], v[5])
    draw_triangle(depth, r, v[6], v[8], v[3])
    draw_triangle(depth, r, v[8], v[9], v[6])
    draw_triangle(depth, r, v[9], v[7], v[8])
    draw_triangle(depth, r, v[7], v[1], v[9])
    draw_triangle(depth, r, v[2], v[1], v[9])
    draw_triangle(depth, r, v[2], v[10], v[1])
    draw_triangle(depth, r, v[2], v[5], v[10])
    draw_triangle(depth, r, v[2], v[6], v[5])
    draw_triangle(depth, r, v[2], v[9], v[6])
    py5.end_shape()


##
# Draw a triangle either immediately or subdivide it first.
# If depth is 1 then draw the triangle otherwise subdivide first.
#
def draw_triangle(depth, r, p1, p2, p3):
    if depth == 1:
        py5.vertex(p1.x, p1.y, p1.z)
        py5.vertex(p2.x, p2.y, p2.z)
        py5.vertex(p3.x, p3.y, p3.z)
    else:
        # Calculate the mid points of this triangle.
        v1 = (p1 + p2) * 0.5
        v2 = (p2 + p3) * 0.5
        v3 = (p3 + p1) * 0.5
        if r != 0:
            # Project the vertices out onto the sphere with radius r.
            v1.set_mag(r)
            v2.set_mag(r)
            v3.set_mag(r)
        # Generate the next level of detail
        depth -= 1
        draw_triangle(depth, r, p1, v1, v3)
        draw_triangle(depth, r, v1, p2, v2)
        draw_triangle(depth, r, v2, p3, v3)
        # Uncomment out the next line to include the central part of the triangle.
        # draw_triangle(depth, r, v1, v2, v3)

def settings():
    py5.size(W, H, py5.P3D)

def sketch_title(name):
    py5.get_surface().set_title(name)

py5.run_sketch()
