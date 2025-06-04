# On lit quatre entiers depuis l'entrée standard (input)
# La méthode input() lit une ligne de texte entrée par l'utilisateur.
# La méthode split() sépare cette ligne de texte en morceaux, en utilisant l'espace comme séparateur (par défaut).
# La fonction map applique la conversion int à chaque morceau, c'est-à-dire qu'elle prend chaque sous-chaîne et la convertit en entier.
# Enfin, on utilise l'affectation multiple pour stocker ces quatre entiers dans les variables a, b, c et d respectivement.
a, b, c, d = map(int, input().split())

# On définit une constante nommée mod et on l'initialise à la valeur 998244353.
# Cette constante est généralement utilisée pour effectuer des opérations modulo, afin d'éviter les débordements d'entiers et de rester dans une plage d'entiers gérable.
# 'mod' est souvent utilisée dans les problèmes d'arithmétique modulaire et de programmation compétitive.
mod = 998244353

# On prépare une structure de données appelée 'DP'.
# Ici, 'DP' est une liste de listes (c'est-à-dire une matrice à deux dimensions).
# La compréhension de liste externe parcourt les valeurs de 0 à c inclus (c+1 au total), car on veut avoir des indices de 0 à c.
# Pour chaque ligne de cette matrice, on crée une liste (ligne) de taille d+1 remplie de zéro (car [0] * (d+1) fait une liste de d+1 zéros).
# De cette manière, DP[y][x] accèdera à la cellule de la ligne y et de la colonne x (0-based index).
DP = [[0] * (d+1) for _ in range(c+1)]

# On initialise une cellule spécifique de la table DP : celle correspondant à la ligne a et la colonne b.
# L’idée ici est de poser l’état de base (valeur initiale) de notre programme dynamique.
# On positionne DP[a][b] à 1, car il y a précisément une manière de construire une "tableau" de a lignes et b colonnes dans le contexte du problème (selon la situation posée à l'origine).
DP[a][b] = 1

# On remplit la première colonne d'intérêt (colonne b) pour toutes les lignes de y = a+1 jusqu'à y = c inclus.
# range(a+1, c+1) génère les entiers de a+1 à c inclus.
# A chaque itération, DP[y][b] est calculé à partir de DP[y-1][b], en multipliant par b (le nombre de colonnes).
# On applique aussi le modulo mod pour garder la valeur dans la fourchette voulue.
for y in range(a+1, c+1):
    DP[y][b] = DP[y-1][b] * b % mod

# On remplit la première ligne d'intérêt (ligne a) pour toutes les colonnes de x = b+1 jusqu'à x = d inclus.
# C'est analogue à la boucle précédente, mais on avance horizontalement sur la première ligne.
# Pour chaque colonne supplémentaire à partir de b+1, la valeur dépend de la colonne précédente (x-1), multipliée par a (le nombre de lignes fixes).
# On utilise également le modulo pour contrôler la croissance des valeurs.
for x in range(b+1, d+1):
    DP[a][x] = DP[a][x-1] * a % mod

# Maintenant, on remplit le reste de la matrice DP, c'est-à-dire toutes les cellules DP[y][x] pour y entre a+1 à c et x entre b+1 à d.
# Il s'agit d'une double boucle imbriquée (une sur les lignes, une sur les colonnes).
# Les indices commencent à a+1 parce que les lignes et colonnes précédentes ont été remplies dans les boucles précédentes.
for y in range(a+1, c+1):
    for x in range(b+1, d+1):
        # Pour chaque cellule DP[y][x], la valeur est calculée selon une formule complexe,
        # qui utilise différentes cellules déjà calculées de la matrice DP.
        # La formule fait intervenir 3 éléments principaux :
        # 1. DP[y-1][x] * x : On ajoute une nouvelle ligne à un tableau de hauteur y-1, le tout multiplié par x colonnes,
        #    car il y a x possibilités pour le nouvel élément.
        # 2. (DP[y][x-1] - DP[y-1][x-1] * (x-1)) * y :
        #    On ajoute une nouvelle colonne à la hauteur y, en évitant les double comptages puisqu'on retire un certain terme pour ajuster.
        # 3. DP[y-1][x-1] * (x-1) : On corrige un surcompte éventuel provenant de deux opérations précédentes.
        # Toute la somme est prise modulo 'mod' pour contrôler la taille de la valeur.
        DP[y][x] = (DP[y-1][x] * x + (DP[y][x-1] - DP[y-1][x-1] * (x-1)) * y + DP[y-1][x-1] * (x-1)) % mod

# Après avoir rempli toute la matrice DP, on affiche la valeur contenue dans DP[c][d],
# c'est-à-dire la dernière cellule correspondant à la taille finale désirée du tableau (ou structure du problème).
# La fonction print() affiche le résultat à l’écran.
print(DP[c][d])