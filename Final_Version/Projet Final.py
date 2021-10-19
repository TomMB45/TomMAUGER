import turtle as t #On import le module turtle
import random #On importe le module random
from copy import deepcopy #On import deepcopy depuis le module copy
import os 




game_area=t.Screen() #On defini un écran pour afficher nos dessins

game_area.setup(width=1920,height=1080) #On fixe la taille de l'écran en HD
game_area.tracer(0,0) #On supprime les animations de dessins

game_area.bgpic("Mer1.gif") #On met un fond d'écran 

#On créer les tortues pour les cartes de l'ordi
to1 = t.Turtle()
to2 = t.Turtle()
to3 = t.Turtle()
to4 = t.Turtle() 
to5 = t.Turtle()
to6 = t.Turtle()
to7 = t.Turtle()
to8 = t.Turtle()

turtordi = [to1,to2,to3,to4,to5,to6,to7,to8] #Liste des tortues utilisées pour dessiner les cartes de l'ordinateur 

#On créer les tortues pour dessiner les cartes de notre main
t0 = t.Turtle()
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t7 = t.Turtle()

Tortues = [t0,t1,t2,t3,t4,t5,t6,t7] #Création de la liste des tortue afin que par la suite chaque carte du joueur soit dessinée par une tortue


tcontour = t.Turtle() #On créer une tortue pour déssiner le contour des cartes



tscore = t.Turtle() #On creer une tortue qui affiche le score
tscore.goto(-670,-250) #On la place à l'endroit ou on veut que le score s'affiche

##################################
# Fonctions nécessaire au dessin #
##################################

def contour(tortue,x,y,decalx,decaly,longueur):
    """Fonction qui prend en entrée une tortue, des coordonnées x et y, un décalage et une longueur et qui trace le contour de la carte"""

    tortue.up() #On lève le stylo
    tortue.width(3) #On definit l'épaisseur du contour
    tortue.color("black") #On définit la couleur du contour
    tortue.goto(x+decalx,y+decaly)#On déplace notre tortue à l'origine de la carte
    tortue.down() #On pose notre stylo
    #On trace le contour
    for i in range(4):  
        tortue.forward(longueur)
        tortue.left(90)
    tortue.width(1)
    
def contourbateau(tortue,x,y,decalx,decaly):
    """Fonction qui prend en entrée une tortue, des coordonnées x,y et un décalage en x et y et qui trace le contour des embarcations"""
  
    tortue.up() #On lève notre stylo
    tortue.width(3)#On definit l'épaisseur du contour
    tortue.color("black")#On définit la couleur du contour
    tortue.goto(x+decalx+20,y+decaly)#On déplace notre tortue à l'origine de la carte
    tortue.down()#On pose notre stylo
     #On trace le contour
    for i in range(2):  
        tortue.forward(160)
        tortue.left(90)
        for j in range(2):
            tortue.forward(10)
            tortue.right(90)
            tortue.forward(10)
            tortue.left(90)
        tortue.forward(280)
        tortue.left(90)
        for j in range(2):
            tortue.forward(10)
            tortue.right(90)
            tortue.forward(10)
            tortue.left(90)  
    tortue.width(1)

def pixel(tortue,v,w,x,y,z,taillePixel):
    """dessin d'un pixel pour pixel art"""

    tortue.up() #On lève le stylo
    tortue.goto(x+v*taillePixel+z,y+w*taillePixel)#On décale la tortue en fonction des pixels déjà dessinés
    tortue.down()#On pose le stylo
    tortue.begin_fill() #On veut un pixel rempli
    #On trace notre pixel
    for i in range(4):  
        tortue.forward(taillePixel)
        tortue.left(90)
    tortue.end_fill() #On arrête le remplissage une fois le pixel fini



def dessinCarte(t,x,y,decalage,C):
    """Dessine la carte à partir de la matice de pixel art et de la matrice de son score""" 

    t.hideturtle()
    t.speed("fastest")
    Mcard = [[Animaux[C[0]][i][j] + Chiffres[C[0]][i][j]  for j in range(len(Animaux[0]))] for i in range(len(Animaux[0]))] # Permet d'obtenir la matrice d'une carte en aditionnant la matrice de l'animal ainsi que la matrice du chiffre représentant sa valeur
    if C[1] == "f":     #Dessine une carte avec un fond rose si sexe = feminin
        t.color(palette[30])
        pixel(t,0,0,x,y,decalage,110)
        contour(t,x,y,decalage,0,110)
    else:               #Sinon dessine une carte avec un fond bleu (sexe = masculin) 
        t.color(palette[29])
        pixel(t,0,0,x,y,decalage,110)
        contour(t,x,y,decalage,0,110)
    for i in range(len(Mcard)):
        for j in range(len(Mcard[0])):  #Parcours la matrice Mcard
            if Mcard[i][j] != 0 :       #Dessine uniquement le pixel si valeur différente de 0
                t.color(palette[Mcard[i][j]])
                pixel(t,j,i,x,y,decalage,5)

                
def carteadversaire(t,x,y):
    """Fonction qui prend en argument la tortue a utiliser et les positions x et y ou il faut dessiner la carte de l'adversaire"""
  
    t.hideturtle() #on cache la tortue
    t.color(palette[1]) #On choisi la couleur de notre tortue
    pixel(t,0,0,-480,300,x,110)#On dessine le fond marron
    contour(t,-480,300,x,y,110) #On dessine le contour
    for i in range(len(Back)):
        for j in range(len(Back[0])):  #Parcours la matrice du dos des cartes de l'adversaire
            if Back[i][j] != 0 :       #Dessine uniquement le pixel si valeur différente de 0
                t.color(palette[Back[i][j]]) #On choisit les couleurs qui correspondent à la matrice
                pixel(t,j,i,-480,300,x,5) #On dessine les pixels de la carte               
                

###############################
# Fonctions nécessaire au jeu #
###############################
def creerCartes(): 
    """Fonction sans argument qui permet de créer une liste de liste des cartes"""

    cartes = [] # liste des cartes (vide)
    nbExemplaires = [3,2,3,3,3,3,2,2,1,1,1] # nombre de cartes identiques pour chaque poids (par sexe) -> ici 3 cartes de oids 0, 2 cartes de poids 1 etc.
    sexes = ["m", "f"]
    for s in sexes: # pour chaque sexe
        poids = 0
        while poids < len(nbExemplaires): # et pour chaque poids (= indice dans la liste nbExemplaires)
            cartes += nbExemplaires[poids] * [[poids,s]] # on cree le bon nombre d'exemplaires pour un poids et un sexe donne
            poids += 1 # on passe au poids suivant
    return(cartes) # renvoie une liste de cartes (soit une liste de listes)

pioche = creerCartes() # creation du jeu de cartes complet ordonne (= pioche)

# Fonction permettant de piocher des cartes
def piocher(nbCartes): # Prend en entree le nombre de cartes a piocher
    """Fonction qui prend en entrée le nombre de cartes a piocher et qui renvoie une liste contenant le nombre de cartes demande"""

    global pioche # le fait de piocher va modifier la pioche (variable globale)
    cartesPiochees = pioche[:nbCartes] # on pioche les cartes
    pioche = pioche[nbCartes:] # on les enleve donc de la pioche
    return(cartesPiochees) # renvoie une liste de cartes (soit une liste de listes)


def coupPossible(carte, cartesEmbarc): # en fonction de la carte a jouer et de la liste des cartes presentes sur l'embarcation
    """Fonction qui prend en argument la carte que l'on veit jouer et la liste des cartes présentes sur l'embarcation et qui renvoie un booleen de si le coup est possible ou non"""

    if len(cartesEmbarc) <= 1 : # si pas encore de carte sur l'embarcation ou une seule

        return(True) # on peut jouer ce qu'on veut
    else: # s'il y a au moins 2 cartes sur l'embarcation
        sexe = carte[1] # sexe de la carte a jouer
        sexeDerniereCarte = cartesEmbarc[-1][1] # sexe de la derniere carte posee sur l'embarcation
        sexeAvantDerniereCarte = cartesEmbarc[-2][1] # sexe de l'avant derniere carte posee sur l'embarcation
        alternance = (sexeDerniereCarte != sexeAvantDerniereCarte) # il faut une alternance des sexes si les 2 dernieres cartes de l'embarcation sont de sexe different, sinon il faut toujours le meme sexe
        if alternance: # s'il y a alternance des sexes sur l'embarcation
            return(sexe != sexeDerniereCarte)
        else: # s'il n'y a pas d'alternance, il faut que le sexe de la carte a jouer soit le meme que celui de la derniere carte 
            return(sexe == sexeDerniereCarte) # renvoie un booleen qui informe de la faisabilite du coup que souhaite faire le joueur




def choixCarteOrdi():
    """Fonction sans paramètre qui permet à l'ordinateur de ne pas jouer de coup perdant et de jouer un coup gagnant si il en la possibilité"""

    scoreFuture = {} #On creer un dictionnaire pour stocker le score associé à chaque cartes
    main = mains["ordi"] #On définit la main utilisée, celle de l'ordi dans ce cas là
    
    for i in range(len(main)): #On parcourt la main
        for embarc in jeu: #On parcourt les embarcations
            if coupPossible(main[i], jeu[embarc]): #Si le coup est possible
                
                if verdictOrdi(jeu[embarc]+[main[i]]) == None : #On regarde si le coup n'est ni gagnant, ni perdant
                    scoreFuture[(i, embarc)] = 0  #Si c'est le cas on affecte un score de 0 à ce coup
                else :
                    scoreFuture[(i, embarc)] = verdictOrdi(jeu[embarc]+[main[i]]) #Si le coup est gagnant on lui affecte son score, idem si il est perdant
    return(max(scoreFuture, key=scoreFuture.get)) #On renvoie la carte qui à le plus haut score



def verdictOrdi(cartesEmbarc): # en fonction de la carte a jouer et de la liste des cartes presentes sur l'embarcation
    """Fonction qui prend en argument quel joueur joue et la liste des cartes présentes sur l'embracation et qui fait le verdict du coup joue sans modification du score(utiliee dans la fonction choixCarteOrdi)"""

    global scores, jeu # le fait de gagner ou perdre va modifier le jeu ainsi que mon score ou celui de l'ordi
    main = mains["ordi"]
    poidsEmbarc = 0 # calcul du poids total de l'embarcation
    for c in cartesEmbarc: # pour chaque carte de l'embarcation
        poidsEmbarc += c[0] # on ajoute le poids de la carte au poids total
    if poidsEmbarc == poidsMax: # si l'embarcation atteint exactement son poids max
        return 15
    if poidsEmbarc > poidsMax: # si l'embarcation depasse le poids max
        return -poidsEmbarc



def verdict(joueur, cartesEmbarc): # en fonction de la carte a jouer et de la liste des cartes presentes sur l'embarcation
    """Fonction qui prend en argument quel joueur joue et la liste des cartes présentes sur l'embracation et qui fait le verdict du coup joue avec modification du score"""
  
    global scores, jeu # le fait de gagner ou perdre va modifier le jeu ainsi que mon score ou celui de l'ordi
    main = mains[joueur]
    poidsEmbarc = 0 # calcul du poids total de l'embarcation
    for c in cartesEmbarc: # pour chaque carte de l'embarcation
        poidsEmbarc += c[0] # on ajoute le poids de la carte au poids total
    if poidsEmbarc == poidsMax: # si l'embarcation atteint exactement son poids max
        scores[joueur] += poidsEmbarc # le joueur gagne des points
        return True
    if poidsEmbarc > poidsMax: # si l'embarcation depasse le poids max
        scores[joueur] -= poidsEmbarc # le joueur perd des points  
        return True
#Fonction pour dessiner à partir des matrices d'animaux



def jouerCarte(joueur, numCarte, embarc): # On choisit celui qui joue ("moi" ou "ordi"), le numero de la carte a jouer (la premiere carte etant numero 0) ainsi que l'embarcation ("A","B"...)
    """Fonction qui prend en argument le joueur, le numero de la carte joué et l'embarcation sur laquelle la carte est joué et qui ajoute la carte jouée sur l'embarcation et supprime la carte jouée de la main du joueur"""
  
    global mains, jeu # le fait de jouer va modifier le jeu ainsi que ma main ou celle de l'ordi
    carteAjouer = mains[joueur][numCarte] # la carte a jouer est la nieme de la main du joueur (mains etant un dictionnaire)
    jeu[embarc] += [carteAjouer] # on ajoute la carte jouee sur l'embarcation choisie du jeu
    mains[joueur].remove(carteAjouer) #supprime de la main du joueur la carte qui vient d'être jouée

        
def bouton_impossible_jouer(x,y) :
    """Fonction qui prend en argument les coordonnées x et y, permettant de vérifier si le joueur peut jouer et si il à bien cliquer sur le bouton"""
  
    L = 0 #Variable permettant de compter le nombre de coup possible
    for i in range(len(mains["moi"])): #On parcourt les cartes de la main du joueur 
        for embarc in jeu: #pour chaque carte du joueur on parcourt chaque embarcation 
            if coupPossible(mains["moi"][i], jeu[embarc]): #On vérifie si coup possible renvoie vrai 
                L+=1 #si coup possible renvoie True alors L augmente de 1 
    if Position_bouton_impossible_jouer[0] < x < (Position_bouton_impossible_jouer[0]+100) and Position_bouton_impossible_jouer[1] < y < (Position_bouton_impossible_jouer[1]+100) and L==0 : #on vérifie si le clique de l'utilisateur est dans la hitbox du bouton et que le joueur ne peut jouer aucun coup
        return True
    else : 
        return False

def numCard(x,y) :
    """Fonction qui prend en argument les coordonnées du clique et qui renvoie l'indice de la carte sur laquelle le clique à été effectué""" 
  
    clic = int((x+480) // 120) #On affecte l'indice de la carte en fonction de l'endroit ou on clique
    if not -400 <= y <= -290 or (x+480) // 120 == (x+370) // 120 or not 0 <= clic <= 7 : # On regarde que notre clic soit bien sur une carte, pas à coté
        return False #On renvoit False si c'est à coté
    return clic + 1 #On renvoit l'indice de la carte en commencant par 1 si on a cliqué sur une carte

def numBoat(x,y) :
    """Fonction qui prend en argument les coordonnées du clique et qui renvoie l'indice de l'embarcation sur laquelle le clique à été effectué""" 
    
    clic = int((x+680)//300)#On affecte l'indice du bateau en fonction de l'endroit ou on clique
    
    if not -100 <= y <= 200 or (x+680)//300 == (x+ 480) //300 or not 0 <= clic <= 4 :# On regarde que notre clic soit bien sur un bateau, pas à coté
        return False#On renvoit False si c'est à coté
 
    return clic + 1 #On renvoit l'indice de la du bateau en commencant par 1 si on a cliqué sur un bateau



##################################################
# Initialisation des variables nécessaire au jeu #
##################################################

random.shuffle(pioche) # on melange la pioche (la methode shuffle du module random permet de melanger une liste aleatoirement)
mains = {"ordi":[],"moi":[]} # On créer les mains de l'ordi et du joueur
mains["ordi"] = piocher(8) #L'ordi pioche 8 cartes
mains["moi"] = piocher(8) #Le joueur pioche 8 cartes
scores = {"ordi":0,"moi":0} #Dictionnaire des scores des deux joueurs
jeu = {"A":[],"B":[],"C":[],"D":[],"E" : []} #Initialisation du jeu 


listJeu = ["A","B","C","D","E"] #Liste des embarcations 
IndiCarte = [] #Liste permettant de connaitre l'indice de la carte sur laquelle on a cliqué
embarcT = {"A":[],"B" : [],"C" : [], "D" :[],"E" : []} # Dictionnaire permettant de savoir quelle tortue a dessiné les cartes en fonction de l'embarcation
cjoueOrdi = [] #Liste des cartes déjà jouéespar l'ordi
cJoue = [] #Liste des cartes déjà jouées par le joueur
mainFixe = deepcopy(mains["moi"]) #Deepcopy de la main du joueur pour récupérer les valeurs des cartes à jouer

posbato = [-635,-335,-35,265,565] #Origine des bateaux
Position_bouton_impossible_jouer = [600,-250] #Origine du bouton pour dire qu'on ne peut pas jouer


poidsMax = 15 #On fixe le poids maximum par embarcation
joueur = "moi" #On initialise le jeu en faisant commencer le joueur

#################
# Moteur du jeu #
#################

def jouer(x,y) :
    """moteur du jeu"""

    global IndiCarte,joueur, jeu,mains, Tortues, turtordi #Il faut pouvoir modifer les variables global comme notre fonction se lance a chaque clic

    if mains[joueur] == [] : # Notre condition de fin du jeu
        gagnant = max(scores, key=scores.get) #On récupere le joueur avec le score le plus haut
        if gagnant == "moi" : #Si on a gagné
            tscore.goto(-440,-200) #On déplace notre tortue des scores
            tscore.write("Whallah t'as assuré ! Chapeau ", font=("Arial", 40, "normal")) #ON EST CHAMPIOONS
        else : #Si l'ordi a gagné
            tscore.goto(-440,-200) #On déplace notre tortue des scores
            tscore.write("Retourne t'entrainer Loser :P", font=("Arial", 40, "normal")) #On doit bosser un peu plus     
    else : #Personne n'a gagné, on joue
        
        if joueur == 'moi' : #Le joueur joue
            if bouton_impossible_jouer(x,y) : #On regarde si le joueur a cliqué sur le bouton pour passer
                mains["moi"] = [] #On vide ses cartes
                for i in Tortues :
                    i.clear() #On supprime les cartes
    
    
            if numCard(x,y) : #On clique sur une carte
                IndiCarte.append(numCard(x,y)) #On ajoute à la liste des cartes cliquées la carte cliquée
                
    
            if IndiCarte != [] and numBoat(x,y) and coupPossible(mainFixe[IndiCarte[-1]-1], jeu[listJeu[numBoat(x,y)-1]]) and not IndiCarte[-1] in cJoue:  #On regarde si on a cliqué sur une carte, puis sur un bateux puis, si le coup est possible, et enfin si la carte a déjà été jouée ou pas
                
                jouerCarte(joueur, mains[joueur].index(mainFixe[IndiCarte[-1]-1]), listJeu[numBoat(x,y)-1]) #On joue la carte
                
                Tortues[IndiCarte[-1]-1].clear() #On efface la carte jouée
                
                dessinCarte(Tortues[IndiCarte[-1]-1], -635+(numBoat(x,y)-1)*300, 90 - (len(jeu[listJeu[numBoat(x,y)-1]])-1)*40,0, mainFixe[IndiCarte[-1]-1]) #On dessine la carte
                
                embarcT[listJeu[numBoat(x,y)-1]].append(Tortues[IndiCarte[-1]-1]) #On ajoute la tortue qui a dessiné la carte à l'embarcation sur laquelle la carte a été jouée
                
                if verdict(joueur, jeu[listJeu[numBoat(x,y)-1]]) : #On regarde si le coup joué est gagnat ou perdant
    
                    for turt in embarcT[listJeu[numBoat(x,y)-1]] : #Si le coup est gagnant ou perdant on parcours les tortues jouées sur l'embarcation
                        turt.clear() #On les effaces
                    tscore.clear()#On efface le score
                    tscore.write("Ordinateur: " + str(scores["ordi"]) + "\n" +  "Moi: " + str(scores["moi"]), font=("Arial", 20, "normal"))#On met à jour le score
                    embarcT[listJeu[numBoat(x,y)-1]] = [] #On vide la liste de tortues sur l'embarcation
                    jeu[listJeu[numBoat(x,y)-1]] = [] #On vide l'embarcation 

    
                IndiCarte = [] #On vide notre liste de cartes cliqués
                
                cJoue.append(numCard(x,y)) #On stock la carte jouée
                joueur = "ordi" #C'est à l'ordi de joueur
                
        
        if joueur == "ordi": # cas de l'ordi
            peutJouer = True #On fixe le fait que l'ordi puisse jouer
            choix = choixCarteOrdi() # choix de la carte a jouer par l'ordi
            if choix == (0,0): # impossible de jouer pour l'ordi 
                mains[joueur] == [] # il defausse toutes ses cartes (sa main devient vide)
                peutJouer = False # L'ordi ne peut plus jouer
            else: #L'ordi peut jouer
                numCarte = choix[0]# numero de la carte choisie par l'ordi
                carte = mains[joueur][numCarte] #On définit la carte à jouer
                embarc = choix[1] # embarcation choisie par l'ordi
            if peutJouer : # On regarde si l'ordi a passé son tour ou pas
                jouerCarte(joueur, numCarte, embarc) #On joue la carte
                
                turtordi[0].clear()#On efface la carte de la main
                dessinCarte(turtordi[0],posbato[listJeu.index(embarc)],90 - (len(jeu[embarc])-1)*40,0,carte) #On dessine la carte sur l'embarcation
                embarcT[embarc].append(turtordi[0]) #On ajoute à la liste des tortues jouée sur l'embarcation
                turtordi = turtordi[1:] #On supprime la tortue de la liste des tortues de l'ordi


            if verdict(joueur, jeu[embarc]) : # On regarde si le coup est gagnant ou perdant
                for turt in embarcT[embarc] : 
                    turt.clear()#On efface les cartes de l'embarcation
                embarcT[embarc] = [] #On vide la liste des tortues de l'embarcation 
                jeu[embarc] = [] #On vide l'embarcation
                tscore.clear() #On efface le score
                tscore.write("Ordinateur: " + str(scores["ordi"]) + "\n" +  "Moi: " + str(scores["moi"]), font=("Arial", 20, "normal")) #On met à jour le score


            joueur = "moi" #On passe à nous



#################
# Dessin du jeu #
#################



for k in range(8): #Boucle permettant de dessiner les 8 cartes de la main du joueur "moi"
        dessinCarte(Tortues[k],-480,-400,120*k,mains["moi"][k])

for k in range(8) : #Boucle permettant de dessiner les 8 cartes de la main du joueur "ordi"
    carteadversaire(turtordi[k],120*k,0)

random.shuffle(Bateaux) #Fonction qui permet de mélanger les couleur des bateau 

#Fonction permettant de dessiner les 5 Bateaux
for k in range(5): #Dessine les 5 Bateaux
    for i in range(len(Bateaux[k])):#Parcourt toutes les liste de la matrice Bateaux 
        for j in range(len(Bateaux[k][i])): #Pour chaque liste de la matrice Coquillage, on parcourt toute la sous liste
            if Bateaux[k][i][j] != 0 : #Si la valeur est égale à 0 on ne dessine pas de pixel
                t.color(palette[Bateaux[k][i][j]]) #On fixe la couleur de dessin de la tortue
                pixel(t,j,i,-680,-100,300 *k,10) #la tortue dessine le pixel correspondant à l'élément de la sous liste
        contourbateau(tcontour,-680,-100,300*k,0) #La tortue du contour dessine le contour du bateau 
    
#Fonction permettant de dessiner le bouton coquillage impossible de jouer 
for i in range(len(Coquillage)): #Parcourt toutes les liste de la matrice Coquillage 
    for j in range(len(Coquillage[i])): #Pour chaque liste de la matrice Coquillage, on parcourt toute la sous liste
        if Coquillage[i][j] != 0 :  #Si la valeur est égale à 0 on ne dessine pas de pixel    
            t.color(palette[Coquillage[i][j]]) #On fixe la couleur de dessin de la tortue
            pixel(t,j,i,600,-250,0,5) #la tortue dessine le pixel correspondant à l'élément de la sous liste
            
t.goto(600,-275)
t.write("Passer", font=("Arial", 20, "normal")) #Permet d'indiquer de le coquillage correspond au boutton
            
tscore.write("Ordinateur: " + str(scores["ordi"]) + "\n" +  "Moi: " + str(scores["moi"]), font=("Arial", 20, "normal")) #la tortue des score dessine le score du joueur et de l'ordi

game_area.onclick(jouer) #On lance la fonction "jouer" à chaque fois que l'utilisateur clique sur l'écran

t.done()#On finit la récolte d'évenement pour terminer notre programme