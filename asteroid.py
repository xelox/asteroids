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


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
