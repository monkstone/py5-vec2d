# A class to describe a group of Particles.
# A list is used to manage the list of Particles.

from particle_system.particle import Particle


class ParticleSystem(object):

    def __init__(self, num, v, img):
        self.particles = []  # Initialize the list.
        self.origin = v.copy()  # Store the origin.
        self.img = img
        for i in range(num):
            # Add "num" amount of particles to the arraylist.
            self.particles.append(Particle(self.origin, img))

    def run(self):
        for i in reversed(range(len(self.particles))):
            p = self.particles[i]
            p.run()
            if p.is_dead():
                del self.particles[i]

    # Method to add a force vector to all particles currently in the system.
    def apply_force(self, dir):
        for p in self.particles:
            p.apply_force(dir)

    def add_particle(self):
        self.particles.append(Particle(self.origin, self.img))
