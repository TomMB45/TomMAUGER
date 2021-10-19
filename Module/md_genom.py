##########################################################
### Fonctions utilisées pour la programation génomique ###
##########################################################

#################################################
############ Import des librairies ##############
#################################################
from Bio.Seq import Seq,transcribe,translate
import re 

#################################
########### Variables ###########
#################################

global nucleotides
nucleotides = ["A","T","G","C"]

########################
### Gestion fichiers ###
########################

def load_Fasta(nom):
    """Fonction qui prend en argument le nom du fichier à ouvrir et qui renvoie une liste contenant toutes les lignes"""
    f = open(nom)
    data=[]
    cdc = f.readline()
    while ">" not in cdc :          #on cherche le début du fichier 
        cdc = f.readline()
    cdc = f.readline()
    while cdc != "" :               #lecture du documentligne par ligne 
        data.append(cdc)
        cdc=f.readline()
    f.close()
    return data 

def From_Dico_To_List(dico): 
    """Fonction qui prend en argument un dictionnaire donc la clée est une chaine de caractère et la valeur une liste de deux éléments"""
    liste=[]
    for clee in dico:
        liste.append(clee)
        liste.append(dico[clee][0])
        liste.append(dico[clee][1])
    return liste 
      
def fichier_sortie(GC,nomFile, extention,A,T,G,C,Liste_prot):
    """Procédure qui prend en argument les datas(une liste de chaine de caractère), le pourcentage de GC du brin, un nom de fichier et une extention et qui écrit dans celui ci les informations de data"""
    nom=str(nomFile)+'.'+str(extention) 
    f=open(nom, "w")
    f.write("Sur ce fragment, on a donc au total {:.3f} % de bases G et C. \nCela correspond donc à une température de fusion approximativement égale à : {:.3f}°C.\n\n".format(GC,Tm(GC)))
    f.write("On à donc :\n{} de base A, \n{} base T,\n{} base G,\n{} base C\n\n\n".format(A,T,G,C))
    index=1
    f.write("Séquences protéiques trouvées :\n")
    for i in Liste_prot:
        if len(i) >=50 :                    #si la longueur de la chaine d'acide aminée est inférieur à 50 on n'écrit pas le résultat dans le fichier
            f.write("Séquence protéique {} : ".format(index) +str(i)+"\n")
            index+=1
    f.close()

def fichier_sortie_dinu_csv(data, nomFile): 
    """Procédure qui prend en entrée les datas(liste de chaine de caractère) et qui écrit un fichier csv contenant les informations de data(dinucléotide, occurence, fréquence"""
    str(nomFile)
    nom=nomFile+'.csv'
    f=open(nom,"w")
    f.write("Dinucléotide, Nombre, Fréquence \n")
    for i in range(0,len(data),3): 
        f.write("{} ,  {} , {:.3f} \n".format(data[i], (data[i+1]),(data[i+2])))
    f.close()
    
################################################
### Nettoyage et transformations des données ###
################################################

def nettoyage(liste) : 
    """Fontion qui prend en argument une liste de chaine de caractère et qui renvoie une chaine de caractère concaténé sans les \n ainsi que les espaces(si espaces crée plusieurs lignes)"""
    data_net=[]
    if len(liste) == 0 :
        return False
    else : 
        for cdc in liste :
            cdc.strip()             #supprime tout les \n 
            cdc.split()             #supprime les espaces
            cdc.upper()
            if cdc[-1]=="\n":
                data_net.append(cdc[:-1])
            else:
                data_net.append(cdc)
        return data_net 
    
def Lignes_To_Ligne(data):
    """Fonction qui prend en argument les données(liste de chaine de caractère) et qui les transforme en une chaine de caractère unique"""
    cdc=""
    if len(data) == 0 :
        return False
    else :  
        for ligne in data : 
            cdc+=ligne
    return cdc

def split_Multi_Fasta(data):
    """Fonction qui prend en argument une liste de chaine de cractère extraite par la fonction load et qui renvoie un dictionnaire donc chaque clée est une séquence et chaque valeur est une liste des lignes de chaines de caractères""" 
    dico={}
    for ligne in data:
        if ">" in ligne :
            key=ligne
            dico[key]=""
        else : 
            dico[key]+=ligne
    return dico

###########################
### Opérations sur data ###
###########################
    
def dicodinucléotides() : 
    """Fonction qui permet de crée un dictionnaire dont la clée est un dinucléotide et la valeur une liste [nombre d'occurence, fréquence]"""
    dinucleotides={}
    for i in range(len(nucleotides)):
        for j in range(len(nucleotides)):
            dinucleotides[nucleotides[i]+nucleotides[j]] = [0,0]
    return dinucleotides

def occurence(lettre,cdc) : 
    """Fonction qui prend en argument une lettre à rechercher et une chaine de caractère et qui renvoie le nombre d'occurence de cette lettre dans une chaine de caractère"""
    nb=0
    if cdc == "" : 
        return False 
    lettre.upper()                      #si en minuscule 
    str(lettre)                         #si oubli des guillemets 
    if lettre not in nucleotides:
        return False
    for base in cdc :
        if base==lettre: 
            nb+=1
    return nb 

def freq(nb,longueur):
    """Fonction qui prend argument un nombre un nombre et la longueur de la chaine nucléotidique et qui renvoie la fréquence"""
    return (nb/longueur) 

def GC(nb,longueur):
    """Fonction qui prend argument un nombre d'occurence de G ou C et la longueur de la chaine nucléotidique et qui renvoie le pourcentage de GC"""
    return (nb/longueur)*100 

def Tm(GC):
    """Fonction qui prend en argument un pourcentage de GC et qui renvoie la température de fusion du brin d'ADN"""
    return (70 + (0.44*GC))

#def recherche_ORF(seq,position=True):
    # """Permet à partir d'une séquence d'ADN de rechercher tout les cadres ouvert de lecture et les renvoie dans une liste"""
    # Liste_cdc=[]
    # Liste_pos=[]
    # res = re.finditer("ATG", seq) 
    # for match in res:
    #     Liste_cdc.append(seq[match.start():])
    #     Liste_pos.append(match.start())
    # if position : 
    #     return Liste_cdc,Liste_pos
    # else : 
    #     return Liste_cdc
    
#def recherche_STOP(seq,position=True):
    # """Permet à partir d'une séquence d'ADN de rechercher tout les cadres ouvert de lecture et les renvoie dans une liste"""
    # Liste_cdc=[]
    # Liste_pos=[]
    # res = re.finditer("(TAA|TAG|TGA)", seq) 
    # for match in res:
    #     Liste_cdc.append(seq[match.start():])
    #     Liste_pos.append(match.start())
    # if position : 
    #     return Liste_cdc,Liste_pos
    # else : 
    #     return Liste_cdc
    
def rechREsimple(motif,seq,position=True):
    """Fonction qui prend en argument une chaine de caractère sous forme d'expression régulière, une chaine de caractère dans laquelle chercher l'expression régulière et un argument optionnel(position) sous forme de booléen et qui renvoie la liste des chaines de caractères ayant pour commencement ce motif et de manière optionnel la liste des index des position des expressions régulières"""
    
    Liste_cdc=[]
    Liste_pos=[]
    res = re.finditer(motif, seq) 
    for match in res:
        Liste_cdc.append(seq[match.start():])
        Liste_pos.append(match.start())
    if position: 
        return Liste_cdc,Liste_pos
    else : 
        return Liste_cdc

def ADN_To_prot(seq):
    """Permet de transformer une séquence d'ADN en ARN puis en une chaine d'acides aminées""" 
    ADN=Seq(seq)
    ARN=ADN.transcribe()
    prot=ARN.translate(to_stop = True,stop_symbol="*")
    return prot

def gene(seq): 
    """Fonction qui prend en argument une séquence nucléotidique et qui renvoie un booléen si on peut considéré la séquence comme un gène ou non"""
    seq=ADN_To_prot(seq)
    if len(seq)>=50: 
        return True 
    return False 



################################
### Intégration des fonction ###
################################

def extract_Fasta(nom): 
    """Fonction qui appele plusieurs fonctions pour ouvrir nettoyer et mettre en une ligne une séquence au format FASTA et qui renvoie la chaine de caractère"""
    d=load_Fasta(nom)
    data=nettoyage(d)
    data=Lignes_To_Ligne(data)
    return data

def extract_MultiFasta(nom): 
    """Fonction qui appele plusieurs fonctions pour ouvrir nettoyer et mettre en une ligne les séquence au format FASTA et qui renvoie un dictionnaire dont les clées sont les noms des séquences et la valeur la chaine de caractère qui lui est associée"""
    d=load_Fasta(nom)
    data=nettoyage(d)
    data=split_Multi_Fasta(data)
    return data