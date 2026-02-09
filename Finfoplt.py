from tkinter import *

def infoplt1(fenetre):
    Plt=Toplevel(fenetre,width=500,height=500)
    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)

    
    valueHum = IntVar()
    scaleHum=Scale(Plt,variable=valueHum,orient=HORIZONTAL,bg="peru")
    Humid=valueHum.get()
    scaleHum.place(x=300,y=50)
    canvaPlt.create_text(100,50,text="Humidité : ")

    valueLum = IntVar()
    scaleLum=Scale(Plt,variable=valueLum,orient=HORIZONTAL,bg="peru")
    Lum=valueLum.get()
    scaleLum.place(x=300,y=100)
    canvaPlt.create_text(100,100,text="Luminosité : ")

    valueChal = IntVar()
    scaleChal=Scale(Plt,variable=valueChal,orient=HORIZONTAL,bg="peru")
    Chal=valueChal.get()
    scaleChal.place(x=300,y=150)
    canvaPlt.create_text(100,150,text="Chaleur : ")

    canvaPlt.pack()