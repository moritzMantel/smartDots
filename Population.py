import pygame
from Colors import color
from Dot import Dot
import random

class Population:
    MOVES = 2000

    def __init__(self, size, game_finish):
        self.game_finish = game_finish
        self.size = size
        self.dots = []
        self.gen = 1

        self.fitness_sum = 0
        self.min_steps = self.MOVES
        
        for i in range(size):
            self.dots.append(Dot(self.MOVES))

    def draw(self, window):
        for dot in self.dots:
            dot.draw(window)

    def natural_selection(self):
        for dot in self.dots:
            self.calculate_fitness(dot)
        
        self.get_fitness_sum()

        new_dots = []

        champ = self.get_champ().get_clone()
        champ.color = color.BLUE
        new_dots.append(champ)

        for i in range(self.size - 1):
            dot = self.select_parent().get_clone()
            dot.brain.mutate()  
            new_dots.append(dot)

        self.dots = new_dots
        self.gen += 1
        
    def calculate_fitness(self, dot):
        if dot.won:
            dot.score = 1/16 + 10000 / (dot.step * dot.step)
        
        else:
            dot.score = 1 / (((self.game_finish.y - dot.y)**2) + ((self.game_finish.x - dot.x)**2))
    
    def get_fitness_sum(self):
        sum = 0
        for dot in self.dots:
            sum += dot.score 
        self.fitness_sum = sum
    
    def get_champ(self):
        max = 0
        champ = None

        for dot in self.dots:
            if dot.score > max:
                max = dot.score
                champ = dot

        if champ.won:
            self.min_steps = champ.step

        print(f"best of gen{self.gen}: {champ.score}")
        return champ
    
    def select_parent(self):
        running_sum = 0
        r = random.uniform(0,self.fitness_sum)

        for dot in self.dots:
            running_sum += dot.score
            if running_sum > r:
                return dot

        print("something is wrong!!!")
    
    def check_moves(self):
        for dot in self.dots:
            if dot.step > self.min_steps:
                dot.dead = True
