import pygame
from Brain import Brain
from Colors import color

class Dot:
    START_X, START_Y = 350, 485
    RADIUS = 3
    VEL = 15
    ID = 1

    def __init__(self, brain_size):
        self.x = self.orig_x = self.START_X
        self.y = self.orig_y = self.START_Y
        self.step = 0
        self.brain_size = brain_size
        self.color = color.BLACK

        self.brain = Brain(brain_size)
        self.dead = False
        self.won = False
        self.score = 0
        self.id = Dot.ID
        Dot.ID += 1

    def move(self):
        if len(self.brain.moves) > self.step:
            self.x += self.brain.moves[self.step][0] * self.VEL
            self.y += self.brain.moves[self.step][1] * self.VEL
            self.step += 1
        else:
            self.dead = True

    def draw(self, window):

        pygame.draw.circle(window, self.color, (self.x, self.y), self.RADIUS)

    def get_clone(self):
        dot = Dot(self.brain_size)
        dot.brain = self.brain.get_clone()
        return dot

    def __repr__(self):
        return f"Dot: {self.id}"
