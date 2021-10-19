from Bio.PDB.Polypeptide import three_to_one

def load(fichier):
    L=[]
    f = open(fichier)
    cdc=f.readline()
    while cdc!="": 
        L.append(cdc)
        cdc=f.readline()
    return L

def atome(data): 
    liste_atome=[]
    for ligne in data :
        if ligne[:4]=="ATOM" or ligne[:3]=="TER": 
            liste_atome.append(ligne)
    return liste_atome

def carbone_alpha(data): 
    liste_Ca=[]
    for ligne in data : 
        if "CA" in ligne and "ATOM   " in ligne : 
            liste_Ca.append(ligne)
    return liste_Ca

def nombre_Aa(data):
    resultat=data[-1].split()
    return resultat[3]

def code3L(data):
    numero=0
    code3L=""
    for ligne in data[1:-1]: 
        ligne=ligne.split()
        if numero!=ligne[4]: 
            numero=ligne[4]
            code3L+=ligne[3] + "-"
    return code3L[:-1]

def code3L_To_code1L(code): 
    code_1L=""
    liste=code.split("-")
    for lettre in liste : 
        code_1L+=three_to_one(lettre)
    return code_1L

def from_PDB_To_fasta(nomFile,data,code,nb_lettre_par_ligne=50): 
    str(nomFile)
    nom=nomFile+'.txt' 
    f=open(nom, "w")
    f.write(data[0]+"\n")
    for i in range(1,len(code),nb_lettre_par_ligne):
        f.write(code[i:i+nb_lettre_par_ligne]+"\n")
    f.close()
        