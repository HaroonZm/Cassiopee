# Lecture de la liste des entiers saisis séparés par des espaces
liste_entiers_saisis = list(map(int, input().split()))

# Tri de la liste des entiers pour obtenir l'ordre croissant
liste_entiers_tries = sorted(liste_entiers_saisis)

# Calcul de la différence maximale entre le plus grand et le plus petit entier de la liste triée
difference_maximale = liste_entiers_tries[2] - liste_entiers_tries[0]

# Affichage du résultat
print(difference_maximale)