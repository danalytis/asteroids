import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        position = self.position
        position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        direction = self.velocity.rotate(random_angle)
        opposite_direction = self.velocity.rotate(-random_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        asteroid_two = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        asteroid_one.velocity = direction * 1.2
        asteroid_two.velocity = opposite_direction * 1.2
