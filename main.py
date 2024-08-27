# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame;
from constants import *;
from player import Player;

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # begin
        dt = clock.tick(60) / 1000

        # update
        player.update(dt);

        # render
        player.draw(screen);

        # end
        pygame.display.flip()
        screen.fill("black")

if __name__ == "__main__":
    main()
