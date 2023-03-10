# -*- coding: utf-8 -*-

# Header

"""
Programme secondaire TP2

Réalise la fonction de vérifier une phrase

Amaury CHRONOWSKI

22/11/2021

-------

"""

def Verif(tr,P): #Vérifie si une phrase est grammaticalement correcte, entré matrice de transistion et phrase à vérifié, sorti etat correspondant de la phrase
    E=0
    
    dico=Dico()#le fichier du dictionnaire
    
    P=Decolpoint(P) #permet de traité la phrase qaund le point est collé
            
    P=RemovPonc(P) #enleve les ; ,
    
    P=P.split(' ')#sépare les mots
    
    if '' in P:#enleve les espaces en trop
        P.remove('')
        
    for i in P:#cherche l'état
        if i in dico:
            if i!='' :
                if E!=8:
                    Ind=dico[i]
                    E=tr[E][Ind]
            else:
                return 8
        else:
            return 8
    if E!=9:
        return 8
    return 9


def Dico():#crée le dictionnaire à partir le fichier du dictionnaire, entré rien sortie dictionnaire
    dico={}
    file=open("Dico.txt") 
    for line in file:
        key,value=line.split()
        dico[key]=int(value)
    return dico


def Decolpoint(P):#permet de traité la phrase qaund le point est collé, entré phrase non traité sortie phrase traité
    if P!='':
        if P[-1]=='.':
            P=P[:-1]+" ."
    return P

    
def RemovPonc(P):#enleve les ; , , entré phrase non traité sortie phrase traité
    PL=list(P) 
    P=''
    if ',' in PL:
        PL.remove(',')
    if ';' in PL: 
        PL.remove(';')
    for i in PL:
        P+=i
    return P
    
            
            