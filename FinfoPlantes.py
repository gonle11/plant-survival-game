from tkinter import *
from tkinter import font

def infoPlantes(fenetre):
        InfoPlantes = Toplevel(fenetre, width=800, height=500,background="grey")
        btn1 = Button(InfoPlantes, text="Epipremnum aureum ",command=plt1)
        btn2 = Button(InfoPlantes, text="Sansevieria trifasciata")#,command=plt2)
        btn3 = Button(InfoPlantes, text="Chlorophytum comosum ")#,command=plt3)
        btn4 = Button(InfoPlantes, text="Ficus elastica")#,command=plt4)
        btn5 = Button(InfoPlantes, text="Monstera deliciosa")#,command=plt5)
        btn6 = Button(InfoPlantes, text="Spathiphyllum wallisii")#,command=plt6)
        btn7 = Button(InfoPlantes, text="Dracaena marginata")#,command=plt7)
        btn8 = Button(InfoPlantes, text="Calathea orbifolia")#,command=plt8)
        btn9 = Button(InfoPlantes, text="Alocasia amazonica ")#,command=plt9)
        btn10 = Button(InfoPlantes, text="Ficus lyrata")#,command=plt10)
        btn11= Button(InfoPlantes, text="Cactus ferocactus")#,command=plt11)
        btn12 = Button(InfoPlantes, text="Nepenthes alata ")#,command=plt12)
        btn1.place(x=25,y=25)
        btn2.place(x=50,y=25)
        btn3.place(x=75,y=25)
        btn4.place(x=100,y=25)
        btn5.place(x=125,y=25)
        btn6.place(x=150,y=25)
        btn7.place(x=175,y=25)
        btn8.place(x=200,y=25)
        btn9.place(x=225,y=25)
        btn10.place(x=250,y=25)
        btn11.place(x=275,y=25)
        btn12.place(x=300,y=25)

def plt1():
        print("plt1")