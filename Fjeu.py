from tkinter import *
from tkinter import font

def jeu(fenetre):
    
    with open("infos.txt","r") as f:
        bestScore, nomActu,pdpActu=f.readlines()
        bPlayer,bMin, bSec = bestScore.split(" ")
    
    canvaJeu = Canvas(fenetre, width=1300, height=645)
    canvaJeu.imgBG = PhotoImage(file="background.png")
    canvaJeu.create_image(650,322,image=canvaJeu.imgBG)
    canvaJeu.create_rectangle(50,50,200,150,fill="#b4b4b4")#nom du joueur + pdp
    canvaJeu.create_oval(95,55,160,120)
    canvaJeu.create_text(127,135,text=nomActu,font=("Arial",15)) 
    canvaJeu.create_rectangle(250,50,500,150,fill="#b4b4b4")#meilleur score
    canvaJeu.create_text(350,75,text="Meilleur score :",font=("Arial",15))
    canvaJeu.create_text(350,120,text=bPlayer +" : " + bMin+" min "+bSec,font=("Arial",15))
    canvaJeu.create_oval(550,50,850,150,fill="#b4b4b4")#temps
    canvaJeu.create_text(700,100,text="00:00",font=("Arial",50))
    canvaJeu.create_oval(900,50,1000,150,fill="#b4b4b4")#pause
    canvaJeu.create_text(950,100,text="| |",font=("Arial",50))
    canvaJeu.create_rectangle(1050,50,1250,150,fill="#b4b4b4")#comment jouer
    canvaJeu.create_text(1150,60,text="Comment jouer",font=(10))
    canvaJeu.create_text(1150,110,text="?",font=("Arial",50))
    
    def up(event):
        x,y=canvaJeu.coords("perso1")
        if (y-10)>200:
            canvaJeu.move("perso1",0,-10)
    def down(event):
        x,y=canvaJeu.coords("perso1")
        if (y+10)<600:
            canvaJeu.move("perso1",0,10)
    def right(event):
        x,y=canvaJeu.coords("perso1")
        if (x+10)<1200:
            canvaJeu.move("perso1",10,0)
    def left(event):
        x,y=canvaJeu.coords("perso1")
        if (x-10)>50:
            canvaJeu.move("perso1",-10,0)
    
        
    
    canvaJeu.imgPerso=PhotoImage(file="perso 1.png")
    canvaJeu.create_image(650,450,image=canvaJeu.imgPerso,tag="perso1")
    fenetre.bind('<KeyPress-Up>', up)
    fenetre.bind('<KeyPress-Down>', down)
    fenetre.bind('<KeyPress-Right>', right)
    fenetre.bind('<KeyPress-Left>', left)
    
    
    
    canvaJeu.imgPan = PhotoImage(file="panneau.png")
    canvaJeu.create_image(650,225,image=canvaJeu.imgPan)
    
    canvaJeu.pack()
    
    def pause():
        Pause = Toplevel(fenetre)
        
    def coord_souris(event):
        x = event.x
        y = event.y
        if (x>900 and x<1000) and (y>50 and y<150):
            pause()
        if (x>1050 and x<1250) and(y>50 and y<150):
            info()
            
    fenetre.bind('<Button-1>', coord_souris)
