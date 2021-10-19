import os 
chemin=os.chdir("C:/Users/Tom/Documents/Cours/Polytech/4A/4A/S1/Progra_Script/Modules")
import md_genom as my_md
import md_affichage as aff
##Faire en sort que ça recherche le fichier 
chemin=os.chdir("C:/Users/Tom/Documents/Cours/Polytech/4A/4A/S1/Progra_Script/TD1")

################################
### import et nettoyage data ###
################################

aff.fenetre("Choix fichier")

try :
    data=my_md.extract_Fasta(aff.F[-1])
    # d=my_md.load_Fasta(aff.F[-1])
    # data=my_md.nettoyage(d)
    # data=my_md.Lignes_To_Ligne(data)
    taille= len(data)

except : 
    aff.fenetre("Fichier inutilisable, réessayer")

############################
### Utilisation de data ###
###########################
dico=my_md.dicodinucléotides()

for pos_nucl in range(len(data)-1) :
    dico[data[pos_nucl]+data[pos_nucl+1]][0]+=1         #Retrouve pour chaque indice et l'indice du suivant le dinucléotide associé dans le dico et ajoute 1 au nombre d'occurence

for dinu in dico : 
    dico[dinu][1]=my_md.freq(dico[dinu][0],taille)      #calcul la fréquence à partir du premier élément de la liste du dico

GC=my_md.GC(my_md.occurence("G",data)+my_md.occurence("C",data),taille)
A,T,G,C=my_md.occurence("A", data),my_md.occurence("T",data),my_md.occurence("G",data),my_md.occurence("C",data)

ORF = my_md.rechREsimple("ATG", data,position=False)
Liste_prot=[]
for orf in ORF : 
    Liste_prot.append(my_md.ADN_To_prot(orf)+"*")

################################
### Ecriture nouveau fichier ###
################################
#crée un fichier résultat/output
liste_sortie=my_md.From_Dico_To_List(dico)
my_md.fichier_sortie(GC,"results","txt",A,T,G,C,Liste_prot) 
my_md.fichier_sortie_dinu_csv(liste_sortie,"resultat")


aff.fenetre_fin("Les fichiers ont été crés et placés dans le même dossier que le programme \nCliquer sur quiter pour terminé le programme")
#input("les fichier a été crée et placé dans le même dossier que le programme \nTaper sur entrée pour terminé le programme")

