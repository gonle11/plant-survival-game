from plant_class import Plant
from plant_difficulty import plant_pool
from simulation import Simulation
import time
import random
from score import save_score, get_best_score
import csv
from tkinter import *
import Finfoplt
import simulation 



def afficheplt(nom,canvaJeu,fenetre):
    
    def appel_plt1():
        Finfoplt.infoplt1(fenetre)
    def appel_plt2():
        Finfoplt.infoplt2(fenetre)
    def appel_plt3():
        Finfoplt.infoplt3(fenetre)
    liste_plt=[appel_plt1,appel_plt2,appel_plt3]
      
    dicoplt={"Epipremnum aureum":(1,1050,175,1050,300),"Sansevieria trifasciata":(2,1050,325,1050,450),"Chlorophytum comosum":(3,1050,475,1050,600)}
    #pltplace = [["Epipremnum aureum",1100,250,1050,300],["Sansevieria trifasciata",1100,400,1050,450],["Chlorophytum comosum",1100,550,1050,600]]
    valeurs = dicoplt.get(nom)
    i,ix,iy,bx,by = valeurs

    plt1=PhotoImage(file="top-view_1.png")
    plt2=PhotoImage(file="top-view_2.png")
    plt3=PhotoImage(file="top-view_3.png")
    
    listeimg=[plt1,plt2,plt3]
    #canvaJeu.create_image(ix,iy,image=listeimg[i-1])
    labelimg=Label(fenetre,image=listeimg[i-1])
    labelimg.place(x=ix,y=iy)
    btnplt=Button(fenetre,font=("Arial",10),width="15",text=nom,bg="peru",command=liste_plt[i-1])
    btnplt.place(x=bx,y=by)
    canvaJeu.pack()
    fenetre.update()

def sim (fenetre,canvaJeu):
    print("debutJeu")

    first_plant = random.choice(plant_pool["easy"])
    plant_pool["easy"].remove(first_plant)

    simulation = Simulation(
        plants=[first_plant],
        plant_pool=plant_pool,
    )
    print(first_plant.name)
    afficheplt(first_plant.name,canvaJeu,fenetre)

    def sii():
        si(simulation)

    def si(simulation):      
        
        if simulation.running:
            simulation.update(canvaJeu,fenetre)
            print(f"Time: {simulation.time}")
            for i, plant in enumerate(simulation.plants):   # affiche les infos de chaque plantes à relier avec interface
                print(
                    f"Plant {i+1} | "
                    f"Health: {plant.health} | "
                    f"Stress: {plant.stress} | "
                    f"Stage: {plant.growth_stage}",
                    plant.name,
                    i
                )
                """
                def appel_info():
                    listefct[i](fenetre)
                    print(i)

                pltplace = [["Epipremnum aureum",1100,250,1050,300,"top-view_1.png"],["Sansevieria trifasciata",1100,400,1050,450,"fond_lavande.png"],["Chlorophytum comosum",1100,550,1050,600,"top-view_1.png"]]
                canvaJeu.plt=PhotoImage(file=pltplace[i][5])
                canvaJeu.create_image(pltplace[i][1],pltplace[i][2],image=canvaJeu.plt,tag=pltplace[i][0])
                canvaJeu.pack()
                btnplt=Button(fenetre,font=("Arial",10),width="15",text=pltplace[i][0],bg="peru",command=appel_info)
                btnplt.place(x=pltplace[i][3],y=pltplace[i][4])
            """
                
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

    
