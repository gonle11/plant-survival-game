import random

class Simulation:
    def __init__(self, plants, available_plants):
        self.plants = plants
        self.available_plants = available_plants
        self.time = 0
        self.running = True

        self.spawn_start = 5     # earliest time
        self.spawn_end = 60      # latest time
        self.spawn_probability = 0.1  # 10% chance per tick

    
    def update(self):
        self.time += 1
    
        # Random plant addition
        if (
            self.spawn_start <= self.time <= self.spawn_end
            and self.available_plants
            and random.random() < self.spawn_probability
        ):
            new_plant = random.choice(self.available_plants)
            self.available_plants.remove(new_plant)
            self.plants.append(new_plant)
    
        # Update existing plants
        for plant in self.plants:
            plant.update()
            if not plant.alive:
                self.running = False
    
