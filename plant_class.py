class Plant:
    def __init__(
        self,
        name,
        water=50,
        light=50,
        humidity=50,
        optimal_water=(40, 70),
        optimal_light=(40, 70),
        optimal_humidity=(40, 70),
        optimal_warmth = (40, 70),
        difficulty="easy"
    ):
        self.name = name

        self.water = water
        self.light = light
        self.humidity = humidity

        self.optimal_water = optimal_water
        self.optimal_light = optimal_light
        self.optimal_humidity = optimal_humidity
        self.optimal_warmth = optimal_warmth
        self.difficulty = difficulty
        self.health = 100
        self.stress = 0
        self.alive = True

        self.growth_stage = 1
        self.age = 0

    # easy plants
    @staticmethod
    def create_Epipremnum_aureum():
        return Plant(
            name="Epipremnum aureum",
            water=50,
            light=55,
            humidity=50,
            warmth=55,
            optimal_water=(40, 60),
            optimal_light=(40, 70),
            optimal_humidity=(40, 60),
            optimal_warmth=(45, 65),
            difficulty="easy"
        )
    
    @staticmethod
    def create_Sansevieria_trifasciata():
        return Plant(
            name="Sansevieria trifasciata",
            water=40,
            light=55,
            humidity=30,
            warmth=55,
            optimal_water=(30, 50),
            optimal_light=(30, 80),
            optimal_humidity=(20, 40),
            optimal_warmth=(45, 65),
            difficulty="easy"
        )
    
    @staticmethod
    def create_Chlorophytum_comosum():
        return Plant(
            name="Chlorophytum comosum",
            water=55,
            light=65,
            humidity=50,
            warmth=55,
            optimal_water=(45, 65),
            optimal_light=(50, 80),
            optimal_humidity=(40, 60),
            optimal_warmth=(50, 65),
            difficulty="easy"
        )

    # Medium plants
    @staticmethod
    def create_Ficus_elastica():
        return Plant(
            name="Ficus elastica",
            water=60,
            light=70,
            humidity=60,
            warmth=60,
            optimal_water=(50, 70),
            optimal_light=(60, 80),
            optimal_humidity=(50, 70),
            optimal_warmth=(55, 70),
            difficulty="medium"
        )
    
    @staticmethod
    def create_Monstera_deliciosa():
        return Plant(
            name="Monstera deliciosa",
            water=65,
            light=70,
            humidity=70,
            warmth=65,
            optimal_water=(55, 75),
            optimal_light=(60, 80),
            optimal_humidity=(60, 80),
            optimal_warmth=(60, 75),
            difficulty="medium"
        )
    
    @staticmethod
    def create_Spathiphyllum_wallisii():
        return Plant(
            name="Spathiphyllum wallisii",
            water=60,
            light=50,
            humidity=80,
            warmth=60,
            optimal_water=(50, 70),
            optimal_light=(40, 60),
            optimal_humidity=(70, 90),
            optimal_warmth=(55, 70),
            difficulty="medium"
        )
    
    @staticmethod
    def create_dracaena_marginata():
        return Plant(
            name="Dracaena marginata",
            water=55,
            light=60,
            humidity=50,
            warmth=60,
            optimal_water=(45, 65),
            optimal_light=(50, 70),
            optimal_humidity=(40, 60),
            optimal_warmth=(55, 70),
            difficulty="medium"
        )
        
# hard plant
    @staticmethod
    def create_Calathea_orbifolia():
        return Plant(
            name="Calathea orbifolia",
            water=65,
            light=50,
            humidity=90,
            warmth=65,
            optimal_water=(60, 70),
            optimal_light=(40, 60),
            optimal_humidity=(80, 100),
            optimal_warmth=(60, 70),
            difficulty="hard"
        )
        
    @staticmethod
    def create_Alocasia_amazonica():
        return Plant(
            name="Alocasia amazonica",
            water=70,
            light=70,
            humidity=90,
            warmth=70,
            optimal_water=(65, 75),
            optimal_light=(60, 80),
            optimal_humidity=(80, 100),
            optimal_warmth=(65, 75),
            difficulty="hard"
        )

    @staticmethod
    def create_Ficus_lyrata():
        return Plant(
            name="Ficus lyrata",
            water=60,
            light=80,
            humidity=60,
            warmth=65,
            optimal_water=(55, 65),
            optimal_light=(70, 90),
            optimal_humidity=(50, 70),
            optimal_warmth=(60, 70),
            difficulty="hard"
        )
#specilal
    @staticmethod
    def create_Cactus_ferocactus():
        return Plant(
            name="Cactus ferocactus",
            water=25,
            light=95,
            humidity=15,
            warmth=80,
            optimal_water=(20, 40),
            optimal_light=(90, 100),
            optimal_humidity=(10, 20),
            optimal_warmth=(75, 90),
            difficulty="special"
        )

@staticmethod
def create_Nepenthes_alata():
    return Plant(
        name="Nepenthes alata",
        water=75,
        light=80,
        humidity=95,
        warmth=75,
        optimal_water=(70, 80),
        optimal_light=(70, 90),
        optimal_humidity=(90, 100),
        optimal_warmth=(70, 80),
        difficulty="special"
    )


    
    def is_in_optimal_water_range(self):
        return (
            self.optimal_water[0] <= self.water <= self.optimal_water[1]
        )
        
    def is_in_optimal_light_range(self):
            return (
            self.optimal_light[0] <= self.light <= self.optimal_light[1]
            )
        
    def is_in_optimal_humidity_range(self):
        return (
            self.optimal_humidity[0] <= self.humidity <= self.optimal_humidity[1]
        )

        
    def get_water_decay(self):
        return 1 + self.growth_stage * 0.5


    def max_stress_allowed(self):
        return 25 - (self.growth_stage * 5)

    def update(self):
        if not self.alive:
            return

        if self.stress > self.max_stress_allowed():
            self.health -= 3 * self.growth_stage

        # Time passes
        self.age += 1

        # Natural decay (needs increase with growth)
        self.water -= self.get_water_decay()
        self.light -= 0.5
        self.humidity -= 0.3

        # checks the otpimal conditions
        checks_optimal = [
            self.is_in_optimal_humidity_range(),
            self.is_in_optimal_light_range(),
            self.is_in_optimal_water_range(),   
        ]
        
        self.stress += checks_optimal.count(False)
        self.stress = max(0, self.stress - 1) if all(checks_optimal) else self.stress


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

    


        
