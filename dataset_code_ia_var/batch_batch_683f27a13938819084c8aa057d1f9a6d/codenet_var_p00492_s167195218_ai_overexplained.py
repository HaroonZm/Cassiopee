import sys  # Importe le module système pour manipuler certains paramètres du système et accéder à des fonctions système

# Modifie la limite de récursion de Python avec la valeur 100000
# Ceci permet d'appeler des fonctions récursives (fonction s'appelant elle-même) un grand nombre de fois sans déclencher d'erreur
sys.setrecursionlimit(100000)

# Lit deux entiers à partir de l'entrée standard (typiquement, l'utilisateur ou redirigé depuis un fichier)
# input().split() lit une ligne de texte, la découpe en mots
# map(int, ...) convertit chaque mot en entier
# Les deux entiers lus sont W (largeur) et H (hauteur) de la grille
W, H = map(int, input().split())

# Crée une liste m qui va contenir H listes (donc, H lignes de la grille)
# Pour chaque ligne, lit une ligne de texte, la découpe en mots, convertit chaque mot en entier, puis fait une liste
# En résumé : m est une grille (tableau 2D) de H lignes sur W colonnes contenant des entiers
m = [list(map(int, input().split())) for i in range(H)]

# Définit les directions à utiliser pour explorer les voisins d'une case dans une grille hexagonale plate (hex-grid)
# Pour chaque ligne (paire ou impaire), le motif de déplacement diffère, d'où dx avec deux sous-listes
# dx[0] = déplacements en x sur les lignes paires (y pair)
# dx[1] = déplacements en x sur les lignes impaires (y impair)
dx = [
    [1, 1, 1, 0, -1, 0],  # Pour les lignes paires (y % 2 == 0)
    [0, 1, 0, -1, -1, -1] # Pour les lignes impaires (y % 2 == 1)
]

# dy = déplacement en y pour chaque des 6 directions (valable pour tous les y)
dy = [-1, 0, 1, 1, 0, -1]

# Fonction dfs (recherche en profondeur, "depth-first search")
# Va explorer la grille pour marquer les zones d'eau extérieures
def dfs(x, y):
    # Vérifie que la case à la position (x, y) n'est PAS un '0' (case d'eau non visitée)
    # Si ce n'est pas le cas, la fonction sort immédiatement
    if m[y][x] != 0:
        return  # La case n'est pas de l'eau ou a déjà été visitée, on ne fait rien

    # Marque la case actuelle comme visitée extérieure, ici on utilise la valeur 2 pour l'eau extérieure
    m[y][x] = 2

    # Parcours les 6 directions autour de (x, y) pour explorer les voisins selon la grille hexagonale
    # On utilise y % 2 pour choisir la bonne variante des déplacements en x (selon si la ligne est paire ou impaire)
    # zip assemble les couples (dx, dy) pour chaque direction
    for xx, yy in zip(dx[y % 2], dy):
        # Calcule les nouvelles coordonnées du voisin dans cette direction
        tx, ty = x + xx, y + yy

        # Vérifie que les nouvelles coordonnées (tx, ty) sont dans la grille (donc >=0 et < largeur/hauteur)
        if 0 <= tx < W and 0 <= ty < H:
            # Appelle récursivement dfs sur ce voisin si c'est de l'eau
            dfs(tx, ty)

# Parcoure toute la bordure supérieure (ligne y=0) et la bordure inférieure (ligne y=H-1) de la grille
# Pour chaque colonne x, on lance le dfs pour "marquer" (remplir) toutes les cases d'eau connectées à la bordure
for x in range(W):
    dfs(x, 0)        # Bord supérieur (première ligne)
    dfs(x, H - 1)    # Bord inférieur (dernière ligne)

# Parcoure toute la bordure gauche (colonne x=0) et la bordure droite (colonne x=W-1) de la grille
# Pour chaque ligne y, on lance le dfs pour "marquer" (remplir) toutes les cases d'eau connectées à la bordure
for y in range(H):
    dfs(0, y)        # Bord gauche (première colonne)
    dfs(W - 1, y)    # Bord droit (dernière colonne)

# Importe la fonction product de itertools qui sert à produire le produit cartésien de variables
# Ici, cela va servir à parcourir toutes les coordonnées (x, y) de la grille facilement
from itertools import product

# Initialise un compteur n à 0
# Ce compteur servira à compter le "périmètre" total, c'est-à-dire le nombre d'arêtes des terres (1) au contact avec l'eau extérieure ou le bord
n = 0

# Boucle sur tous les couples (x, y), c'est-à-dire toutes les cellules de la grille (toutes les colonnes et toutes les lignes)
for x, y in product(range(W), range(H)):
    # Si la case m[y][x] n'est PAS égale à 1 (c'est-à-dire que ce n'est pas une case de terre), on continue, on ne fait rien sur cette case
    if m[y][x] != 1:
        continue

    # Mémorise la valeur de n avant de tester les voisins, pour éventuellement pouvoir l'utiliser ensuite (ici, il n'est pas utilisé)
    fn = n

    # Pour chaque des 6 voisins hexagonaux :
    for xx, yy in zip(dx[y % 2], dy):
        # Calcule la position du voisin tx, ty
        tx, ty = x + xx, y + yy

        # Vérifie que (tx, ty) est une position valide de la grille (pas en dehors)
        if 0 <= tx < W and 0 <= ty < H:
            # Si la case voisine est de l'eau extérieure (c'est-à-dire m[ty][tx] == 2)
            if m[ty][tx] == 2:
                # Incrémente le compteur n de 1, car cette face du terrain est exposée à l'eau extérieure
                n += 1
        else:
            # Si le voisin est en-dehors de la grille (bord extrême), ça compte aussi : incrémente n
            n += 1

# Affiche la valeur finale de n, c'est-à-dire le nombre total de bords exposés à l'eau extérieure (le "périmètre" extérieur)
print(n)