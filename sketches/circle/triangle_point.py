
import py5
from vector.vec2d import Vec2D

class TPoint:
  def __init__(self, position):
      global xbound, ybound
      self.pos = position
      self.vel = Vec2D()
      self.accel = Vec2D.random()
      xbound = Boundary(0, py5.width)
      ybound = Boundary(0, py5.height)

  def direction(self, acc):
      # direction of the acceleration is defined by the new angle
      self.accel = acc
      # magnitude of the acceleration is proportional to the angle between
      # acceleration and velocity
      self.dif = acc.angle_between(vel)
      self.dif = py5.remap(dif, 0, PI, 0.1, 0.001)
      self.accel = acc * dif

  def update(self):
      self.vel += self.accel
      self.vel.limit(1.5)
      self.pos += self.vel
      check_bounds()

  def check_bounds(self):
      global xbound, ybound
      if xbound.not_include(pos.x):
          self.vel.x *= -1
      if ybound.not_include(pos.y):
          self.vel.y *= -1

class Boundary:
    '''
    Simple Boundary class
    '''
    def __init__(self, lower, upper):
        self.lo = lower
        self.hi = upper

    def not_include(self, val):
        return (val < self.lo or val > self.hi)
