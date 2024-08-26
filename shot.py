import pygame
from circleshape import CircleShape
from constants import *

class Boolet(CircleShape):
    def __init__(self, position,x=0, y=0, radius=0,rotation=0):
        super().__init__(x, y, BOOLET_RADIUS)

        self.position = position
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius,  2)

    def update(self,  dt):
        self.position += (self.velocity * dt)




