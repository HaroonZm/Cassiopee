entiers_saisis = [int(valeur_saisie) for valeur_saisie in input().split()]

entiers_saisis.sort()

premier_entier = entiers_saisis[0]
deuxieme_entier = entiers_saisis[1]
troisieme_entier = entiers_saisis[2]

deux_entiers_egaux_uniquement = (premier_entier == deuxieme_entier and deuxieme_entier != troisieme_entier) or (premier_entier != deuxieme_entier and deuxieme_entier == troisieme_entier)

if deux_entiers_egaux_uniquement:
    print("Yes")
else:
    print("No")