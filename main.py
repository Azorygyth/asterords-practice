import pygame
from player import *
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        for sprite in updatable.sprites():
            sprite.update(dt)
        
        screen.fill("black")

        for sprite in drawable.sprites():
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
       
        

        

if __name__ == "__main__":
    main()




