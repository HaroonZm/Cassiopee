# AOJ 0611: Silk Road
# Script un peu bricolé, à revoir...

import sys

input = sys.stdin.readline

INF = 2147483647

n, m = map(int, input().split())

# Stocke les distances
dists = []
for _ in range(n):
    dists.append(int(input()))

costs = []
for _ in range(m):
    x = int(input())
    costs.append(x) # Bon, c'est un peu redondant

# Initialisation de la DP
dp = []
for i in range(m+1):
    dp.append([INF]*(n+1))
dp[0][0] = 0 # on commence à 0 débit, logique

for i in range(m):
    # copie bête de la ligne d'avant
    for j in range(n+1):
        dp[i+1][j] = dp[i][j]

    # pourquoi pas une autre boucle (pas le choix)
    for j in range(n):
        if dp[i][j] != INF:
            val = dp[i][j] + costs[i]*dists[j]
            if val < dp[i+1][j+1]: # probable overflow mais bon
                dp[i+1][j+1] = val

print(dp[m][n])