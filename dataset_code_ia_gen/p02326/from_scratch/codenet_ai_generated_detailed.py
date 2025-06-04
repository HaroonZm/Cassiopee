# Lecture de l'entrée et mise en place de la matrice
H, W = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]

# On va utiliser une programmation dynamique pour résoudre le problème.
# L'idée est de créer une matrice dp de même taille que la matrice d'entrée,
# où dp[i][j] représente la taille du plus grand carré de zéros dont le coin inférieur droit est à la position (i, j).

# Initialisation de la matrice dp avec des zéros
dp = [[0]*W for _ in range(H)]

# Variable pour garder la taille maximale du carré trouvé
max_side = 0

# Parcours de chaque élément de la matrice pour remplir dp
for i in range(H):
    for j in range(W):
        # Si la valeur à la position (i, j) est 0, on peut potentiellement former un carré
        if matrix[i][j] == 0:
            if i == 0 or j == 0:
                # En bordure, le plus grand carré est de taille 1 si c'est un 0
                dp[i][j] = 1
            else:
                # Sinon, on regarde les voisins (gauche, haut, diagonale haut-gauche)
                # Le plus grand carré possible est le minimum de ces 3 voisins + 1
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            # Mise à jour de la taille maximale
            if dp[i][j] > max_side:
                max_side = dp[i][j]

# L'aire du plus grand carré est le carré de la taille maximale
print(max_side * max_side)