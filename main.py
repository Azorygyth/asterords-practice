import sys
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *
import random


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
    asteroids = pygame.sprite.Group()
    boolets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Boolet.containers = (boolets, updatable, drawable)
    


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        for sprite in updatable.sprites():
            sprite.update(dt)
        
        screen.fill("black")

        for sprite in drawable.sprites():
            sprite.draw(screen)

        for asteroid in asteroids.sprites():
            if player.collided(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids.sprites():
            for boolet in boolets.sprites():
                if boolet.collided(asteroid):
                    boolet.kill()
                    asteroid.split()
                    
                    
                

        pygame.display.flip()
        dt = clock.tick(60) / 1000
       
        

        

if __name__ == "__main__":
    main()




