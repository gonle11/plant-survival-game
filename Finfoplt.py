from tkinter import *

def recup_hum():
    global Humid
    Humid=valueHum.get()
    print(Humid)


def recup_lum():
    global Lumin
    Lumin=valueLum.get()
    print(Lumin)

def recup_chal():
    global Chal
    Chal=valueChal.get()
    print(Chal)

def ajt_eau():
    global eauActu
    eauActu+=10
    print(eauActu)

def canva (fenetre,eauActu,humi,lumi,chal):
    global valueHum, valueLum, valueChal
    Plt=Toplevel(fenetre,width=500,height=500)

    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)

    valueHum = IntVar()
    scaleHum=Scale(Plt,variable=valueHum,orient=HORIZONTAL,bg="peru")
    scaleHum.set(humi)
    scaleHum.place(x=300,y=50)
    canvaPlt.create_text(133,75,text="Humidité : ",font=("Times",35))
    btnHum=Button(Plt,text="Valider",background="peru",command=recup_hum)
    btnHum.place(x=450,y=50)

    valueLum = IntVar()
    scaleLum=Scale(Plt,variable=valueLum,orient=HORIZONTAL,bg="peru")
    scaleLum.set(lumi)
    scaleLum.place(x=300,y=100)
    canvaPlt.create_text(150,120,text="Luminosité : ",font=("Times",35))
    btnLum=Button(Plt,text="Valider",background="peru",command=recup_lum)
    btnLum.place(x=450,y=100)

    valueChal = IntVar()
    scaleChal=Scale(Plt,variable=valueChal,orient=HORIZONTAL,bg="peru")
    scaleChal.set(chal)
    scaleChal.place(x=300,y=150)
    canvaPlt.create_text(120,175,text="Chaleur : ",font=("Times",35))
    btnChal=Button(Plt,text="Valider",background="peru",command=recup_chal)
    btnChal.place(x=450,y=150)

    canvaPlt.create_text(85,215,text="Eau :",font=("Times",35))
    canvaPlt.create_text(250,225,text="(actuelement : {} cl)".format(eauActu),font=("Times",15))
    btnAjoutEau=Button(Plt,text="Ajouter \n de l'eau",background="blue",command=ajt_eau)
    btnAjoutEau.place(x=400,y=200)

    canvaPlt.pack()

def infoplt1(fenetre):
    canva(fenetre,35,45,65,87)