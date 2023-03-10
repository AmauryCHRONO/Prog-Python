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
from tkinter import Tk, Frame, Label, Button, Entry, Canvas

def Pendu(s=0):#réalise le pendu;a en entré le score de la meilleurpartie précédante; retourne rien. 
    print("Bienvenue sur le jeu du pendu.\nVeuillez choisir une lettre :")
    M=str(fichiermot())
    mot=M[0]
    for i in range(len(M)-1):
        mot+="_"
    v=rechrechelettre(mot,M)
    fin(s,v)      

        

    
def fichiermot():#ouvre un fichier contenant des mots  et en prenrd un au hasrad; rien en entré; donne le mot prie au hasrad;
    listM=[]
    file=open("Pendu.txt","r") 
    for line in file:
        listM.append(line[:-1])
    t=len(listM)-1
    ind=randint(0,t)
    return listM[ind]

def rechrechelettre(mot,M):#cherche les lettre et gère la vie de l'utilisateur; a en entré le mot recherché et le mot qu'on a; et donne en sortie les vies restantes.
    listlettre=[] 
    v=8
    while mot!=M:
        if v==0:
            print("Vous avez perdu")
            return v
        print(mot)
        lettre=str(input("Votre lettre :\n"))
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
    