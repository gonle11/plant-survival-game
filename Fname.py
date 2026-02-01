from tkinter import *
from tkinter import font

def name(fenetre):
    """
    fenêtre qui s'ouvre pour changer son nom et sa pdp
    """
    nomDonne=StringVar()
    
    def recupNom():
        """
        pour recuperer le nom de l'input et le mettre dans le fichier
        """
        nom=nomDonne.get()
        with open("infos.txt","r") as f:
            """
            recuperer les données du fichier
            """
            bestScore, nomActu,pdpActu=f.readlines()
                        
        with open("infos.txt","w") as f:
            """
            réecrire le fichier
            """
            f.write(bestScore)
            f.write(nom)
            f.write("\n")
            f.write(pdpActu)
        Name.destroy()
         
    Name= Toplevel(fenetre) #créer la fenêtre
    canvaName = Canvas(Name, width=700, height=400,background="peru")
    fontCheque = font.Font(family="Cheque",size=80)
    canvaName.create_text(350,50,text="Nom",font=fontCheque) #titre - NOM
    canvaName.create_oval(100,125,250,275)# pdp
    canvaName.create_text(175,300,text="Choisir",font=("Times",20))
    canvaName.create_text(200,350,text="votre photo de profil",font=("Times",20))
    canvaName.create_text(500,175,text="Entrer votre nom",font=("Times",30))
    entreeNom=Entry(Name, width=10,font=("Arial",25),textvariable=nomDonne) #input du nom
    entreeNom.place(x=375,y=225)
    valider=Button(Name,text="Valider",command=recupNom) #bouton pour lancer la récuperation du nom
    valider.place(x=565,y=235)
    canvaName.pack()
    
    def pdp():
        Pdp = Toplevel(Name)
        canvaPdp = Canvas(Pdp, width=500,height=200)
        canvaPdp.create_oval(50,50,150,150)
        canvaPdp.create_oval(200,50,300,150)
        canvaPdp.create_oval(350,50,450,150)
        canvaPdp.pack()
        
        def numeroPdp(event):
            x = event.x
            y = event.y
            with open("infos.txt","r") as f:
                bestScore, nomActu,pdpActu=f.readlines()
            if (x>50 and x<150) and (y>50 and y<150):
                pdpChoisi="1"
            if (x>200 and x<300) and (y>50 and y<150):
                pdpChoisi="2"
            if (x>350 and x<450) and (y>50 and y<150):
                pdpChoisi="3"
            with open("infos.txt","w") as f:
                f.write(bestScore)
                f.write(nomActu)
                f.write(pdpChoisi)
            Pdp.destroy()    
        Pdp.bind('<Button-1>', numeroPdp)
    
    
    def choisirPdp(event):
        x = event.x
        y = event.y
        if (x>100 and x<250) and (y>125 and y<275):
            pdp()
            
    Name.bind('<Button-1>', choisirPdp)
