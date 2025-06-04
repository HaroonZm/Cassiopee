# Lecture des entrées et définition de la grille
H, W = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(H)]

# Initialisation d'une matrice dp où dp[i][j] contient le nombre minimal de cigales rencontrées
# pour atteindre la case (i, j) depuis (0, 0)
dp = [[float('inf')] * W for _ in range(H)]

# La case de départ (la maison) ne contient pas de cigales
dp[0][0] = 0

# Remplissage de la première ligne (on ne peut que venir de la gauche)
for j in range(1, W):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# Remplissage de la première colonne (on ne peut que venir d'en haut)
for i in range(1, H):
    dp[i][0] = dp[i-1][0] + grid[i][0]

# Remplissage du reste du dp
for i in range(1, H):
    for j in range(1, W):
        # Le nombre minimal de cigales pour atteindre (i,j) est le minimum entre
        # venir du dessus (i-1, j) ou venir de gauche (i, j-1) plus le nombre de cigales à (i,j)
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# Le résultat est dans la case de l'école (en bas à droite)
print(dp[H-1][W-1])