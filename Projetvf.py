#from tkinter import * 
from tkinter import filedialog,Menu, Tk,Canvas, Entry,Button,Label
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy import stats # calculer modèle linéaire 
from scipy.interpolate import make_interp_spline as sp, BSpline
import os 
import matplotlib.image as pltim 
import PIL 
os.chdir(r"C:\Users\Tom\Documents\Cours\Polytech\3A\S6\Programmation\TD\Projet_Entreprise")
#print(os.getcwd())


global F
F = [] 

#Programme courbe 
Liste = [] 
def image_import(fichier) : 
    R = []
    V=[]
    B=[]
    global moyenne
    moyenne = 0 
    moyenne2 = 0
    moyenne3 = 0
    im = pltim.imread(fichier) 
    img = PIL.Image.open(fichier)
#    raws,line = np.shape(im[0])
    for i in range((len(im[0])//2)-100,(len(im[0])//2)+100):
        for j in range((len(im)//2)-100,(len(im)//2)+100):
            r,v,b = img.getpixel((i,j))
            R.append(r)
            V.append(v)
            B.append(b)
    for i in range(len(R)) : 
        moyenne+=R[i]
    moyenne = moyenne//len(R)
    for j in range(len(V)) : 
        moyenne2+=V[j]
    moyenne2 = moyenne2//len(V)
    for k in range(len(B))  : 
        moyenne3+=B[k]
    moyenne3 = moyenne3//len(B)
    if (moyenne > moyenne2 or moyenne > moyenne3) and (moyenne != moyenne2 != moyenne3) and (moyenne2 < 100 and moyenne3 < 100) and moyenne>150: 
        Liste.append(moyenne)
        return Liste
    
def tri(L): 
    for i in range(len(L)-1): 
        mini=min(L[i:])
        imini = L[i:].index(mini)
        if imini != 0 : 
            L[i],L[i+imini] = L[i+imini],L[i]
    return L

def graph():
    Entree1.destroy()
    Valideur1.destroy()
    Entree2.destroy()
    Valideur2.destroy()
    Entree3.destroy()
    Valideur3.destroy()
    Entree4.destroy()
    Valideur4.destroy()
    Entree5.destroy()
    Valideur5.destroy()
    Calibrer.destroy() 
    global xcal , L
    xcal = []
    L=[]
    Liste_complet=[]
    for i in range(len(F)):
        L = image_import(F[i][0]) 
        Liste_complet.append(moyenne)
    L = tri(L)
    for i in range(len(Liste_complet)):
        for j in range(len(L)):
            print(Liste_complet[i],L[j],i,j)
            if Liste_complet[i] == L[j]:
                xcal.append(F[i][1])
    xcal = tri(xcal)
    print(L,xcal)
    xcal=np.array(xcal)
    L=np.array(L)
    axes = plt.gca()
    axes.set_ylim(L[0],L[-1])
    x_new = np.linspace(min(xcal), max(xcal),300)#=> 50 nouveau points à partir des datas 
    sp1 = sp(xcal,L,k=3)
    y_new = sp1(x_new)
    #Intégration graphique TK de la courbe
    figure=Figure(figsize=(6,4),dpi=96)
    ax = figure.add_subplot(111)
    ax.plot(x_new,y_new)
    print(x_new, y_new)
    
    graphique=FigureCanvasTkAgg(figure,master=Fenetre)
    canvas = graphique.get_tk_widget()
    canvas.pack()
    
    global Boutton_Sauver
    Boutton_Sauver = Button(cnv,text="Sauvegarder mes données",command=save)
    Boutton_Sauver.pack()

#programme explorateur fichier
def parcourir() : 
    Fichier = filedialog.askopenfilename(initialdir = r"C:\Users\Tom\Documents\Cours\Polytech\3A\S6\Programmation\TD\Projet_Entreprise", 
                                         title = "Choix de l'image")
    global F
    F.append(Fichier)
    Result = image_import(F[0])
    Result = int(Result[0])
    resultats(Result)
    
    
    
    
def parcourir_images():
    while len(F) < 5 : 
        Fichier = filedialog.askopenfilename(initialdir = r"C:\Users\Tom\Documents\Cours\Polytech\3A\S6\Programmation\TD\Projet_Entreprise", 
                                             title = "Choix de l'image")
        F.append([Fichier])
    global Boutton_Entree
    Boutton_Entree = Button(cnv, text="Entrer ma glycémie", 
                            command=Entree_gly)
    Boutton_Entree.pack()



def Entree_gly() : 
    global Entree1,Valideur1,Entree2,Valideur2,Entree3,Valideur3,Entree4
    global Valideur4,Entree5,Valideur5,Calibrer
    Boutton_Entree.destroy()
    Entree1 = Entry(cnv)
    Entree1.pack()      
    Valideur1 = Button(cnv, text="Valider la valeur pour l'image 1", 
                       command=Ajout_liste1)
    Valideur1.pack()
    
    Entree2 = Entry(cnv)
    Entree2.pack()   
    Valideur2 = Button(cnv, text="Valider la valeur pour l'image 2", 
                       command=Ajout_liste2)
    Valideur2.pack()
    
    Entree3 = Entry(cnv)
    Entree3.pack()  
    Valideur3 = Button(cnv, text="Valider la valeur pour l'image 3", 
                       command=Ajout_liste3)
    Valideur3.pack()
    
    Entree4 = Entry(cnv)
    Entree4.pack()  
    Valideur4 = Button(cnv, text="Valider la valeur pour l'image 4", 
                       command=Ajout_liste4)
    Valideur4.pack()
    
    Entree5 = Entry(cnv)
    Entree5.pack()  
    Valideur5 = Button(cnv, text="Valider la valeur pour l'image 5", 
                       command=Ajout_liste5)
    Valideur5.pack()
    
    
    Calibrer = Button(cnv, text="Calibrer",
                      command=graph)
    Calibrer.pack()

def Ajout_liste1() :
    F[0].append(float(Entree1.get()))
    
def Ajout_liste2() :
    F[1].append(float(Entree2.get()))

def Ajout_liste3() :
    F[2].append(float(Entree3.get()))
    
def Ajout_liste4() :
    F[3].append(float(Entree4.get()))

def Ajout_liste5() :
    F[4].append(float(Entree5.get()))

def Fermer() : 
    print(F)
    Fenetre.destroy()
    
def Fermer_fenetre() :
    cnv.destroy()
    print(F)

def save(): 
    cdc=''
    f = open("data.txt","r")
    cdc = f.readline() 
    x = str(xcal)
    y = str(L)
    x += cdc 
    cdc = f.readline()
    y += cdc 
    f.close() 
    f = open("data.txt","w")
    f.write(x + "\n") 
    f.write(y)
    f.close() 
    Boutton_Sauver.destroy()

def arrondis(L):
    Liste_arrondis = [] 
    for i in range(len(L)):
        if int(L[i]) not in Liste_arrondis:
            Liste_arrondis.append(int(L[i]))
    return Liste_arrondis

def resultats(y_val) :
    i=3
    debut = 0
    Flag = True 
    x,y = graphiques()
    y_arrondis = arrondis(y)
    
    if y_val <= y[0] or y_val>= 249 :
        print("impossible")
        return ("Valeur saisie hors des limites")
    
    #faire une boucle permettant de calculer des tangentes 
    while Flag :
        reticulation = 1
        while reticulation > 0.95:
            if i == len(y)-1:
                pente, ordonnee,reticulation, p_val, std_error = stats.linregress(x[i-5:i],
                                                                                  y[i-5:i])
#                print((y_val - ordonnee)/pente,pente, ordonnee,reticulation )
#                return (y_val - ordonnee)/pente
            
            pente, ordonnee,reticulation, p_val, std_error = stats.linregress(x[debut:i],
                                                                              y[debut:i])
            i+=1
            
        y_val_arrondis = int(y[i-2])
        
        if y_val in y_arrondis[:y_arrondis.index(y_val_arrondis)]:
            Flag = False
            
        debut = i
        i+=3
        
    print(1)
        
    print((y_val - ordonnee)/pente)
    
    gly = (y_val - ordonnee)/pente
    
    label = Label(cnv, text="Votre glycémie est de %f g/L" %(gly))
    label.pack()
    
    Boutton_fermer = Button(cnv,text="fermer",command=Fermer)
    Boutton_fermer.pack() 

#    
def dataFrame() : 
    #Récupération des fichiers 
    f = open("data.txt","r")
    tot = '' 
    x_final = []
    y_final = []
    x = f.readline()
    for i in range(1,len(x)-1):
        if x[i]!= ' ' and x[i]!= '' and x[i]!= '[' and x[i]!= ']' and x[i] != "\n" and x[i] != ',' :
            tot += x[i]
        elif tot != '' :
            if '.' in tot :
                tot = float(tot)
            else : 
                tot = int(tot)
            x_final.append(tot)
            tot = ''             
            
        
    y=f.readline()
    for j in range(1,len(y)):
        if y[j]!= ' ' and y[j]!= '' and y[j]!= '[' and y[j]!= ']' and y[j] != "\n" and y[j] !=',':
            tot += y[j]
        elif tot != '' :
            if '.' in tot :
                tot = float(tot)
            else : 
                tot = int(tot)
            y_final.append(tot)
            tot = ''
    f.close()  
    return x_final,y_final
    
def graphiques() :
    x_final, y_final = dataFrame()
    #Tri des datas 
    x_final = tri(x_final)
    y_final = tri(y_final)
    
    #affichage graphiques 
    x_final=np.array(x_final)
    y_final=np.array(y_final)
    axes = plt.gca()
    axes.set_ylim(y_final[0],y_final[-1])
    x_new = np.linspace(min(x_final), max(x_final),50)#=> 50 nouveau points à partir des datas 
    sp1 = sp(x_final,y_final,k=3)
    y_new = sp1(x_new)
    
    #Intégration graphique TK de la courbe 
    figure=Figure(figsize=(6,4),dpi=96)
    ax = figure.add_subplot(111)
    ax.plot(x_new,y_new)
    
    graphique=FigureCanvasTkAgg(figure,master=cnv)
    canvas = graphique.get_tk_widget()
    canvas.pack()
    return x_new,y_new
    
#Fenètre principale
Fenetre = Tk()
Fenetre.title('Glycémia')
Fenetre.geometry("500x500")
#Fenetre.attributes("-fullscreen", True)
Fenetre.config(background="white")

#Canvas  
cnv=Canvas(Fenetre,width=500, height=500, bg='white')
cnv.pack()

#Barre menu
Barre_menu=Menu(Fenetre)
Fenetre.config(menu=Barre_menu)

#Barre menu 
Utilisateur = Menu(Barre_menu,tearoff=0)
Barre_menu.add_cascade(label="Utilisateur", menu=Utilisateur)

Mesure = Menu(Barre_menu,tearoff=0) 
Mesure.add_command(label="Importer une image", command = parcourir)
Utilisateur.add_cascade(label="Mesure glycémie", menu=Mesure)

Calibrage = Menu(Barre_menu,tearoff=0) 
Calibrage.add_command(label="Importer des images", command = parcourir_images)
Utilisateur.add_cascade(label="Calibrage", menu=Calibrage)

#menu voir resultats => Courbe d'étalonnage + glycémie en fct du temps
Graphique = Menu(Barre_menu,tearoff=0)
Barre_menu.add_cascade(label="Voir mes résultats",menu=Graphique)

#Resultats = Menu(Barre_menu,tearoff=0) 
#Resultats.add_command(label="Mes résultats", command = resultats)
#Graphique.add_cascade(label="Resultats" , menu=Resultats)

Graphiques = Menu(Barre_menu,tearoff=0) 
Graphiques.add_command(label="Mes graphiques", command = graphiques)
Graphique.add_cascade(label="Resultats" , menu=Graphiques)

#Menu quitter 
Quitter = Menu(Barre_menu, tearoff=0)
Quitter.add_command(label="Quiter", command = Fermer)
Barre_menu.add_cascade(label="Quitter l'application", menu=Quitter)

Fenetre.mainloop()
#Boutton supprimer mes data 