from tkinter import *

def infoplt1(fenetre):
    Plt=Toplevel(fenetre)
    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)
    canvaPlt.pack()