from tkinter import *

def panneau(fenetre):
    Pan=Toplevel(fenetre)
    Pan.focus_set()
    canvaPan= Canvas(Pan,width=700, height=500)
    canvaPan.bg=PhotoImage(file="bgpanneau.png")
    canvaPan.create_image(350,250,image=canvaPan.bg)
    canvaPan.create_text(350,35,text="Plantes",font=("Times",50))
    
    #plante 1
    canvaPan.plante1=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante1)#,command=plante1)
    btn1.place(x=75,y=75)

    #plante 2
    canvaPan.plante2=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante2)#,command=plante1)
    btn1.place(x=215,y=75)

    #plante 3
    canvaPan.plante3=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante3)#,command=plante1)
    btn1.place(x=355,y=75)

    #plante 4
    canvaPan.plante4=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante4)#,command=plante1)
    btn1.place(x=495,y=75)

    #plante 5
    canvaPan.plante5=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante5)#,command=plante1)
    btn1.place(x=75,y=200)

    #plante 6
    canvaPan.plante6=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante6)#,command=plante1)
    btn1.place(x=215,y=200)

    #plante 7
    canvaPan.plante7=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante7)#,command=plante1)
    btn1.place(x=355,y=200)

    #plante 8
    canvaPan.plante8=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante8)#,command=plante1)
    btn1.place(x=495,y=200)

    #plante 9
    canvaPan.plante9=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante9)#,command=plante1)
    btn1.place(x=75,y=325)

    #plante 10
    canvaPan.plante10=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante10)#,command=plante1)
    btn1.place(x=215,y=325)

    #plante 11
    canvaPan.plante11=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante11)#,command=plante1)
    btn1.place(x=355,y=325)
    
    #plante 12
    canvaPan.plante12=PhotoImage(file="plante1.png")
    btn1=Button(Pan,font=("Arial",15),image=canvaPan.plante12)#,command=plante1)
    btn1.place(x=495,y=325)

    canvaPan.pack()

    