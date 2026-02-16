from plant_class import Plant
from plant_difficulty import plant_pool
from simulation import Simulation
import time
import random
from score import save_score, get_best_score
import csv
from tkinter import *

import acceuil

def init_lancerFen(fenetre,first_plant):
    #creation du canva + bg
    canvaJeu = Canvas(fenetre, width=1300, height=645)
    canvaJeu.fondBG = PhotoImage(file="fond_lavande.png")
    canvaJeu.create_image(650,322,image=canvaJeu.fondBG)
    canvaJeu.parquetBG = PhotoImage(file="background_fond1.png")
    canvaJeu.create_image(650,322,image=canvaJeu.parquetBG)
    debutJeu=False
    acceuil.accueil(fenetre,canvaJeu)
    print("premiere plante",first_plant.name)
    canvaJeu.itemconfigure("Epipremnum aureum",state='normal')###
    canvaJeu.pack()####
    fenetre.update()###
    print("show")
