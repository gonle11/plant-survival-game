from tkinter import *
from tkinter import font

def infoPlantes(fenetre):

        def plt1():
                InfoP1= Toplevel(InfoPlantes, width=600, height=400)
                canva1=Canvas(InfoP1,width=600,height=400,background="#b4b4b4")
                canva1.create_text(300,30,text="Epipremnum aureum ", font=("Times",50))
                canva1.create_text(315,150,text="L’Epipremnum aureum, ou Pothos ou Scindapsus doré est une espèce \n de plantes à fleurs de la famille des Aracées. Elle est originaire de       \n Polynésie française. C’est une plante grimpante qui s’accroche aux      \n troncs d’arbre et aux rochers grâce à ses racines aérienne. C’est une       \n plante sempervirente. Elle est beaucoup cultivée comme plante       \n d’intérieur comme dans le jeu ! ", font=("Times",15))
                canva1.create_rectangle(25,250,375,350,fill="#C98E26")
                canva1.create_text(150,275,text="Le saviez-vous ? ",font=("Times",25))
                canva1.create_text(200,325,font=("Times",10),text="L’épithète spécifique aureum de son nom latin vient du latin \n aurĕus, a, um qui signifie « doré, de couleur d’or » par \n allusion aux mouchetures jaunes des feuilles d’une variété ")
                canva1.img=PhotoImage(file="Epipremnum_aureum.png")
                canva1.create_image(485,300,image=canva1.img)
                canva1.pack()

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
        btn2.place(x=25,y=50)
        btn3.place(x=25,y=75)
        btn4.place(x=25,y=100)
        btn5.place(x=25,y=125)
        btn6.place(x=25,y=150)
        btn7.place(x=25,y=175)
        btn8.place(x=25,y=200)
        btn9.place(x=25,y=225)
        btn10.place(x=25,y=250)
        btn11.place(x=25,y=275)
        btn12.place(x=25,y=300)

