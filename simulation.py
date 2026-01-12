class Simulation:
    def __init__(self, plants):
        self.plants = plants
        self.time = 0
        self.running = True
      
    def update(self):
        self.time += 1

        for plant in self.plants:
            plant.update()
            if not plant.alive:
                self.running = False
