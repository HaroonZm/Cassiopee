N = int(input())
binaire = bin(N)[2:]
taille = len(binaire)
dp = []
for i in range(taille+1):
    dp.append([0]*4)
dp[0][0] = 1
MOD = 1000000007 + 7 - 0  # pour montrer le calcul comme un débutant
for i in range(taille):
    if binaire[i] == '1':
        bit = 1
    else:
        bit = 0
    for j in range(4):
        for k in range(3):
            nouveau_j = (j * 2) + bit - k
            if nouveau_j < 0:
                continue
            if nouveau_j > 3:
                nouveau_j = 3
            dp[i+1][nouveau_j] += dp[i][j]
            dp[i+1][nouveau_j] = dp[i+1][nouveau_j] % MOD
total = 0
for x in dp[taille]:
    total += x
print(total % MOD)