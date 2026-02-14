from tkinter import *
from tkinter import font
import Finfo, Fpanneau, Finfoplt

def jeu(fenetre,nom,pdp):
    global tempsEcoule

    def appel_info():
        Finfo.info(fenetre)
    
    def appel_infoplt1():
        Finfoplt.infoplt1(fenetre)
    def appel_infoplt2():
        Finfoplt.infoplt2(fenetre)
    def appel_infoplt3():
        Finfoplt.infoplt3(fenetre)
    def appel_infoplt4():
        Finfoplt.infoplt4(fenetre)
    def appel_infoplt5():
        Finfoplt.infoplt5(fenetre)
    def appel_infoplt6():
        Finfoplt.infoplt6(fenetre)
    def appel_infoplt7():
        Finfoplt.infoplt7(fenetre)
    def appel_infoplt8():
        Finfoplt.infoplt8(fenetre)
    def appel_infoplt9():
        Finfoplt.infoplt9(fenetre)
    def appel_infoplt10():
        Finfoplt.infoplt10(fenetre)
    def appel_infoplt11():
        Finfoplt.infoplt11(fenetre)
    def appel_infoplt12():
        Finfoplt.infoplt12(fenetre)
    
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
    def mettreAJourTimer():
        global tempsEcoule
        tempsEcoule += 1
        min=tempsEcoule//60
        sec=tempsEcoule%60
        
        canvaJeu.itemconfig("timer",text=f"{min:02d}:{sec:02d}")
        fenetre.after(1000, mettreAJourTimer)
    
    canvaJeu.create_oval(550,50,850,150,fill="#b4b4b4")
    canvaJeu.create_text(700,100,text="00:00",font=("Arial",50),tag="timer")
    tempsEcoule=0
    mettreAJourTimer()
    


    #pause
    canvaJeu.create_oval(900,50,1000,150,fill="#b4b4b4")
    canvaJeu.create_text(950,100,text="| |",font=("Arial",50))

    #comment jouer
    btnCommentJouer=Button(fenetre,font=("Arial",30),width="8",text="Comment \n jouer ? ",bg="#b4b4b4",command=appel_info)
    btnCommentJouer.place(x=1050,y=50)

    #plante1
    canvaJeu.plt1=PhotoImage(file="top-view_1.png")
    canvaJeu.create_image(1100,250,image=canvaJeu.plt1)
    btnplt1=Button(fenetre,font=("Arial",10),width="15",text="Epipremnum aureum \n Niveau 1",bg="peru",command=appel_infoplt1)
    btnplt1.place(x=1050,y=300)
    
    #plante2
    canvaJeu.plt2=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(1100,400,image=canvaJeu.plt2)
    btnplt2=Button(fenetre,font=("Arial",10),width="15",text="plante2 \n Niveau 1",bg="peru",command=appel_infoplt2)
    btnplt2.place(x=1050,y=450)

    #plante3
    canvaJeu.plt3=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(1100,550,image=canvaJeu.plt3)
    btnplt3=Button(fenetre,font=("Arial",10),width="15",text="plante3 \n Niveau 1",bg="peru",command=appel_infoplt3)
    btnplt3.place(x=1050,y=600)

    #plante4
    canvaJeu.plt4=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(230,250,image=canvaJeu.plt4)
    btnplt4=Button(fenetre,font=("Arial",10),width="15",text="plante4 \n Niveau 1",bg="peru",command=appel_infoplt4)
    btnplt4.place(x=180,y=300)
    
    #plante5
    canvaJeu.plt5=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(230,400,image=canvaJeu.plt5)
    btnplt5=Button(fenetre,font=("Arial",10),width="15",text="plante5 \n Niveau 1",bg="peru",command=appel_infoplt5)
    btnplt5.place(x=180,y=450)

    #plante6
    canvaJeu.plt6=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(230,550,image=canvaJeu.plt6)
    btnplt6=Button(fenetre,font=("Arial",10),width="15",text="plante6 \n Niveau 1",bg="peru",command=appel_infoplt6)
    btnplt6.place(x=180,y=600)
    
    #plante7
    canvaJeu.plt7=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(725,600,image=canvaJeu.plt7)
    btnplt7=Button(fenetre,font=("Arial",10),width="15",text="plante7 \n Niveau 1",bg="peru",command=appel_infoplt7)
    btnplt7.place(x=675,y=500)

    #plante8
    canvaJeu.plt8=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(575,600,image=canvaJeu.plt8)
    btnplt8=Button(fenetre,font=("Arial",10),width="15",text="plante8 \n Niveau 1",bg="peru",command=appel_infoplt8)
    btnplt8.place(x=525,y=500)

    #plante9
    canvaJeu.plt9=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(450,250,image=canvaJeu.plt9)
    btnplt9=Button(fenetre,font=("Arial",10),width="15",text="plante9 \n Niveau 1",bg="peru",command=appel_infoplt9)
    btnplt9.place(x=400,y=300)

    #plante10
    canvaJeu.plt10=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(850,250,image=canvaJeu.plt10)
    btnplt10=Button(fenetre,font=("Arial",10),width="15",text="plante10 \n Niveau 1",bg="peru",command=appel_infoplt10)
    btnplt10.place(x=800,y=300)

    #plante11
    canvaJeu.plt11=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(900,600,image=canvaJeu.plt11)
    btnplt11=Button(fenetre,font=("Arial",10),width="15",text="plante11 \n Niveau 1",bg="peru",command=appel_infoplt11)
    btnplt11.place(x=850,y=500)

    #plante8
    canvaJeu.plt12=PhotoImage(file="top-view_1.png")##
    canvaJeu.create_image(400,600,image=canvaJeu.plt12)
    btnplt12=Button(fenetre,font=("Arial",10),width="15",text="plante12\n Niveau 1",bg="peru",command=appel_infoplt12)
    btnplt12.place(x=350,y=500)

    def up(event):
        x,y=canvaJeu.coords("perso1")
        if (y-10)>200 and not pan(x,y,0,-10):
            canvaJeu.move("perso1",0,-10)
        elif pan(x,y,0,-10) :
            Fpanneau.panneau(fenetre)

    def down(event):
        x,y=canvaJeu.coords("perso1")
        if (y+10)<600 and not pan(x,y,0,10):
            canvaJeu.move("perso1",0,10)
        elif pan(x,y,0,10):
            Fpanneau.panneau(fenetre)

    def right(event):
        x,y=canvaJeu.coords("perso1")
        if (x+10)<1150 and not pan(x,y,10,0):
            canvaJeu.move("perso1",10,0)
        elif pan(x,y,10,0) :
            Fpanneau.panneau(fenetre)

    def left(event):
        x,y=canvaJeu.coords("perso1")
        if (x-10)>150 and not pan(x,y,-10,0):
            canvaJeu.move("perso1",-10,0)
        elif pan(x,y,-10,0):
            Fpanneau.panneau(fenetre)
        
    
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


