s = input()
t = input()
n = len(s)
m = len(t)
# On crée la matrice memo avec des valeurs initiales grandes
memo = []
for i in range(n + 1):
    ligne = []
    for j in range(m + 1):
        ligne.append(n + m)
    memo.append(ligne)

memo[0][0] = 0

# Boucle principale pour calculer le résultat
for i in range(n + m):
    for j in range(i + 1):
        k = i - j
        if 0 <= j < n and 0 <= k < m:
            if s[j] == t[k]:
                if memo[j+1][k+1] > memo[j][k]:
                    memo[j+1][k+1] = memo[j][k]
            else:
                if memo[j+1][k] > memo[j][k] + 1:
                    memo[j+1][k] = memo[j][k] + 1
                if memo[j][k+1] > memo[j][k] + 1:
                    memo[j][k+1] = memo[j][k] + 1
                if memo[j+1][k+1] > memo[j][k] + 1:
                    memo[j+1][k+1] = memo[j][k] + 1
        elif j == n and k < m:
            if memo[j][k+1] > memo[j][k] + 1:
                memo[j][k+1] = memo[j][k] + 1
        elif k == m and j < n:
            if memo[j+1][k] > memo[j][k] + 1:
                memo[j+1][k] = memo[j][k] + 1

print(memo[n][m])