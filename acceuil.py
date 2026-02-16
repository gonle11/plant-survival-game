from tkinter import *
import Fjeu, Finfo,FinfoPlantes



def accueil(fenetre):

    def appel_jeu():
        Fjeu.jeu(fenetre,nom,actu)

    def appel_info():
        Finfo.info(fenetre)
        
    def appel_infoPlantes():
        FinfoPlantes.infoPlantes(fenetre) 
        
    nom=""
    global actu
    with open("best_score.txt","r") as f:
       bPlayer,bMin, bSec = f.read().split(" ")

    def coord_souris(event):
        global actu
        x = event.x
        y = event.y
        if (x>800 and x<1200) and (y>350 and y<700):#"btn" jouer
            canvaAcc.destroy()
            appel_jeu()
        if (x>500 and x<550) and (y>250 and y<350): #skin de gauche
            if actu==0:
                actu=len(skin)-1
            else:
                actu-=1
            canvaAcc.itemconfigure("perso",image=skin[actu])
 
        if (x>700 and x<750) and (y>250 and y<350): #skin de droite
            if actu==(len(skin)-1):
                actu=0
            else:
                actu+=1
            canvaAcc.itemconfigure("perso",image=skin[actu])
 

    def recupNom():
       global nom
       nom=nomDonne.get()
       entreeNom.configure(bg="green")
        
    canvaAcc = Canvas(fenetre, width=1300, height=645)
    canvaAcc.fondBG = PhotoImage(file="fond_lavande.png")
    canvaAcc.create_image(650,322,image=canvaAcc.fondBG)
    canvaAcc.parquetBG = PhotoImage(file="background_fond1.png")
    canvaAcc.create_image(650,322,image=canvaAcc.parquetBG)
    
    # titre
    canvaAcc.create_rectangle(75,50,1200,150, fill="peru")
    canvaAcc.create_text(650,100,text="LE JEU DES PLANTES",font=("times",75,"bold"))
    
    #meilleur temps
    canvaAcc.create_rectangle(100,200,400,400,fill="peru")
    canvaAcc.create_text(250,250,text="Meilleur temps :",font=("times",30))
    canvaAcc.create_text(250,315,text=bPlayer,font=("times",40))
    canvaAcc.create_text(250,375,text=bMin + " min "+ bSec,font=("times",40))
    
    #info plantes
    btnInfoPlantes=Button(fenetre,font=("Arial",30),width="15",text="Infos \n sur \n les plantes",bg="peru",command=appel_infoPlantes)
    btnInfoPlantes.place(x=100,y=450)
    
    #Comment jouer
    btnCommentJouer=Button(fenetre,font=("Arial",30),width="15",text="Comment \n jouer ?",bg="peru",command=appel_info)
    btnCommentJouer.place(x=900,y=200)
    
    #Jouer
    canvaAcc.create_text(1050,550,text="Jouer",font=("times",125))
    
    #bonhomme + nom
    canvaAcc.create_oval(500,425,800,525,fill="red")
    canvaAcc.imgPerso1 = PhotoImage(file="bonhomme1.png")
    canvaAcc.imgPerso2 = PhotoImage(file="bonhomme2.png")
    skin=[canvaAcc.imgPerso1,canvaAcc.imgPerso2]
    actu=0
    canvaAcc.create_image(600,200, anchor='nw',image=canvaAcc.imgPerso1,tag="perso")
    canvaAcc.create_polygon((500,300),(550,250),(550,350))
    canvaAcc.create_polygon((700,350),(700,250),(750,300))
    nomDonne=StringVar()
    entreeNom=Entry(fenetre, width=10,font=("Arial",25),textvariable=nomDonne) #input du nom
    entreeNom.place(x=500,y=550)
    btnValiderNom=Button(fenetre,text="Valider",font=("Arial",15),command=recupNom)
    btnValiderNom.place(x=700,y=550)
    
    canvaAcc.pack()
          
    fenetre.bind('<Button-1>', coord_souris)

    
    



    
#accueil()
