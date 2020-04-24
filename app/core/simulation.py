import sys
import arcade
import random
sys.path.append("..")
from app.ui.bird import Bird

import ui.world as world


class Simulation:
    def __init__(self, size):
        self.world = world.World(1200, 600)
        self.size = size
        self.population = []

    @staticmethod
    def is_bird_present_in_bird_list(bird, bird_list):
        for b in bird_list:
            if b.id == bird.id:
                return True
        return False

    def setup(self):
        #Create birds
        for i in range(self.size):
            self.population.append(Bird(self.world))

    def crossover(self, next_generation):

        while len(next_generation) < len(self.population):
            rand_bird1_index = random.randint(len(self.population))
            rand_bird2_index = random.randint(len(self.population))

            if(rand_bird1_index == rand_bird2_index):
                continue

            bird1 = self.population[rand_bird1_index]
            bird2 = self.population[rand_bird2_index]

            next_generation.extends([bird1.crossover(bird2)])


    def mutation(self):
        pass

    def sort(self):
        self.population.sort(key=lambda x: x.distance, reverse=False)

    def roulette_whell(self, next_generation):
        sum = sum([bird.distance for bird in self.population])

        while len(next_generation) < self.size / 2:
            pivot = random.randint(sum)
            local_sum = 0

            for bird in self.population:
                local_sum += bird.distance

                if local_sum > pivot and not Simulation.is_bird_present_in_bird_list(bird, next_generation):
                    next_generation.append(bird)
                    break
        return next_generation

    def ellitism(self, next_generation):
        pivot = 0.98 * len(self.population)
        next_generation.extend(self.population[pivot:-1])

    def run(self):
        pass

    def create_next_generation(self):
        next_generation = []

        self.sort()
        self.ellitism(next_generation)
        self.roulette_whell(next_generation)
        self.crossover(next_generation)

        #mutation

        #tests + restrat



Simulation()