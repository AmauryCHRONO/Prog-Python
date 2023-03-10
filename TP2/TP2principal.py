# -*- coding: utf-8 -*-

# Header

"""
Programme principale TP2

Donne une phrase à vérifier

Amaury CHRONOWSKI

22/11/2021

-------

"""
#Importation de bibliothèques nécessaire

import TP2scondaire

#Variables
transition=((1,8,8,8,4,8),
            (8,1,2,8,8,8),
            (8,2,8,3,8,8),
            (5,8,8,8,7,9),
            (8,8,8,3,8,8),
            (8,5,6,8,8,8),
            (8,6,8,8,8,9),
            (8,8,8,8,8,9))

#Phrase=str(input("Veuillez saisir votre phrase :\n"))
Phrase1="le joli chat joue."
Phrase2="la verte souris grosse petite mange le blanc verte chat petit."
Phrase3="le joli chat joue" 
Phrase4="."
Phrase5="" 
Phrase6="Jean joue ."
Phrase7="Jean mange Martin."
Phrase8="le ,joli chat ; joue." 

#Programme principale

print("Etat "+str(TP2scondaire.Verif(transition,Phrase1)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase2)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase3)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase4)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase5)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase6)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase7)))
print("Etat "+str(TP2scondaire.Verif(transition,Phrase8)))
