from tkinter import *

def canva (fenetre):
    Plt=Toplevel(fenetre,width=500,height=500)

    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)

    valueHum = IntVar()
    scaleHum=Scale(Plt,variable=valueHum,orient=HORIZONTAL,bg="peru")
    Humid=valueHum.get()
    scaleHum.place(x=300,y=50)
    canvaPlt.create_text(133,75,text="Humidité : ",font=("Times",35))

    valueLum = IntVar()
    scaleLum=Scale(Plt,variable=valueLum,orient=HORIZONTAL,bg="peru")
    Lum=valueLum.get()
    scaleLum.place(x=300,y=100)
    canvaPlt.create_text(150,120,text="Luminosité : ",font=("Times",35))

    valueChal = IntVar()
    scaleChal=Scale(Plt,variable=valueChal,orient=HORIZONTAL,bg="peru")
    Chal=valueChal.get()
    scaleChal.place(x=300,y=150)
    canvaPlt.create_text(120,175,text="Chaleur : ",font=("Times",35))

    canvaPlt.pack()
    return Humid, Lum, Chal

def infoplt1(fenetre):
    print(canva(fenetre))