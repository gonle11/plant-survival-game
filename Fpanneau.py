from tkinter import *

def panneau(fenetre):
    Pan=Toplevel(fenetre)
    Pan.focus_set()
    canvaPan= Canvas(Pan,width=700, height=500)
    canvaPan.bg=PhotoImage(file="bgpanneau.png")
    canvaPan.create_image(350,250,image=canvaPan.bg)
    canvaPan.create_text(350,35,text="Plantes",font=("Times",50))
    
    btn1=Button(Pan,text="1",font=("Arial",15),background="#b4b4b4",image="plante1.png")#,command=plante1)
    btn1.place(x=75,y=75)

    #canvaPan.create_rectangle(75,75,175,175,fill="#b4b4b4")
    canvaPan.create_rectangle(215,75,315,175,fill="#b4b4b4")
    canvaPan.create_rectangle(355,75,455,175,fill="#b4b4b4")
    canvaPan.create_rectangle(495,75,595,175,fill="#b4b4b4")
    canvaPan.create_rectangle(75,200,175,300,fill="#b4b4b4")
    canvaPan.create_rectangle(215,200,315,300,fill="#b4b4b4")
    canvaPan.create_rectangle(355,200,455,300,fill="#b4b4b4")
    canvaPan.create_rectangle(495,200,595,300,fill="#b4b4b4")
    canvaPan.create_rectangle(75,325,175,425,fill="#b4b4b4")
    canvaPan.create_rectangle(215,325,315,425,fill="#b4b4b4")
    canvaPan.create_rectangle(355,325,455,425,fill="#b4b4b4")
    canvaPan.create_rectangle(495,325,595,425,fill="#b4b4b4")
    canvaPan.pack()

    