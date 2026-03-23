#simulation.py

import random
import csv
from tkinter import *
import simul

class Simulation:
    def __init__(self, plants, plant_pool):
        self.plants = plants
        self.plant_pool = plant_pool
        self.time = 0
        self.running = True
        self.level = 1
        #self.spawn_start = 5     # earliest time
        #self.spawn_end = 60      # latest time
        
        self.spawn_probability = 0.1



        
    def update(self,canvaJeu,fenetre):
        self.time += 1

        # define if level up
        if self.time % 40 == 0 and self.level < 3:
            self.level += 1

    
        # Decide which difficulties are allowed
        if self.time < 30:
            allowed = ["easy"]
        elif self.time < 60:
            allowed = ["easy", "medium"]
        elif self.time < 75:
            allowed = ["medium", "hard"]
        else:
            allowed = ["medium", "hard", "special"]

        
        # Random spawn
        if random.random() < self.spawn_probability:
            possible = [
                plant
                for level in allowed
                for plant in self.plant_pool[level]
            ]
    
            if possible:
                new_plant = random.choice(possible)
                self.plant_pool[new_plant.difficulty].remove(new_plant)
<<<<<<< HEAD
                self.plants.append(new_plant)
                ###
                print(new_plant.name)
                simul.afficheplt(new_plant.name,canvaJeu,fenetre)
                
=======
                ### AFFICHE LA PLANTE DANS LE JEU ###
    
>>>>>>> 5b1d6f3ed5f78c32ec3acad42c143d371d403e8f
        # Update plants
        for plant in self.plants:
            plant.update()
            if not plant.alive:
                self.running = False



    
