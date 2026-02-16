#plant_difficulty.py

from plant_class import Plant

plant_pool = {
    "easy": [
        Plant.create_Epipremnum_aureum(),
        Plant.create_Sansevieria_trifasciata(),
        Plant.create_Chlorophytum_comosum(),
    ],

    "medium": [
        Plant.create_Ficus_elastica(),
        Plant.create_Monstera_deliciosa(),
        Plant.create_Spathiphyllum_wallisii(),
        Plant.create_dracaena_marginata(),
    ],

    "hard": [
        Plant.create_Calathea_orbifolia(),
        Plant.create_Alocasia_amazonica(),
        Plant.create_Ficus_lyrata(),
    ],

    "special": [
        Plant.create_Cactus_ferocactus(),
        Plant.create_Nepenthes_alata(),
    ]
}
