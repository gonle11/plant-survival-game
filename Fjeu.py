from tkinter import *
from tkinter import font
import Finfo, Fpanneau
def jeu(fenetre,nom,pdp):

    def appel_info():
        Finfo.info(fenetre)
    
    with open("best_score.txt","r") as f:
       bPlayer,bMin, bSec = f.read().split(" ")
    
    #creation du canva + bg
    canvaJeu = Canvas(fenetre, width=1300, height=645)
    canvaJeu.fondBG = PhotoImage(file="fond_lavande.png")
    canvaJeu.create_image(650,322,image=canvaJeu.fondBG)
    canvaJeu.parquetBG = PhotoImage(file="background_fond1.png")
    canvaJeu.create_image(650,322,image=canvaJeu.parquetBG)
    
    #panneau
    canvaJeu.imgPan = PhotoImage(file="panneau.png")
    canvaJeu.create_image(650,225,image=canvaJeu.imgPan)
    def pan(x,y,Dx,Dy):
        x+=Dx
        y+=Dy
        if (x>500 and x<750) and (y>200 and y<300):
            return True

    #nom du joueur + pdp
    canvaJeu.create_rectangle(50,50,200,150,fill="#b4b4b4")
    canvaJeu.create_oval(95,55,160,120)
    canvaJeu.create_text(127,135,text=nom,font=("Arial",15))
    canvaJeu.pdp1=PhotoImage(file="pdp1.png")
    canvaJeu.pdp2=PhotoImage(file="pdp2.png")
    pdps=[canvaJeu.pdp1,canvaJeu.pdp2]
    canvaJeu.create_image(127.5,87.5,image=pdps[pdp])


    #meilleur (score)
    canvaJeu.create_rectangle(250,50,500,150,fill="#b4b4b4")
    canvaJeu.create_text(350,75,text="Meilleur score :",font=("Arial",15))
    canvaJeu.create_text(350,120,text=bPlayer +" : " + bMin+" min "+bSec,font=("Arial",15))

    #temps
    canvaJeu.create_oval(550,50,850,150,fill="#b4b4b4")
    canvaJeu.create_text(700,100,text="00:00",font=("Arial",50))

    #pause
    canvaJeu.create_oval(900,50,1000,150,fill="#b4b4b4")
    canvaJeu.create_text(950,100,text="| |",font=("Arial",50))

    #comment jouer
    btnCommentJouer=Button(fenetre,font=("Arial",30),width="8",text="Comment \n jouer ? ",bg="#b4b4b4",command=appel_info)
    btnCommentJouer.place(x=1050,y=50)
    
    def up(event):
        x,y=canvaJeu.coords("perso1")
        if (y-10)>200 and not pan(x,y,0,-10):
            canvaJeu.move("perso1",0,-10)
        elif pan(x,y,0,-10):
            Fpanneau.panneau()

    def down(event):
        x,y=canvaJeu.coords("perso1")
        if (y+10)<600 and not pan(x,y,0,10):
            canvaJeu.move("perso1",0,10)
        elif pan(x,y,0,10):
            Fpanneau.panneau()

    def right(event):
        x,y=canvaJeu.coords("perso1")
        if (x+10)<1150 and not pan(x,y,10,0):
            canvaJeu.move("perso1",10,0)
        elif pan(x,y,10,0):
            Fpanneau.panneau()

    def left(event):
        x,y=canvaJeu.coords("perso1")
        if (x-10)>150 and not pan(x,y,-10,0):
            canvaJeu.move("perso1",-10,0)
        elif pan(x,y,-10,0):
            Fpanneau.panneau()
        
    
    canvaJeu.imgPerso=PhotoImage(file="perso 1.png")
    canvaJeu.create_image(650,450,image=canvaJeu.imgPerso,tag="perso1")
    fenetre.bind('<KeyPress-Up>', up)
    fenetre.bind('<KeyPress-Down>', down)
    fenetre.bind('<KeyPress-Right>', right)
    fenetre.bind('<KeyPress-Left>', left)
    
    
    canvaJeu.pack()
    
    def pause():
        Pause = Toplevel(fenetre)
        
    def coord_souris(event):
        x = event.x
        y = event.y
        if (x>900 and x<1000) and (y>50 and y<150):
            pause()
        if (x>1050 and x<1250) and(y>50 and y<150):
            appel_info()
            
    fenetre.bind('<Button-1>', coord_souris)


