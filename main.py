# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame;
from constants import *;
from player import *;
from asteroid import Asteroid;
from asteroidfield import AsteroidField;
import sys;

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group();
    updateable = pygame.sprite.Group();
    drawable = pygame.sprite.Group();
    shots = pygame.sprite.Group();

    Player.containers = (updateable, drawable);
    Asteroid.containers = (updateable, drawable, asteroids);
    AsteroidField.containers = (updateable);
    Shot.containers = (shots, updateable, drawable);


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField();

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # begin
        dt = clock.tick(60) / 1000

        # update
        for u in updateable:
            u.update(dt);

        for a in asteroids:
            if player.collides(a):
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.collides(s):
                    a.split();
                    s.kill();

        # render
        for u in drawable:
            u.draw(screen);

        # end
        pygame.display.flip()
        screen.fill("black")

if __name__ == "__main__":
    main()
