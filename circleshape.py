import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        print("hello")
        pass

    def update(self, dt):
        pass

    def collided(self, circleShape):
        
        if self.position.distance_to(circleShape.position) <=  self.radius + circleShape.radius:
            print("boolet?",self.position.distance_to(circleShape.position), self.radius, circleShape.radius)

        if self.position.distance_to(circleShape.position) <=  self.radius + circleShape.radius:
            return True
        return False