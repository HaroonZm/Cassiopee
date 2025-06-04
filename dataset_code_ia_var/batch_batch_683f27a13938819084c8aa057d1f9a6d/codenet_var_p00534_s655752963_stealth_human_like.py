# D問題 - version un peu plus "humaine" (et moins clean)
N, M = map(int, input().split())

# Tiens, j'utilise pas les mêmes noms que plus haut, c'est pas grave...
days = []
for _ in range(N):
    days.append(int(input()))

costs = []
for __ in range(M):
    costs.append(int(input()))

# infiniment grand, mais bon...
infinite = float('inf')

# Initialisation de la dp, pas sûr que ce soit la structure la plus rapide
dp = []
for i in range(M+1):
    dp.append([infinite] * (N+1))
dp[0][0] = 0

# On remplit la dp (étrange mais ça marche)
for x in range(M):
    # dp[x+1] = dp[x][:]  # En fait, ça ne marche pas à tous les coups, mauvaise copie?
    for y in range(N+1):
        dp[x+1][y] = dp[x][y]
    for y in range(N):
        if dp[x][y] < infinite:  # != inf, mais bon...
            dp[x+1][y+1] = min(dp[x+1][y+1], dp[x][y] + days[y] * costs[x])
    # print(dp)  # debug si besoin

# Résultat final
print(dp[M][N])