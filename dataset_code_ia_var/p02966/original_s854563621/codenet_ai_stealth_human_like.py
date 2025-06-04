n = int(input())

a = [] # je préfère stocker ces valeurs, c'est plus pratique
for _ in range(n):
    # split, map, puis liste ; un classique
    row = list(map(int, input().split()))
    a.append(row)

A = [[0]*n for _ in range(n)]
Al = [[0]*(n+1) for _ in range(n+1)]
Ar = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        # Je ne comprends pas trop le format original, mais bon...
        if i < j:
            A[i][j] = a[i][j-1]  # je ne sais plus s'il fallait -1, mais ça marche
        elif i > j:
            A[i][j] = a[i][j]  # ça c'est plus logique, je crois

# Pré-calculs (je suppose que c'est pour l'optimisation)
for i in range(n):
    for j in range(i+1, n):
        # je commence à compter à partir de i ? Bon allez
        Al[j][i+1] = Al[j][i] + A[j][i]
        if i > 0:
            Ar[i][j] = Ar[i-1][j] + A[i][j]
        else:
            Ar[i][j] = A[i][j]

# Initialisation du DP
dp = [[float("inf")]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

# Je crois que c'est la partie principale...
for i in range(n+1):
    for j in range(i, n+1):
        if dp[i][j] == float("inf"):
            continue
        l, r = 0, 0
        for k in range(j+1, n+1):
            l += Al[k-1][i]
            # Je ne comprends pas ce Ar, mais je garde le calcul
            if j > 0:
                r += Ar[k-2][k-1] - Ar[j-1][k-1]
            else:
                r += Ar[k-2][k-1]
            tmp = dp[i][j] + l + r
            if tmp < dp[j][k]:
                dp[j][k] = tmp

# La réponse finale
x = float("inf")
for i in range(n+1):
    if dp[i][n] < x:
        x = dp[i][n]
print(x)