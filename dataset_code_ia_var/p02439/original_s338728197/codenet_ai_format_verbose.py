# Lire une ligne d'entrée utilisateur, la découper puis convertir chaque élément en entier
entiers_saisis = list(map(int, input().split()))

# Trier la liste d'entiers par ordre croissant
entiers_tries = sorted(entiers_saisis)

# Récupérer la valeur minimale et maximale de la liste triée
valeur_minimale = entiers_tries[0]
valeur_maximale = entiers_tries[-1]

# Afficher la valeur minimale puis la valeur maximale
print(valeur_minimale, valeur_maximale)