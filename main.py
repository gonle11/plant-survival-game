
#main.py
from plant_class import Plant
from plant_difficulty import plant_pool
from simulation import Simulation
import time
import random
from score import save_score, get_best_score
import csv
from tkinter import *

import Fjeu
import acceuil

     
first_plant = random.choice(plant_pool["easy"])
plant_pool["easy"].remove(first_plant)

simulation = Simulation(
    plants=[first_plant],
    plant_pool=plant_pool
)
fenetre=Tk()

#creation du canva + bg
canvaJeu = Canvas(fenetre, width=1300, height=645)
canvaJeu.fondBG = PhotoImage(file="fond_lavande.png")
canvaJeu.create_image(650,322,image=canvaJeu.fondBG)
canvaJeu.parquetBG = PhotoImage(file="background_fond1.png")
canvaJeu.create_image(650,322,image=canvaJeu.parquetBG)

acceuil.accueil(fenetre,canvaJeu)
print("premiere plante",first_plant.name)
canvaJeu.itemconfigure("Epipremnum aureum",state='normal')
fenetre.update()
print("show")
fenetre.mainloop()



while simulation.running:
    simulation.update()
    print(f"Time: {simulation.time}")
    for i, plant in enumerate(simulation.plants):   # affiche les infos de chaque plantes à relier avec interface
        print(
            f"Plant {i+1} | "
            f"Health: {plant.health} | "
            f"Stress: {plant.stress} | "
            f"Stage: {plant.growth_stage}"
        )
         
    time.sleep(1)  # 1 second per tick

# gestion chronos
player_name = "Alice"  # later passed from UI
save_score(player_name, simulation.time)
print("💀 GAME OVER — Une plante est morte")

#dispay best time
best_player, best_time = get_best_score()

best_time = (
     "Jouer pour afficher vos scores!" 
     if best_player is None 
     else f"{best_player}, {best_time}" 
)





