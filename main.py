from plant import Plant
from simulation import Simulation
import time

available_plants = [
    create_Epipremnum_aureum(), 
]

simulation = Simulation(
    plants=[],
    available_plants=available_plants
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
