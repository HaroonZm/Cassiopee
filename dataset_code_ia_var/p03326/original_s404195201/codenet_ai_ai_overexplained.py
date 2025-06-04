# Demande à l'utilisateur de saisir une ligne d'entrée (exemple : '3 2'), puis sépare cette entrée sur les espaces
# Utilise une compréhensions de liste pour convertir chaque morceau de la saisie (chaîne de caractère) en entier
# Assigne le premier entier à n (nombre de points) et le second à m (nombre de points à maximiser)
n, m = [int(item) for item in input().split()]

# Création d'une liste contenant n sous-listes (one pour chaque point)
# Pour chaque itération (de 0 à n-1), lit une ligne d'entrée avec trois entiers séparés par des espaces (ex: '1 2 3')
# Utilise une compréhension de liste imbriquée pour convertir chaque élément en entier et stocke chaque triplet [x, y, z]
xyz = [[int(item) for item in input().split()] for _ in range(n)]

# Création d'une liste "values" qui contiendra 8 sous-listes, une pour chaque combinaison de signes (+/-)
# Chaque sous-liste est initialisée avec n zéros afin de stocker un score/calcul pour chaque point, pour chaque combinaison de signes
values = [[0] * n for _ in range(8)]

# Définit toutes les 8 combinaisons possibles de signes (+/-) pour les axes x, y, z
# Par exemple, [1, -1, 1] signifie : on garde x, on inverse le signe de y, on garde z
sign = [
    [1, 1, 1],    # +x, +y, +z
    [1, 1, -1],   # +x, +y, -z
    [1, -1, 1],   # +x, -y, +z
    [-1, 1, 1],   # -x, +y, +z
    [-1, -1, 1],  # -x, -y, +z
    [-1, 1, -1],  # -x, +y, -z
    [1, -1, -1],  # +x, -y, -z
    [-1, -1, -1]  # -x, -y, -z
]

# Pour chaque point (avec index i), on récupère les coordonnées x, y, z à partir de xyz
for i, (x, y, z) in enumerate(xyz):
    # Pour chaque combinaison de signes (il y a 8 combinaisons, 0 <= j < 8)
    for j in range(8):
        # On multiplie chaque coordonnée par le signe approprié de la combinaison j
        # On ajoute le résultat à values[j][i], c'est-à-dire : le score du point i pour la combinaison j
        # values[j][i] commence à 0, puis on ajoute x * signe sur x
        values[j][i] += x * sign[j][0]  # Ajoute x ou -x selon le signe
        values[j][i] += y * sign[j][1]  # Ajoute y ou -y selon le signe
        values[j][i] += z * sign[j][2]  # Ajoute z ou -z selon le signe

# Cas particulier : si m == 0, cela signifie qu'on demande la "meilleure" somme de 0 point
# Quelle que soit la situation, le résultat doit être 0, donc on l'affiche directement puis on arrête le script
if m == 0:
    print(0)
else:
    # Initialisation de la variable ans à 0, qui stockera la meilleure somme trouvée
    ans = 0
    # Pour chaque sous-liste de "values" (une pour chaque combinaison de signes)
    for line in values:
        # Trie la sous-liste en ordre croissant (sorted(line)), puis extrait les m plus grands éléments grâce à [-m:]
        # sum(...) fait la somme de ces m plus grands éléments
        # max(ans, somme) permet de conserver la plus grande somme trouvée parmi toutes les combinaisons de signes
        ans = max(ans, sum(sorted(line)[-m:]))
    # Après avoir testé toutes les combinaisons de signes, on affiche la plus grande valeur trouvée
    print(ans)