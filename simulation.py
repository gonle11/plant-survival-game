import random

class Simulation:
    def __init__(self, plants, plant_pool):
        self.plants = plants
        self.plant_pool = plant_pool
        self.time = 0
        self.running = True
        #self.spawn_start = 5     # earliest time
        #self.spawn_end = 60      # latest time
        
        self.spawn_probability = 0.1



        
        def update(self):
            self.time += 1
        
            # Decide which difficulties are allowed
            if self.time < 30:
                allowed = ["easy"]
            elif self.time < 60:
                allowed = ["easy", "medium"]
            else:
                allowed = ["medium", "hard"]
        
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
        
            # Update plants
            for plant in self.plants:
                plant.update()
                if not plant.alive:
                    self.running = False

    
