from tkinter import *
from tkinter.ttk import *
import sqlite3
import sys
import traceback

def canva(fen,txt):
    canva1=Canvas(fen,width=1000, height=130)
    canva1.bg=PhotoImage(file="bgpanneau.png")
    canva1.create_image(150,100,image=canva1.bg)
    canva1.create_text(500,25,text=txt,font=("Times",25))
    canva1.pack()

def tab(fen,p1,p2,p3,p4,unun,undeux,untrois,unquatre,deuxun,deuxdeux,deuxtrois,deuxquatre,troisun,troisdeux,troistrois,troisquatre):
    style= Style(fen)
    style.theme_use("clam")
    style.configure("Treeview", background="peru",foreground="black")

    tableau = Treeview(fen, columns=('niv','pa1', 'pa2', 'pa3','pa4'))
    
    tableau.heading('niv', text='niveau')
    tableau.heading('pa1', text=p1)
    tableau.heading('pa2', text=p2)
    tableau.heading('pa3', text=p3)
    tableau.heading('pa4', text=p4)

    tableau['show'] = 'headings'

    tableau.insert('', 'end', iid="a", values=('niveau 1',unun, undeux, untrois ,unquatre))
    tableau.insert('', 'end', iid="b", values=('niveau 2',deuxun, deuxdeux, deuxtrois,deuxquatre))
    tableau.insert('', 'end', iid="c", values=('niveau 3',troisun, troisdeux, troistrois,troisquatre))

    tableau.place(x=0,y=50)

def plante1(Pan):
    plt1=Toplevel(Pan)
    canva(plt1,"Epipremnum aureum")
    tab(plt1,'Eau (entre 40 et 60 cL)','Lumière (entre 40 et 70 %)','Humidité(entre 40 et 60 %)','Chaleur (entre 45 et 65 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

    
def plante2(Pan):
    plt2=Toplevel(Pan)
    canva(plt2,"Sansevieria trifasciata")
    tab(plt2,'Eau (entre 30 et 50 cL)','Lumière (entre 30 et 80 %)','Humidité(entre 20 et 40 %)','Chaleur (entre 45 et 65 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante3(Pan):
    plt3=Toplevel(Pan)
    canva(plt3,"Chlorophytum comosum")
    tab(plt3,'Eau (entre 45 et 65 cL)','Lumière (entre 50 et 80 %)','Humidité(entre 40 et 60 %)','Chaleur (entre 50 et 65 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante4(Pan):
    plt4=Toplevel(Pan)
    canva(plt4,"Ficus elastica")
    tab(plt4,'Eau (entre 50 et 70 cL)','Lumière (entre 60 et 80 %)','Humidité(entre 50 et 70 %)','Chaleur (entre 55 et 70 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante5(Pan):
    plt5=Toplevel(Pan)
    canva(plt5,"Monstera deliciosa")
    tab(plt5,'Eau (entre 55 et 75 cL)','Lumière (entre 60 et 80 %)','Humidité(entre 60 et 80 %)','Chaleur (entre 60 et 75 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')
    
def plante6(Pan):
    plt6=Toplevel(Pan)
    canva(plt6,"Spathiphyllum wallisii")
    tab(plt6,'Eau (entre 50 et 70 cL)','Lumière (entre 40 et 60 %)','Humidité(entre 70 et 90 %)','Chaleur (entre 55 et 70 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante7(Pan):
    plt7=Toplevel(Pan)
    canva(plt7,"Dracaena marginata")
    tab(plt7,'Eau (entre 45 et 65 cL)','Lumière (entre 50 et 70 %)','Humidité(entre 40 et 60 %)','Chaleur (entre 55 et 70 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante8(Pan):
    plt8=Toplevel(Pan)
    canva(plt8,"Calathea orbifolia")
    tab(plt8,'Eau (entre 60 et 70 cL)','Lumière (entre 40 et 60 %)','Humidité(entre 80 et 100 %)','Chaleur (entre 60 et 70 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante9(Pan):
    plt9=Toplevel(Pan)
    canva(plt9,"Alocasia amazonica")
    tab(plt9,'Eau (entre 65 et 75 cL)','Lumière (entre 60 et 80 %)','Humidité(entre 80 et 100 %)','Chaleur (entre 65 et 75 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante10(Pan):
    plt10=Toplevel(Pan)
    canva(plt10,"Ficus lyrata")
    tab(plt10,'Eau (entre 55 et 65 cL)','Lumière (entre 70 et 90 %)','Humidité(entre 50 et 70 %)','Chaleur (entre 60 et 70 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante11(Pan):
    plt11=Toplevel(Pan)
    canva(plt11,"Cactus ferocactus")
    tab(plt11,'Eau (entre 20 et 40 cL)','Lumière (entre 90 et 100 %)','Humidité(entre 10 et 20 %)','Chaleur (entre 75 et 90 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante12(Pan):
    plt12=Toplevel(Pan)
    canva(plt12,"Nepenthes alata")
    tab(plt12,'Eau (entre 70 et 80 cL)','Lumière (entre 70 et 90 %)','Humidité(entre 90 et 100 %)','Chaleur (entre 70 et 80 %)','-4cl/sec','-4%/sec','-4%/sec','-4%/sec','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')