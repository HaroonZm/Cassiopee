n, m = map(int, input().split())

# Création du graphe avec des zéros
g = []
for i in range(n):
    ligne = []
    for j in range(n):
        ligne.append(0)
    g.append(ligne)

# Ajout des arêtes
for i in range(m):
    u, v, w = map(int, input().split())
    g[u - 1][v - 1] = w
    g[v - 1][u - 1] = w

# Calcul du tableau e
e = []
for S in range(1 << n):
    total = 0
    for i in range(n):
        if (S >> i) & 1:
            for j in range(i + 1, n):
                if (S >> j) & 1:
                    total += g[i][j]
    e.append(total)

# Initialisation du tableau dp
dp = []
for i in range(1 << n):
    d = []
    for j in range(n):
        d.append(-1000000000)
    dp.append(d)

for i in range(1 << n):
    for j in range(n):
        if (i >> j) & 1:
            if j == 0:
                dp[i][j] = e[i]
            else:
                for k in range(n):
                    if j != k and ((i >> k) & 1) and g[k][j]:
                        temp = dp[i ^ (1 << j)][k] + g[k][j]
                        if temp > dp[i][j]:
                            dp[i][j] = temp
                s = i ^ (1 << j)
                k = s
                while k:
                    temp = dp[i ^ k][j] + e[(k | (1 << j))]
                    if temp > dp[i][j]:
                        dp[i][j] = temp
                    k = (k - 1) & s

resultat = e[(1 << n) - 1] - dp[(1 << n) - 1][n - 1]
print(resultat)