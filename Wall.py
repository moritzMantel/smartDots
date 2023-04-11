import pygame
from Colors import color

class Wall:
    COLOR = color.RED
    WIDTH, HEIGHT = 700 - 200, 20

    def __init__(self, x, y, horizontal= True):
        if not horizontal:
            self.WIDTH, self.HEIGHT = self.HEIGHT, self.WIDTH
        self.x = x
        self.y = y
            
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))