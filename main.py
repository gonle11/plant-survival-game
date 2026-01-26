
from plant import Plant
from simulation import Simulation
import time
import ramdom

     
first_plant = random.choice(plant_pool["easy"])
plant_pool["easy"].remove(first_plant)

simulation = Simulation(
    plants=[first_plant],
    plant_pool=plant_pool
)




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

print("💀 GAME OVER — A plant has died")
