import pygame
from Colors import color

class Finish:
    COLOR = color.GREEN
    RADIUS = 10

    IMAGE_SIZE = (4* RADIUS, 4* RADIUS)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("portal.png")
        self.image = pygame.transform.scale(self.image, self.IMAGE_SIZE)

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.RADIUS)
        window.blit(self.image, (
            self.x - self.IMAGE_SIZE[0] // 2,
            self.y - self.IMAGE_SIZE[1] // 2,
        ) )