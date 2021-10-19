import os 
import re
chemin=os.chdir("C:/Users/Tom/Documents/Cours/Polytech/4A/4A/S1/Progra_Script/Modules")
import md_genom as my_md
#import md_prot as my_md_p
chemin=os.chdir("C:/Users/Tom/Documents/Cours/Polytech/4A/4A/S1/Progra_Script/TD2")

##Extraction data
d=my_md.load_Fasta("NC_000908.fna")
d=my_md.nettoyage(d)
d=my_md.Lignes_To_Ligne(d)

#1)
data, indexATG=my_md.rechREsimple("ATG",d)
nbATG=len(indexATG)
print(nbATG)

#2)
data_2, indexSTOP=my_md.rechREsimple("(TAA|TAG|TGA)",d)
nbSTOP=len(indexSTOP)
print(nbSTOP)

#3)    => voir mes_modules_génomiques
#4)
expression=re.compile("(TATA).{10,20}(A){3,5}")
data_expression, index_expression = my_md.rechREsimple(expression,d)
print(len(index_expression))

#5)
Liste_gene=[]
for orf in data : 
    if my_md.gene(orf): 
        Liste_gene.append(my_md.ADN_To_prot(orf)+"*")
print(Liste_gene)
        


