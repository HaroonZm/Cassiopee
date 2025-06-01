n = int(input())
arr = list(map(int, input().split()))

# Initialisation du tableau DP, à 1 partout, parce que chaque élément seul vaut 1
dp = [[1 for _ in range(3)] for __ in range(n)]
max_len = 1

for i in range(n - 1):
    for j in range(3):
        if arr[i] != arr[i + 1]:
            # Si les éléments adjacents sont différents, on peut continuer dans la même catégorie j
            if dp[i + 1][j] < dp[i][j] + 1:
                dp[i + 1][j] = dp[i][j] + 1
        # Sinon, si on a pas dépassé la 3ème sous-séquence (j<2) et les éléments sont égaux
        if j < 2 and arr[i] == arr[i + 1]:
            if dp[i + 1][j + 1] < dp[i][j] + 1:
                dp[i + 1][j + 1] = dp[i][j] + 1

# Trouver la plus grande valeur dans dp
for row in dp:
    cur_max = max(row)
    if cur_max > max_len:
        max_len = cur_max

print(max_len)