from random import *
from math import *
from tkinter import *
from time import *
Fenetre_Principale=Tk()
Fenetre_Principale.title("Fourmi de Langton")

Liste_rectangle=[]
grille=Canvas(Fenetre_Principale,height=800,width=1600)
grille.grid(row=0,column=0)
for i in range(0,1601,10):
    Liste_rectangle.append([])
    for j in range(0,801,10):
        Liste_rectangle[int(i/10)].append(grille.create_rectangle(i,j,i+10,j+10,outline="blue",fill='red'))

def affichage(grille,Déplacement_fourmi,Couleur_case):
    Vecteur=[Déplacement_fourmi[1][0]-Déplacement_fourmi[0][0],Déplacement_fourmi[1][1]-Déplacement_fourmi[0][1]]
    if Couleur_case[0]=='black':
        if Vecteur[0]==0:
            Déplacement_fourmi.append([Déplacement_fourmi[1][0]-Vecteur[1],Déplacement_fourmi[1][1]])
        else:
            Déplacement_fourmi.append([Déplacement_fourmi[1][0],Déplacement_fourmi[1][1]+Vecteur[0]])
    else:
        if Vecteur[0]==0:
            Déplacement_fourmi.append([Déplacement_fourmi[1][0]+Vecteur[1],Déplacement_fourmi[1][1]])
        else:
            Déplacement_fourmi.append([Déplacement_fourmi[1][0],Déplacement_fourmi[1][1]-Vecteur[0]])
    del(Déplacement_fourmi[0])
    if grille.itemcget(Liste_rectangle[Déplacement_fourmi[1][0]][Déplacement_fourmi[1][1]],"fill")=="black":
        Couleur_case.append("white")
    else:
        Couleur_case.append("black")
    grille.itemconfigure(Liste_rectangle[Déplacement_fourmi[0][0]][Déplacement_fourmi[0][1]],fill=Couleur_case[0])    
    del(Couleur_case[0])
    grille.itemconfigure(Liste_rectangle[Déplacement_fourmi[1][0]][Déplacement_fourmi[1][1]],fill="blue")
    grille.update_idletasks()
    grille.after(1,lambda Déplacement_fourmi=Déplacement_fourmi,Couleur_case=Couleur_case:affichage(grille,Déplacement_fourmi,Couleur_case))
            
def debut(event,Liste_rectangle,Liste_fourmis):
    grille.unbind("<Motion>")
    grille.unbind("<ButtonRelease-1>")
    Dép=[[0,-1],[0,1],[-1,0],[1,0]]
    a=randint(0,3)
    sleep(0.1)
    grille.itemconfigure(Liste_rectangle[Liste_fourmis[0]][Liste_fourmis[1]],fill="black")
    grille.itemconfigure(Liste_rectangle[Dép[a][0]+Liste_fourmis[0]][Dép[a][1]+Liste_fourmis[1]],fill="blue")
    Déplacement_fourmi=[[Liste_fourmis[0],Liste_fourmis[1]],[Dép[a][0]+Liste_fourmis[0],Dép[a][1]+Liste_fourmis[1]]]
    Couleur_case=["black"]
    grille.after(10,lambda Déplacement_fourmi=Déplacement_fourmi,Couleur_case=Couleur_case:affichage(grille,Déplacement_fourmi,Couleur_case))
      
        
def couleur(event,Liste_rectangle,Liste_fourmis):
    x,y=event.x,event.y
    grille.itemconfigure(Liste_rectangle[Liste_fourmis[0]][Liste_fourmis[1]],fill="red") 
    for i in range(len(Liste_rectangle)):
        for j in range(len(Liste_rectangle[i])):
            if i*10<=x and (i+1)*10>x and j*10<=y and (j+1)*10>y:
                grille.itemconfigure(Liste_rectangle[i][j],fill="blue") 
                Liste_fourmis=[i,j]
                grille.bind("<Motion>",lambda event:couleur(event,Liste_rectangle,Liste_fourmis))
                grille.bind("<ButtonRelease-1>",lambda event,Liste_rectangle=Liste_rectangle,Liste_fourmis=Liste_fourmis:debut(event,Liste_rectangle,Liste_fourmis))
Liste_souris=[0,0]
grille.bind("<Motion>",lambda event:couleur(event,Liste_rectangle,Liste_souris))    
            
            
Fenetre_Principale.mainloop()