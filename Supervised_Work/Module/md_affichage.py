from tkinter import filedialog,Tk,Button,Label
import os 
global chemin 
chemin=os.getcwd()

global F
F=[]

def parcourir() : 
    """Fonction qui ne prend pas d'argument et qui permet d'ouvrir 
    un explorateur de fichier pour choisir celui que l'on veut exécuter. 
    Le chemin d'accès est ensuite ajouté dans une liste"""
    Fichier = filedialog.askopenfilename(initialdir = chemin, title = "Choix du fichier")
    F.append(Fichier)
    return F

def fenetre(name):
    """Procédure qui permet de crée une fenètre TK avec un bouton parcourir 
    et un bouton quiter, le bouton parcourir ouvrir un explorateur de fichier
    le bouton quiter permet de fermer la page"""
    Fenetre=Tk()
    Fenetre.title(name)
    Fenetre.geometry("300x100")
    Fenetre.config(background="white")
    Bouton_explorer = Button(Fenetre, text="Parcourir", command=parcourir).pack()
    Bouton_quitter = Button(Fenetre, text="Lancer le calcul", command=Fenetre.destroy).pack()
    Fenetre.mainloop()
    
def fenetre_fin(texte): 
    """Procédure qui permet de crée une fenètre TK avec un bouton quiter, 
    ainsi qu'un texte au dessus du bouton. Le bouton ferme la fenetre"""
    Fenetre=Tk()
    Fenetre.title("Fenètre de fin")
    Fenetre.config(background="white")
    Lab=Label(Fenetre, bg='white',text=texte)
    Lab.pack()
    Bouton_quitter = Button(Fenetre, text="Quitter", command=Fenetre.destroy).pack()
    Fenetre.mainloop()
