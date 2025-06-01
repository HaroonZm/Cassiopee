import math

nombre_entrees = 5
valeurs_saisies = [int(input()) for index_entree in range(nombre_entrees)]

temps_initial = valeurs_saisies[0]
valeur_deuxieme_entree = valeurs_saisies[1]
valeur_troisieme_entree = valeurs_saisies[2]
valeur_quatrieme_entree = valeurs_saisies[3]
valeur_cinquieme_entree = valeurs_saisies[4]

temps_necessaire_premier_calcul = math.ceil(valeur_deuxieme_entree / valeur_quatrieme_entree)
temps_necessaire_deuxieme_calcul = math.ceil(valeur_troisieme_entree / valeur_cinquieme_entree)

temps_necessaire_maximum = sorted([temps_necessaire_premier_calcul, temps_necessaire_deuxieme_calcul])[-1]

resultat_final = temps_initial - temps_necessaire_maximum

print(resultat_final)