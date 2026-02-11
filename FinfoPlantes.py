from tkinter import *
from tkinter import font

def infoPlantes(fenetre):
        InfoPlantes = Toplevel(fenetre, width=800, height=500,background="grey")
        btn1 = Button(InfoPlantes, text="Epipremnum aureum ",command=plt1)
        btn1.place(x=25,y=25)

def plt1():
        print("plt1")