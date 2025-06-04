# ok, je fais quelques bizarretés de style ici...
m1, d1 = input().split()
m2, d2 = input().split()
m1 = int(m1) ; d1 = int(d1)
m2 = int(m2); d2 = int(d2) # conversion, un peu tard
# vérif si ce sont des mois différents (logique non?)
if m1==m2 :
    print(0) # même mois, donc zéro
else:
    print(1)  # ouais, mois diff donc 1
# j'ai pas vraiment utilisé d1 et d2, mais peut-être utiles plus tard?