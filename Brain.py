import random

class Brain:
    MUTATION_RATE = 0.04

    def __init__(self, size):
        self.moves = []
        self.size = size

        self.randomize()
        
    def get_clone(self):
        b = Brain(self.size)
        b.moves = [x for x in self.moves]
        return b

    def randomize(self):
        for i in range(self.size):
            x, y = random.uniform(-1,1), random.uniform(-1,1)
            self.moves.append([x,y])

    def mutate(self):
        for i in range(len(self.moves)):
            r = random.random()
            if r < self.MUTATION_RATE:
                self.moves[i] = [random.uniform(-1,1), random.uniform(-1,1)]
        