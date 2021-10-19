import os 
chemin=os.chdir("C:/Users/Tom/Documents/Cours/Polytech/4A/4A/S1/Progra_Script/Modules")
import md_genom as my_md
import md_prot as my_md_p
chemin=os.chdir("C:/Users/Tom/Documents/Cours/Polytech/4A/4A/S1/Progra_Script/TD2")

data=my_md_p.load("1BTA.pdb")
data=my_md.nettoyage(data)
atom=my_md_p.atome(data)
C_a = my_md_p.carbone_alpha(atom)
nb=my_md_p.nombre_Aa(atom)
code_3L=my_md_p.code3L(atom)
code_1L=my_md_p.code3L_To_code1L(code_3L)
my_md_p.from_PDB_To_fasta("résultat",data,code_1L)
input("les fichier a été crée et placé dans le même dossier que le programme \nTaper sur entrée pour terminé le programme")