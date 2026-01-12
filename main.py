from plant import Plant
from simulation import Simulation
import time

# have to finish to complete the caracteristics of each a plant and define light, hmuidity's,  warmth's, range
plant1 = Plant(
    name="Epipremnum aureum (Scindapsus doré)",
    water=30,
    light=80,
    humidity=20
)

plant2 = Plant(
    name="Fern",
    water=60,
    light=40,
    humidity=70
)

simulation = Simulation([plant1, plant2])



simulation = Simulation([plant1, plant2])

while simulation.running:
    simulation.update()

    print(f"Time: {simulation.time}")
    for i, plant in enumerate(simulation.plants):
        print(
            f"Plant {i+1} | "
            f"Health: {plant.health} | "
            f"Stress: {plant.stress} | "
            f"Stage: {plant.growth_stage}"
        )

    time.sleep(1)  # 1 second per tick

print("💀 GAME OVER — A plant has died")
