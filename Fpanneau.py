from tkinter import *

def panneau(fenetre):
    Pan=Toplevel(fenetre)
    Pan.focus_set()
    canvaPan= Canvas(Pan,width=700, height=400)
    canvaPan.pack()

    