
from plant import Plant
from simulation import Simulation
import time
import ramdom
from score import save_score, get_best_score
import csv

     
first_plant = random.choice(plant_pool["easy"])
plant_pool["easy"].remove(first_plant)

simulation = Simulation(
    plants=[first_plant],
    plant_pool=plant_pool
)
print(first_plant)




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





