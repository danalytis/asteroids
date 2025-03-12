import pygame
from circleshape import CircleShape
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.shots_group = shots_group
        self.timer = 0

    def shoot(self):
        if self.timer > 0:
            return
        else:
            newshot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            newshot.velocity = forward * PLAYER_SHOOT_SPEED
            self.shots_group.add(newshot)
            self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):

        self.timer -= 0.1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
