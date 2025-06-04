# Demande à l'utilisateur d'entrer deux entiers séparés par un espace
# Ces deux entiers seront stockés respectivement dans les variables n et m
# n représente probablement une longueur, une limite, ou la fin d'un segment
# m représente le nombre d'éléments ou de points à considérer par la suite
n, m = map(int, input().split(" "))

# Demande ensuite à l'utilisateur d'entrer m entiers, séparés par des espaces
# Ces entiers représentent une liste de positions dans un intervalle de 1 à n
# Ils sont stockés dans la variable a sous la forme d'une liste d'entiers
a = list(map(int, input().split(" ")))

# Calculons différentes distances pour déterminer la plus grande séparation possible ou optimale

# Première possibilité :
# a[0] - 1
# Cela calcule la distance entre le début du segment (qui est 1 car les positions commencent à 1)
# et la première position occupée indiquée dans 'a'
premiere_distance = a[0] - 1

# Deuxième possibilité :
# n - a[-1]
# Cela calcule la distance entre la dernière position occupée indiquée dans 'a' (a[-1])
# et la fin du segment, c'est-à-dire la position n
derniere_distance = n - a[-1

# Troisième possibilité :
# Pour chaque paire consécutive dans la liste, calcule la moitié de la distance entière
# Sélectionne les indices de 0 jusqu'à m-2, c'est-à-dire toutes les paires (a[i], a[i+1])
# Pour chaque paire, a[i+1] - a[i] donne la distance entre deux positions consécutives
# On utilise la division entière '//' pour obtenir la moitié sans décimales (arrondi vers le bas)
distances_entre_points = []
for i in range(m - 1):
    # Calcul de la demi-distance entière (distance entre deux points / 2)
    demi_distance = (a[i+1] - a[i]) // 2
    # Ajoute le résultat à la liste des demi-distances
    distances_entre_points.append(demi_distance)

# Enfin, on utilise la fonction max pour trouver la distance maximale possible parmi :
# - la distance entre le début du segment et le premier point (premiere_distance)
# - la distance entre le dernier point et la fin du segment (derniere_distance)
# - toutes les demi-distances entre chaque paire consécutive (avec l'opérateur *, on étale la liste)
resultat = max(premiere_distance, derniere_distance, *distances_entre_points)

# Affiche le résultat final sur la sortie standard (console)
print(resultat)