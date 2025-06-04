n, k, m = map(int, input().split())

# dp[i][x][y]: le nombre de façons de remplir les colonnes de 0 à i,
# avec x et y les valeurs des cellules haut et bas à la colonne i (1-based)
# en respectant les contraintes et la monotonie strictement croissante

# On note que les valeurs possibles pour chaque cellule vont de 1 à 2n
MAX = 2 * n + 1

dp = [[[0] * MAX for _ in range(MAX)] for _ in range(n)]
# Pour la première colonne, on essaie toutes paires (x,y) avec x < y et y-x <= k
for x in range(1, MAX):
    for y in range(1, MAX):
        if x < y and y - x <= k:
            dp[0][x][y] = 1

for i in range(1, n):
    for x in range(1, MAX):
        for y in range(1, MAX):
            if x >= y:
                continue
            if y - x > k:
                continue
            ways = 0
            # Le précédent couple (px, py) doit être < (x, y) dans le sens strictement croissant pour chaque cellule
            # Aussi, les valeurs adjacentes (haut-droite et bas-droite) doivent avoir différence <= k
            for px in range(1, MAX):
                for py in range(1, MAX):
                    if px >= py:
                        continue
                    if py - px > k:
                        continue
                    # vérifier contraintes entre colonnes adjacentes:
                    # x > px et |x - px| <= k
                    if not (px < x and abs(x - px) <= k):
                        continue
                    # y > py et |y - py| <= k
                    if not (py < y and abs(y - py) <= k):
                        continue
                    ways += dp[i-1][px][py]
            dp[i][x][y] = ways % m

# Calcul du résultat final : somme de dp[n-1][x][y] pour tous x,y valides avec x<y et y - x <= k
result = 0
for x in range(1, MAX):
    for y in range(1, MAX):
        if x < y and y - x <= k:
            result = (result + dp[n-1][x][y]) % m

print(result)