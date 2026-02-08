from tkinter import *
import Fplantes

def panneau(fenetre):
    Pan=Toplevel(fenetre)
    Pan.focus_set()
    canvaPan= Canvas(Pan,width=700, height=500)
    canvaPan.bg=PhotoImage(file="bgpanneau.png")
    canvaPan.create_image(350,250,image=canvaPan.bg)
    canvaPan.create_text(350,35,text="Plantes",font=("Times",50))
    
    #plante 1
    def appel_plante1():
        Fplantes.plante1(Pan)
    canvaPan.plante1=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante1,command=appel_plante1)
    btn1.place(x=75,y=75)
    

    #plante 2
    def appel_plante2():
        Fplantes.plante2(Pan)
    canvaPan.plante2=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante2,command=appel_plante2)
    btn1.place(x=215,y=75)

    #plante 3
    def appel_plante3():
        Fplantes.plante3(Pan)
    canvaPan.plante3=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante3, command=appel_plante3)
    btn1.place(x=355,y=75)

    #plante 4
    def appel_plante4():
        Fplantes.plante4(Pan)
    canvaPan.plante4=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante4,command=appel_plante4)
    btn1.place(x=495,y=75)

    #plante 5
    def appel_plante5():
        Fplantes.plante5(Pan)
    canvaPan.plante5=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante5,command=appel_plante5)
    btn1.place(x=75,y=200)

    #plante 6
    def appel_plante6():
        Fplantes.plante6(Pan)
    canvaPan.plante6=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante6,command=appel_plante6)
    btn1.place(x=215,y=200)

    #plante 7
    def appel_plante7():
        Fplantes.plante7(Pan)
    canvaPan.plante7=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante7,command=appel_plante7)
    btn1.place(x=355,y=200)

    #plante 8
    def appel_plante8():
        Fplantes.plante8(Pan)
    canvaPan.plante8=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante8,command=appel_plante8)
    btn1.place(x=495,y=200)

    #plante 9
    def appel_plante9():
        Fplantes.plante9(Pan)
    canvaPan.plante9=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante9,command=appel_plante9)
    btn1.place(x=75,y=325)

    #plante 10
    def appel_plante10():
        Fplantes.plante10(Pan)
    canvaPan.plante10=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante10,command=appel_plante10)
    btn1.place(x=215,y=325)

    #plante 11
    def appel_plante11():
        Fplantes.plante11(Pan)
    canvaPan.plante11=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante11,command=appel_plante11)
    btn1.place(x=355,y=325)
    
    #plante 12
    def appel_plante12():
        Fplantes.plante12(Pan)
    canvaPan.plante12=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante12,command=appel_plante12)
    btn1.place(x=495,y=325)

    canvaPan.pack()

    