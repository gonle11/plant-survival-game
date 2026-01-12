class Plant:
    def __init__(
        self,
        name,
        water=50,
        light=50,
        humidity=50,
        optimal_water=(40, 70),
        optimal_light=(40, 70),
        optimal_humidity=(40, 70)
    ):
        self.name = name

        self.water = water
        self.light = light
        self.humidity = humidity

        self.optimal_water = optimal_water
        self.optimal_light = optimal_light
        self.optimal_humidity = optimal_humidity

        self.health = 100
        self.stress = 0
        self.alive = True

        self.growth_stage = 1
        self.age = 0

        
def is_in_optimal_range(self):
    return (
        self.optimal_water[0] <= self.water <= self.optimal_water[1] and
        self.optimal_light[0] <= self.light <= self.optimal_light[1] and
        self.optimal_humidity[0] <= self.humidity <= self.optimal_humidity[1]
    )

        
    def get_water_decay(self):
        return 1 + self.growth_stage * 0.5

        def update(self):
        if not self.alive:
            return

        # Time passes
        self.age += 1

        # Natural decay (needs increase with growth)
        self.water -= self.get_water_decay()
        self.light -= 0.5
        self.humidity -= 0.3

        # Stress logic
        if not self.is_in_optimal_range():
            self.stress += 1
        else:
            self.stress = max(0, self.stress - 1)

        # Delayed health impact
        if self.stress > 10:
            self.health -= 2
        if self.stress > 20:
            self.health -= 5

        # Growth
        if self.age % 30 == 0 and self.growth_stage < 3:
            self.growth_stage += 1

        # Death
        if self.health <= 0:
            self.alive = False



        
