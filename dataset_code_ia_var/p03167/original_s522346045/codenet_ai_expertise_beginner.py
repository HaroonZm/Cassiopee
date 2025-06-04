MOD = 10 ** 9 + 7
H, W = map(int, input().split())

# On prépare le tableau avec des murs autour
a = []
a.append(["#"] * (W + 2))
for i in range(H):
    line = list(input())
    row = ["#"] + line + ["#"]
    a.append(row)
a.append(["#"] * (W + 2))

# Création du tableau dp pour compter les manières d'arriver à chaque case
dp = []
for i in range(H + 10):
    dp.append([0] * (W + 10))

dp[0][1] = 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if a[i][j] != "#":
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD

print(dp[H][W] % MOD)