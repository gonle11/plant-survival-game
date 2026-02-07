from tkinter import *
from tkinter import font

def info(fenetre):
    Info = Toplevel(fenetre)
    canvaInfo = Canvas(Info, width=700, height=400)
    canvaInfo.bg=PhotoImage(file="fondInfo.png")
    canvaInfo.create_image(350,200,image=canvaInfo.bg)
    canvaInfo.create_text(350,30,text="Regles du jeu :",font=("Times",50))
    canvaInfo.create_text(400,200,font=("Times",15),text="- tu dois t'occuper de plantes qui apparaissent dans ton salon \n- tu peux de déplacer dans ton salon en appuyant \n                   sur les touches ↑ ↓ ← → \n - quand tu t'approches des plantes, tu peux modifier ses réglages \n - quand tu t'approches du tableau, tu peux voir \n                  les meilleurs réglages pour chacune des plantes \n - si une plante reste trop longtemps avec des mauvais réglages, \n                        elle meurt \n - lorsque toutes tes plantes sont mortes, tu as perdu ! ")
    canvaInfo.create_text(400,345,font=("Times",25),text=" Bon courage et prend bien soin de tes plantes !")
    canvaInfo.pack()