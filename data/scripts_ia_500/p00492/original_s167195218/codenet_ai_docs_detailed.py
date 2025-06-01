import sys

# Augmente la limite maximale de récursion pour permettre des appels récursifs profonds
sys.setrecursionlimit(100000)

# Lecture des dimensions de la grille : largeur W et hauteur H
W, H = map(int, input().split())

# Lecture de la grille HxW composée de valeurs entières (0, 1, etc.)
m = [list(map(int, input().split())) for i in range(H)]

# Déplacements possibles en x selon la ligne (pair ou impair) pour un hexagone ou grille spécifique
dx = [[1, 1, 1, 0, -1, 0],  # Décalages en x si la ligne y est paire (y%2 == 0)
      [0, 1, 0, -1, -1, -1]] # Décalages en x si la ligne y est impaire (y%2 == 1)

# Déplacements possibles en y (identiques pour tous les y)
dy = [-1, 0, 1, 1, 0, -1]

def dfs(x, y):
    """
    Effectue une recherche en profondeur (DFS) pour marquer toutes les cellules accessibles 
    à partir de la cellule (x, y) qui ont la valeur 0 dans la grille m.
    
    Cette fonction remplace la valeur 0 par 2 pour indiquer que la cellule a été visitée.
    Elle explore récursivement les 6 voisins possibles, adaptés à un système de coordonnées hexagonales.
    
    Arguments:
    x -- coordonnée en x (colonne)
    y -- coordonnée en y (ligne)
    """
    # Si la cellule n'est pas 0, on ne fait rien (cas base)
    if m[y][x] != 0:
        return
    # Marque la cellule comme visitée en remplaçant 0 par 2
    m[y][x] = 2
    # Parcourt les 6 voisins possibles en fonction de la parité de la ligne y
    for xx, yy in zip(dx[y % 2], dy):
        tx, ty = x + xx, y + yy
        # Vérifie que le voisin est dans la grille
        if 0 <= tx < W and 0 <= ty < H:
            # Appelle récursivement dfs sur le voisin
            dfs(tx, ty)

# Effectue un DFS sur toutes les cellules de la bordure (top et bottom)
for x in range(W):
    dfs(x, 0)         # bord supérieur
    dfs(x, H - 1)     # bord inférieur

# Effectue un DFS sur toutes les cellules des bordures gauche et droite
for y in range(H):
    dfs(0, y)         # bord gauche
    dfs(W - 1, y)     # bord droit

from itertools import product

# Initialise le compteur des 'frontières' détectées
n = 0

# Parcourt toutes les positions (x,y) dans la grille
for x, y in product(range(W), range(H)):
    # Ignore les cellules qui ne valent pas 1
    if m[y][x] != 1:
        continue
    # Variable temporaire non utilisée dans ce code, pourrait être retirée
    fn = n
    # Vérifie tous les voisins de la cellule (x,y)
    for xx, yy in zip(dx[y % 2], dy):
        tx, ty = x + xx, y + yy
        # Si voisin dans grille et valeur 2 (zone accessible marquée)
        if 0 <= tx < W and 0 <= ty < H:
            if m[ty][tx] == 2:
                n += 1  # Incrémente la frontière détectée
        else:
            # Si le voisin est hors de la grille, c'est aussi une frontière
            n += 1

# Affiche le nombre total de frontières détectées
print(n)