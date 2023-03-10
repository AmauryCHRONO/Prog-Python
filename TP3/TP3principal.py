# -*- coding: utf-8 -*-

# Header

"""
Programme principale TP3

Donne Commence une partie de pandu

Amaury CHRONOWSKI

06/12/2021

to do
finir tkinter

-------

"""
#Importation de bibliothèques nécessaire

import TP3secondaire3
import TP3secondaire2
from tkinter import Tk, Label, Button, Entry, Canvas, StringVar,PhotoImage,messagebox

#Variables
mot,M=TP3secondaire2.fichiermot()

"""
if __name__ == "__main__":
    app = TP3secondaire3.Pendu(M,mot)
    app.mainloop()
    
"""
v=8 

Fene=Tk()
Fene.title("Jeu du pendu")

imbon=PhotoImage(file="images_PENDU/bonhomme1.gif")
l=300
h=300
bon=Canvas(Fene,width=l,height=h)
item=bon.create_image(l/2,h/2,image=imbon)
bon.pack(side="right",padx=10,pady=10)

MOT=Label(Fene,text=mot)
MOT.pack(anchor="nw", padx=10,pady=10)

info=Label(Fene,text='')
MOT.pack(padx=10,pady=10)

Lettre=StringVar()
propolet=Entry(Fene,textvariable=Lettre,show="Choirsir une lettre")
propolet.focus_set()
propolet.pack(side="left",padx=5,pady=5)
    
Buntonsoumettre=Button(Fene, text="Proposer")
Buntonsoumettre.pack(side="right",padx=10,pady=10)
    

Fene.mainloop()
