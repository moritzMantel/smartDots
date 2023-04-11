import pygame
from Colors import color
from Finish import Finish
from Population import Population
from Wall import Wall

pygame.init()

class Game():
    WIDTH, HEIGHT = 700, 500
    BG = color.GREY

    def __init__(self):
        self.window = pygame.display.set_mode( (self.WIDTH, self.HEIGHT) )
        pygame.display.set_caption("SMART DOTS")
        
        self.finish = Finish(self.WIDTH // 2, 15)
        self.walls = []
        self.walls.append(Wall(0, 150, horizontal=True))

        self.population = Population(500, self.finish)

        self.run = True

    def draw(self):
        self.window.fill(self.BG)

        for wall in self.walls:
            wall.draw(self.window)

        self.finish.draw(self.window)
        self.population.draw(self.window)
        
        pygame.display.update()
    
    def train(self):
        while self.run:
            
            while self.run and not self.game_dead(): 

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        break
                    
                self.move()
                self.draw()
                self.collision()
                self.population.check_moves()
                
            self.population.natural_selection()

        pygame.quit()
    
    def move(self):
        for dot in self.population.dots:
            if not dot.dead:
                dot.move()

    def collision(self):
        for dot in self.population.dots:
            if dot.x - dot.RADIUS <= 5 or dot.x + dot.RADIUS >= self.WIDTH - 5 or dot.y - dot.RADIUS <= 5 or dot.y + dot.RADIUS >= self.HEIGHT - 5:
                dot.dead = True

            if dot.x + dot.RADIUS >= self.finish.x - self.finish.RADIUS and dot.x - dot.RADIUS <= self.finish.x + self.finish.RADIUS and dot.y + dot.RADIUS >= self.finish.y - self.finish.RADIUS and dot.y - dot.RADIUS <= self.finish.y + self.finish.RADIUS:
                dot.won = True
                dot.dead = True

            for wall in self.walls:
                if dot.x + dot.RADIUS >= wall.x and dot.x - dot.RADIUS <= wall.x + wall.WIDTH and dot.y + dot.RADIUS >= wall.y and dot.y - dot.RADIUS <= wall.y + wall.HEIGHT:
                    dot.dead = True
        
    def game_dead(self):
        for dot in self.population.dots:
            if not dot.dead:
                return False
        return True
        

game = Game()
game.train()