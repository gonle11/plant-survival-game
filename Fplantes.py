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
    canva(plt2,"Plante 2")
    tab(plt2,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')


def plante3(Pan):
    plt3=Toplevel(Pan)
    canva(plt3,"Plante 3")
    tab(plt3,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

    
def plante4(Pan):
    plt4=Toplevel(Pan)
    canva(plt4,"Plante 4")
    tab(plt4,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')


def plante5(Pan):
    plt5=Toplevel(Pan)
    canva(plt5,"Plante 5")
    tab(plt5,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

    
def plante6(Pan):
    plt6=Toplevel(Pan)
    canva(plt6,"Plante 6")
    tab(plt6,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante7(Pan):
    plt7=Toplevel(Pan)
    canva(plt7,"Plante 7")
    tab(plt7,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

    
def plante8(Pan):
    plt8=Toplevel(Pan)
    canva(plt8,"Plante 8")
    tab(plt8,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')


def plante9(Pan):
    plt9=Toplevel(Pan)
    canva(plt9,"Plante 9")
    tab(plt9,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')
    
def plante10(Pan):
    plt10=Toplevel(Pan)
    canva(plt10,"Plante 10")
    tab(plt10,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')

def plante11(Pan):
    plt11=Toplevel(Pan)
    canva(plt11,"Plante 11")
    tab(plt11,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')
    
def plante12(Pan):
    plt12=Toplevel(Pan)
    canva(plt12,"Plante 12")
    tab(plt12,'1/1','1/2','1/3','1/4','2/1','2/2','2/3','2/4','3/1','3/2','3/3','3/4')
