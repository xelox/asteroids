import circleshape;
import pygame;
from constants import *;

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y);
        self.rotation = 0
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN;

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt;

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0: return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        vel = pygame.Vector2(0, 1);
        vel = vel.rotate(self.rotation);
        vel *= PLAYER_SHOT_SPEED;
        pos = pygame.Vector2(self.position.x, self.position.y);
        shot = Shot(pos, vel)

    def update(self, dt):
        self.shoot_timer -= dt;
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


class Shot(circleshape.CircleShape):
    def __init__(self, initial_position, vel):
        super().__init__(initial_position.x, initial_position.y, SHOT_RADIUS)
        self.position = initial_position;
        self.radius = SHOT_RADIUS;
        self.velocity = vel;

    def update(self, dt):
        self.position += self.velocity * dt;

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
