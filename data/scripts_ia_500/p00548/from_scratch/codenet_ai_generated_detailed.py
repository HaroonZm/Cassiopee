import sys
input = sys.stdin.readline

# On lit les données d'entrée
N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# dp[i] va contenir le coût minimal pour empaqueter les oranges de 1 à i (1-based)
# Nous allons utiliser une liste de taille N+1 pour faciliter les indices (0 à N)
dp = [float('inf')] * (N + 1)
dp[0] = 0  # Aucun coût pour empaqueter 0 orange

# Pour chaque position i, on regarde les groupes possibles de oranges derrière, jusqu'à M
# et on calcule le coût de cette boîte et on met à jour dp[i]
for i in range(1, N + 1):
    max_orange = -float('inf')  # pour suivre la taille maximale dans la boîte
    min_orange = float('inf')   # pour suivre la taille minimale dans la boîte

    # On regarde toutes les tailles possibles de la boîte (de 1 à M), mais on ne dépasse pas le début (i-j >= 0)
    for j in range(1, min(M, i) + 1):
        orange_size = A[i - j]
        if orange_size > max_orange:
            max_orange = orange_size
        if orange_size < min_orange:
            min_orange = orange_size

        # Le coût de cette boîte est K + s * (a - b), s = j ici
        cost = K + j * (max_orange - min_orange)

        # On met à jour dp[i] avec le coût minimum en combinant dp[i-j] (le coût des oranges précédentes)
        if dp[i - j] + cost < dp[i]:
            dp[i] = dp[i - j] + cost

# Le résultat final est le coût minimal pour empaqueter toutes les oranges (de 1 à N)
print(dp[N])