from tkinter import *

def infoplt1(fenetre):
    Plt=Toplevel(fenetre,width=500,height=500)
    canvaPlt=Canvas(Plt,width=500,height=300)
    canvaPlt.bg=PhotoImage(file="bgpanneau.png")
    canvaPlt.create_image(350,250,image=canvaPlt.bg)

    
    valueHum = IntVar()
    scaleHum=Scrollbar(Plt,orient=HORIZONTAL,bg="peru")
    Humid=valueHum.get()
    scaleHum.place(x=25,y=25)

    valueLum = DoubleVar()
    scaleLum=Scrollbar(Plt)
    scaleLum.pack(anchor=CENTER)#lace(x=25,y=50)

    valueChal = DoubleVar()
    scaleChal=Scrollbar(Plt)
    scaleChal.pack()#lace(x=25,y=75)

    canvaPlt.pack()