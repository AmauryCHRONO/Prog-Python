# -*- coding: utf-8 -*-

# Header

"""
Programme secondaire TP3

Réalise le pendu

Amaury CHRONOWSKI

06/12/2021

-------

"""
#Importation de bibliothèques nécessaire
from random import randint
from tkinter import messagebox

def fichiermot():#ouvre un fichier contenant des mots  et en prenrd un au hasrad; rien en entré; donne le mot prie au hasrad;
    listM=[]
    a=""
    file=open("Pendu.txt","r") 
    for line in file:
        listM.append(line[:-1])
    t=len(listM)-1
    ind=randint(0,t)
    a=listM[ind][0]
    for i in range(len(listM[ind])-1):
        a+="_"
    return a,listM[ind]

def rechrechelettre():#cherche les lettre et gère la vie de l'utilisateur; a en entré le mot recherché et le mot qu'on a; et donne en sortie les vies restantes.
     mot,M=fichiermot()
     v=8
     listlettre=[]
     lettre="u"
     while mot!=M:
        if v==0:
            messagebox.shominfo('Jeu du pendu', 'Vous avez perdu')
        if lettre in listlettre:
            print("Vous avez deja utilisé cette lettre")
        else:
            listlettre.append(lettre)
            if M.find(lettre)!=-1 :
                i=0
                for i,le in enumerate(M):
                    if le==lettre:
                        mot=mot[:i]+lettre+mot[i+1:]
                i+=1
            else:
                print("Vous avez perdu une vie")
                v-=1
                print("Vie : "+str(v))
        return v

"""             
def fin(s,v):#gère la fin de partie affiche le score et demande si l'on veut rejouer; a en entré le score actuel et le meilleur scroe des partie précedante; ne retourne rien. 
    if v!=0:
        if s<=v:
            s=v
        print("Vous avez gagné")    
        print(("Vorte score est de "+str(v)))
    h=str(input("Voulez-vous rejouer? (Oui/Non)\n"))
    h.lower()
    if h=="oui":
        Pendu(s)
    else:
        print(("Vorte meilleur score est de "+str(s)))
"""    