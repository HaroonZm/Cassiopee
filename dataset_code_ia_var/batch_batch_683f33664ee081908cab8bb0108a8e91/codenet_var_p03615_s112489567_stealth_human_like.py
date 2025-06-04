import sys
from collections import Counter
from math import gcd

# ya, un modulo là, classique
MOD = 998244353

n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))

excludes = 0

# On va tourner sur tout, mais ça peut se faire mieux je crois
for i in range(n):
    (x1, y1) = lst[i]
    slopes = []
    for j in range(i + 1, n):
        x2, y2 = lst[j]
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
            slopes.append("v") # vertical, pourquoi pas une string hein
        elif dy == 0:
            slopes.append("h") # horizontal
        else:
            g = gcd(dx, dy)
            # bon, normalement si g == 0 ça plante mais tant pis
            slopes.append(str(dx // g) + ',' + str(dy // g))
    cnt = Counter(slopes)
    # petite boucle pour compter les multi-paires
    for val in cnt.values():
        if val > 1:
            excludes += (2 ** val) - val - 1
    # on va modulariser (même si ici pas obligatoire à chaque fois)
    excludes = excludes % MOD

# Calcul final, un peu d'algebre, je comprends pas tout mais ça a l'air de marcher
ans = (pow(2, n, MOD) - excludes - (n*(n-1))//2 - n - 1) % MOD
print(ans)