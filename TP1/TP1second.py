# -*- coding: utf-8 -*-

# Header

"""
Programme secondaire TP1

Amaury CHRONOWSKI

15/11/2021

-------

"""

#Importation de bibliothèques nécessaires


#Progrmme secondaire
def AnneeBiss(An): #Vériffie que l'année est bissextile, à besoin de l'année en int et retourne si elle l'est ou pas
    if An%4==0 or An%400==0 or An%100==0:
        return True
    return False

def NbJourMois(M,An): #Donne le nombre de jour qu'a un mois de l'année, à besonde l'année en int et du numéro du mois en int et retourne le nombre de jour du mois en int
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        return 31 
    elif M==4 or M==6 or M==9 or M==11:
        return 30 
    elif M==2 and AnneeBiss(An):
        return 29 
    return 28 

def DateValide(D): #Vérifie si un date est valide, a besoin d'une date sous la forme DD/MM/AAAA en str et retourne vrai si la date est bonne faux si la date est fausse
    Dt=D.split('/')
    DJ=int(Dt[0])
    DM=int(Dt[1])
    DA=int(Dt[2])
    if DM<=12:
        J=NbJourMois(DM,DA)
        if DJ<=J:
            return 'Date valide'
        
    return 'Date non valide'

def SaisieD():
    D=str(input('Veulliez rentrer votre date(JJ/MM/AAAA):\n'))
    print(DateValide(D))
    
def mesImpots(revenu):
    R=revenu
    if R<=10084:
        print('Vous payez ',0,"€ d'impôt")
        return 0
    elif R<=25710 and R>10084:
        t=((R-10085)*0.11)
        print('Vous payez ',t,"€ d'impôt")
        return t
    elif R<=73516 and R>25710:
        t=((R-25711)*0.3)+((25710-10084)*0.11)
        print('Vous payez ',t,"€ d'impôt")
        return t
    elif R<=158122 and R>73516:
        t=(R-73517)*0.41+((73516-25710)*0.3)+((25710-10084)*0.11)
        print('Vous payez ',t,"€ d'impôt")
        return t
    elif R>158122:
        t=((R-158123)*0.45)+((158122-73517)*0.41)+((73516-25710)*0.3)+((25710-10084)*0.11)
        print('Vous payez ',t,"€ d'impôt")
        return t
    
def multiplication(A,B):
    m=[]
    if len(B[0])!=len(A):
        print('Erreur de dimension')
        return
    for i in range(len(A)):
        ligne=[]
        for j in range(len(B[0])):
            c=0
            for k in range(len(A[0])):
                c+=A[i][k]*B[k][j]
            ligne.append(c)
        m.append(ligne)
    print(m)
    
def Hanoi(n , A, B, C):
    if n==1:
        print("Disk 1 from",A,"to",B)
        print((2^n)-1)
        return 
    Hanoi(n-1, A, C, B)
    print("Disk",n,"from",A,"to",B)
    Hanoi(n-1, C, B, A)
    
          
def Syracuse(n,p=0,i=0):
    if n==1:
        return p,i
    if n%2==0:
        n=n/2
        i+=1
        p,i = Syracuse(n,p,i)
    else:
        n=(3*n)+1
        if p<n:
            p=n
        i+=1
        p,i = Syracuse(n,p,i)
    return p,i
        
def SyracuseVolPicM(n):
    p=0
    h=0
    for i in range(2,1000):
        u,v=Syracuse(i)
        if u>p:
            p=u
            ip=i
        if v>h:
            h=v
            iv=i
    print(iv)
    print(h)
    print(ip)
    print(p)

        
        
        
        
def tricolore(n):
    a=str(n*n)
    for i in a:
        if i!="1" and i!="4" and i!="9":
            return False
    return True
    
def tous_les_tricolores(n):
    m=0
    for i in range(n+1):
        if (tricolore(i)):
            m+=1
            print(i)
    print(m)
            
def NbAmicaux(a,b):
    n=1
    m=1
    i=0
    j=0
    while n<=a:
        if a%n==0:
            i+=n
        n+=1
    while m<=b:
        if b%m==0:
            j+=m
        m+=1
    if i==j and i==(a+b) and j==(a+b):
        print("ce sont des nombres amicaux")
        return
    print("ce ne sont pas des nombres amicaux")
    return
    
    
            
    
            
        
    
        
 
    
            
            
            
            
        

    
    