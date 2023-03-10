#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:02:16 2021

@author: amaury.chronowski
"""

from tkinter import Tk, Label, Button, Entry, Canvas, StringVar,PhotoImage,messagebox
import tkinter as tk


class Pendu(tk.Tk):
    def __init__(self,M,mot,s=0):
        super().__init__()
        self.M=M
        self.mot=mot
        self.s=s
        self.v=8
        self.listlet=[]
        self.title("Jeu du pendu")

        imgbon=PhotoImage(file="images_PENDU/bonhomme1.gif")
        l=300
        h=300
        self.bon=Canvas(self,width=l,height=h)
        self.item=self.bon.create_image(l/2,h/2,image=imgbon)
        self.bon.pack(side="right",padx=10,pady=10)

        self.MOT=Label(self,text=self.mot)
        self.MOT.pack(anchor="nw", padx=10,pady=10)

        self.info=Label(self,text='')
        self.info.pack(padx=10,pady=10)

        self.Lettre=StringVar()
        self.let=Entry(self,textvariable=self.Lettre,show="Choirsir une lettre")
        self.let.focus_set()
        self.let.pack(side="left",padx=5,pady=5)
            
        self.Buntonsoumettre=Button(self, text="Proposer", command=self.recherchelettre())
        self.Buntonsoumettre.pack(side="right",padx=10,pady=10)
        
        
    def recherchelettre(self):
        while self.mot!=self.M:
            self.info['text'] =""
            self.l=self.Lettre.get()
            if self.v==0:
                messagebox.showinfo('Jeu du pendu', 'Vous avez perdu')
            if self.l in self.listlet:
                self.info['text'] = "Vous avez deja utilisé cette lettre"
            else:
                self.listlet.append(self.l)
                if self.M.find(self.l)!=-1 :
                    i=0
                    for i,le in enumerate(self.M):
                        if le==self.l:
                            self.mot=self.mot[:i]+self.l+self.mot[i+1:]
                            self.MOT['text'] = self.mot
                    i+=1
                else:
                    self.v-=1
                    self.info['text'] = "Vous avez perdu une vie ("+self.v+")"
                    self.bon.itemconfig(self.item, image = "images_PENDU/bonhomme"+str(9-self.v)+".gif")

        self.info['text'] = "Vous avez gagner" 
