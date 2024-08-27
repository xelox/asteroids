import pygame;
import random;
import math;
import circleshape;
from constants import *;

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y);
        self.radius = radius;

    def update(self, dt):
        self.position += self.velocity * dt;

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        alpha = random.uniform(20, 50)
        v1 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(alpha) * 1.2;
        v2 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(-alpha) * 1.2;
        radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, radius)
        a2 = Asteroid(self.position.x, self.position.y, radius)
        a1.velocity = v1
        a2.velocity = v2


        

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
