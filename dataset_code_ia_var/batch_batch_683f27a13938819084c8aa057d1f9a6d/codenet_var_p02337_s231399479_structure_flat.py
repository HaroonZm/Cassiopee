import sys
sys.setrecursionlimit(10**7)

mod = 10**9 + 7

star = [[None] * 1001 for _ in range(1001)]
for i in range(1001):
    star[i][1] = 1
    star[i][i] = 1
    star[i][0] = 0

n, k = map(int, input().split())
ans = 0

stack = []
memo_done = set()
for i in range(k + 1):
    stack.append((n, i))

while stack:
    n0, k0 = stack[-1]
    # Invalide
    if n0 < k0:
        star[n0][k0] = 0
        stack.pop()
        continue
    # Déjà calculé
    if star[n0][k0] is not None:
        stack.pop()
        continue
    # On doit calculer les dépendances
    if (n0-1 >= 0 and k0-1 >= 0 and star[n0-1][k0-1] is None):
        stack.append((n0-1, k0-1))
        continue
    if (n0-1 >= 0 and star[n0-1][k0] is None):
        stack.append((n0-1, k0))
        continue
    # Toutes les dépendances sont prêtes
    left = 0 if n0-1 < 0 or k0-1 < 0 else star[n0-1][k0-1]
    right = 0 if n0-1 < 0 else star[n0-1][k0]
    star[n0][k0] = (left + k0 * right) % mod
    stack.pop()

for i in range(k + 1):
    ans = (ans + (0 if n < i else star[n][i])) % mod

print(ans)