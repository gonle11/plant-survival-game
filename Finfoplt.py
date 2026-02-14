from tkinter import *
import FinfoPlantes

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

def canva (fenetre,titre,lumi,humi,chal,fct):
    global valueHum, valueLum, valueChal,canvaPlt,Plt    
        
    Plt=Toplevel(fenetre,width=500,height=500)

    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)

    canvaPlt.create_text(250,30,text=titre,font=("Times",50))

    btnInfo=Button(Plt,text="*",bg="orange",bd=0,command=fct)
    btnInfo.place(x=450,y=25)


    valueHum = IntVar()
    scaleHum=Scale(Plt,variable=valueHum,orient=HORIZONTAL,bg="peru",command=recup_hum)
    scaleHum.set(humi)
    scaleHum.place(x=300,y=75)
    canvaPlt.create_text(133,100,text="Humidité : ",font=("Times",35))

    valueLum = IntVar()
    scaleLum=Scale(Plt,variable=valueLum,orient=HORIZONTAL,bg="peru",command=recup_lum)
    scaleLum.set(lumi)
    scaleLum.place(x=300,y=125)
    canvaPlt.create_text(150,155,text="Luminosité : ",font=("Times",35))

    valueChal = IntVar()
    scaleChal=Scale(Plt,variable=valueChal,orient=HORIZONTAL,bg="peru",command=recup_chal)
    scaleChal.set(chal)
    scaleChal.place(x=300,y=175)
    canvaPlt.create_text(120,205,text="Chaleur : ",font=("Times",35))

    canvaPlt.create_text(85,255,text="Eau :",font=("Times",35))
    canvaPlt.create_text(250,265,text="(actuelement : {} cl)".format(eauActu),font=("Times",15),tag="eau")
    btnAjoutEau=Button(Plt,text="Ajouter \n de l'eau",background="blue",command=ajt_eau)
    btnAjoutEau.place(x=350,y=250)

    canvaPlt.pack()

def infoplt1(fenetre):
    global eauActu
    eauActu=50
    canva(fenetre,"plante 1",55,50,55,Aplt1)

def infoplt2(fenetre):
    global eauActu
    eauActu=40
    canva(fenetre,"plante 2",55,30,55,Aplt2)

def infoplt3(fenetre):
    global eauActu
    eauActu=55
    canva(fenetre,"plante 3",65,50,55,Aplt3)

def infoplt4(fenetre):
    global eauActu
    eauActu=60
    canva(fenetre,"plante 4",70,60,60,Aplt4)

def infoplt5(fenetre):
    global eauActu
    eauActu=65
    canva(fenetre,"plante 5",70,70,65,Aplt5)

def infoplt6(fenetre):
    global eauActu
    eauActu=60
    canva(fenetre,"plante 6",50,80,60,Aplt6)

def infoplt7(fenetre):
    global eauActu
    eauActu=55
    canva(fenetre,"plante 7",60,50,60,Aplt7)

def infoplt8(fenetre):
    global eauActu
    eauActu=65
    canva(fenetre,"plante 8",60,90,65,Aplt8)

def infoplt9(fenetre):
    global eauActu
    eauActu=70
    canva(fenetre,"plante 9",70,90,70,Aplt9)

def infoplt10(fenetre):
    global eauActu
    eauActu=60
    canva(fenetre,"plante 10",80,60,65,Aplt10)

def infoplt11(fenetre):
    global eauActu
    eauActu=25
    canva(fenetre,"plante 11",95,15,80,Aplt11)

def infoplt12(fenetre):
    global eauActu
    eauActu=75
    canva(fenetre,"plante 12",80,95,75,Aplt12)

def Aplt1():
    FinfoPlantes.plt1(Plt)
def Aplt2():
    FinfoPlantes.plt2(Plt)
def Aplt3():
    FinfoPlantes.plt3(Plt)
def Aplt4():
    FinfoPlantes.plt4(Plt)
def Aplt5():
    FinfoPlantes.plt5(Plt)
def Aplt6():
    FinfoPlantes.plt6(Plt)
def Aplt7():
    FinfoPlantes.plt7(Plt)
def Aplt8():
    FinfoPlantes.plt8(Plt)
def Aplt9():
    FinfoPlantes.plt9(Plt)
def Aplt10():
    FinfoPlantes.plt10(Plt)
def Aplt11():
    FinfoPlantes.plt11(Plt)
def Aplt12():
    FinfoPlantes.plt12(Plt)