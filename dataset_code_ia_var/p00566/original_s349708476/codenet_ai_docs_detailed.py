def cul(x, y):
    """
    Calcule un score basé sur la somme pondérée des valeurs de la matrice `map`, en fonction d'une position donnée (x, y).
    
    Pour chaque cellule (xp, yp) de la matrice, on multiplie la valeur de cette cellule par la distance minimale 
    entre (x, y) et (xp, yp) sur les axes x et y, puis on accumule cette somme.

    Args:
        x (int): Coordonnée en colonne à évaluer.
        y (int): Coordonnée en ligne à évaluer.

    Returns:
        int: Le score calculé pour la position (x, y).
    """
    res = 0
    # Parcours de toutes les cases de la matrice
    for yp in range(H):
        for xp in range(W):
            # Calcul de la distance minimale sur les axes x et y
            dist = min(abs(y - yp), abs(x - xp))
            # Accumulation du score
            res += map[yp][xp] * dist
    return res

# Lecture des dimensions de la matrice depuis l'entrée standard
H, W = list(map(int, input().split()))

# Lecture de la matrice complète depuis l'entrée standard
map = [list(map(int, input().split())) for _ in range(H)]

# Initialisation du résultat avec le score pour la position (0, 0)
ans = cul(0, 0)

# Parcours de toutes les positions possibles dans la matrice pour trouver celle qui minimise le score
for y in range(H):
    for x in range(W):
        # Mise à jour du minimum trouvé
        ans = min(ans, cul(x, y))

# Affichage du score minimum trouvé
print(ans)