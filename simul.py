from plant_class import Plant
from plant_difficulty import plant_pool
from simulation import Simulation
import time
import random
from score import save_score, get_best_score
import csv
from tkinter import *
import Finfoplt

def sim (fenetre,canvaJeu):
    print("debutJeu")

    first_plant = random.choice(plant_pool["easy"])
    plant_pool["easy"].remove(first_plant)

    simulation = Simulation(
        plants=[first_plant],
        plant_pool=plant_pool,
    )
    print(first_plant.name)

    def sii():
        si(simulation)

    def si(simulation):
        listefct=[Finfoplt.infoplt1,Finfoplt.infoplt2,Finfoplt.infoplt3]
        
        if simulation.running:
            simulation.update()
            print(f"Time: {simulation.time}")
            for i, plant in enumerate(simulation.plants):   # affiche les infos de chaque plantes à relier avec interface
                print(
                    f"Plant {i+1} | "
                    f"Health: {plant.health} | "
                    f"Stress: {plant.stress} | "
                    f"Stage: {plant.growth_stage}",
                    plant.name,
                )
                #canvaJeu.itemconfig(str(plant.name),state='hidden')##
                #dicopltidex = {0 : "Epipremnum aureum",....}
                def appel_info():
                    listefct[i](fenetre)
                pltplace = [["Epipremnum aureum",1100,250,1050,300],["Sansevieria trifasciata",1100,400,1050,450],["Chlorophytum comosum",1100,550,1050,600]]
                canvaJeu.plt1=PhotoImage(file="top-view_1.png")
                canvaJeu.create_image(pltplace[i][1],pltplace[i][2],image=canvaJeu.plt1,tag=pltplace[i][0])
                btnplt1=Button(fenetre,font=("Arial",10),width="15",text=pltplace[i][0],bg="peru",command=appel_info)
                btnplt1.place(x=pltplace[i][3],y=pltplace[i][4])
                


                canvaJeu.pack()
                fenetre.update()
                fenetre.after(1000, sii)
        else:
            # gestion chronos
            player_name = "Alice"  # later passed from UI
            save_score(player_name, simulation.time)
            print("💀 GAME OVER — Une plante est morte")
            canvaFin = Canvas(fenetre, width=1300, height=645)
            canvaFin.create_text(200,200,text="VOUS AVEZ PERDU")
            canvaFin.pack()
            fenetre.update()

            #dispay best time
            best_player, best_time = get_best_score()
            print(best_player,best_time)
            with open("best_score.txt","w") as f:
                f.write(f"{best_player} {best_time}")

            best_time = (
                "Jouer pour afficher vos scores!" 
                if best_player is None 
                else f"{best_player}, {best_time}" 
            )
                
    si(simulation)

    
