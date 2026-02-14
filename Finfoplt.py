from tkinter import *

def recup_hum(Humid):
    print(Humid)


def recup_lum(Lumin):
    print(Lumin)

def recup_chal(Chal):
    print(Chal)

def ajt_eau():
    global eauActu
    eauActu+=10
    print(eauActu)
    canvaPlt.itemconfigure("eau",text="(actuelement : {} cl)".format(eauActu))

def canva (fenetre,lumi,humi,chal):
    global valueHum, valueLum, valueChal,canvaPlt
    Plt=Toplevel(fenetre,width=500,height=500)

    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)

    valueHum = IntVar()
    scaleHum=Scale(Plt,variable=valueHum,orient=HORIZONTAL,bg="peru",command=recup_hum)
    scaleHum.set(humi)
    scaleHum.place(x=300,y=50)
    canvaPlt.create_text(133,75,text="Humidité : ",font=("Times",35))

    valueLum = IntVar()
    scaleLum=Scale(Plt,variable=valueLum,orient=HORIZONTAL,bg="peru",command=recup_lum)
    scaleLum.set(lumi)
    scaleLum.place(x=300,y=100)
    canvaPlt.create_text(150,120,text="Luminosité : ",font=("Times",35))

    valueChal = IntVar()
    scaleChal=Scale(Plt,variable=valueChal,orient=HORIZONTAL,bg="peru",command=recup_chal)
    scaleChal.set(chal)
    scaleChal.place(x=300,y=150)
    canvaPlt.create_text(120,175,text="Chaleur : ",font=("Times",35))

    canvaPlt.create_text(85,215,text="Eau :",font=("Times",35))
    canvaPlt.create_text(250,225,text="(actuelement : {} cl)".format(eauActu),font=("Times",15),tag="eau")
    btnAjoutEau=Button(Plt,text="Ajouter \n de l'eau",background="blue",command=ajt_eau)
    btnAjoutEau.place(x=400,y=200)

    canvaPlt.pack()

def infoplt1(fenetre):
    global eauActu
    eauActu=50
    canva(fenetre,55,50,55)

def infoplt2(fenetre):
    global eauActu
    eauActu=40
    canva(fenetre,55,30,55)

def infoplt3(fenetre):
    global eauActu
    eauActu=55
    canva(fenetre,65,50,55)

def infoplt4(fenetre):
    global eauActu
    eauActu=60
    canva(fenetre,70,60,60)

def infoplt5(fenetre):
    global eauActu
    eauActu=65
    canva(fenetre,70,70,65)

def infoplt6(fenetre):
    global eauActu
    eauActu=60
    canva(fenetre,50,80,60)

def infoplt7(fenetre):
    global eauActu
    eauActu=55
    canva(fenetre,60,50,60)

def infoplt8(fenetre):
    global eauActu
    eauActu=65
    canva(fenetre,60,90,65)

def infoplt9(fenetre):
    global eauActu
    eauActu=70
    canva(fenetre,70,90,70)

def infoplt10(fenetre):
    global eauActu
    eauActu=60
    canva(fenetre,80,60,65)

def infoplt11(fenetre):
    global eauActu
    eauActu=25
    canva(fenetre,95,15,80)

def infoplt12(fenetre):
    global eauActu
    eauActu=75
    canva(fenetre,80,95,75)
