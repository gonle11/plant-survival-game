#simulation.py

import random
import csv
import tkinter

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



        
    def update(self):
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
                self.plants.append(new_plant)
                ###
                """
                dicoplt={"Epipremnum aureum":(1100,250,1050,300)}
                pltplace = [["Epipremnum aureum",1100,250,1050,300],["Sansevieria trifasciata",1100,400,1050,450],["Chlorophytum comosum",1100,550,1050,600]]
                canvaJeu.plt1=PhotoImage(file="top-view_1.png")
                canvaJeu.create_image(pltplace[i][1],pltplace[i][2],image=canvaJeu.plt1,tag=pltplace[i][0])
                btnplt1=Button(fenetre,font=("Arial",10),width="15",text=pltplace[i][0],bg="peru")#,command=appel_infoplt1)
                btnplt1.place(x=pltplace[i][3],y=pltplace[i][4])
                """
        # Update plants
        for plant in self.plants:
            plant.update()
            if not plant.alive:
                self.running = False



    
