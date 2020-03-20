import sys
import arcade
sys.path.append("..")

import ui.world as world

class Simulation:
    def __init__(self, size):
        self.world = world.World(1200, 600)
        self.size = size
        self.population = []

    def setup(self):
        #Create birds
        for i in range(self.size):
            self.population.append(world.Bird(str(i), self.world))

    def crossover(self):
        pass

    def mutation(self):
        pass

    def roulette_whell(self):
        pass

    def ellitism(self):
        pass

    def run(self):
        #start simulation to end
        #compute fitness score forech bird and get sorted list
        #create new pool for next generation
        #ellitism -> final pool n*0.02
        #roullette wheel for selecction -> 0.5*n
        #crossover -> 0.98 * n
        #mutation with factor of 0.004
        #go to 1


Simulation()