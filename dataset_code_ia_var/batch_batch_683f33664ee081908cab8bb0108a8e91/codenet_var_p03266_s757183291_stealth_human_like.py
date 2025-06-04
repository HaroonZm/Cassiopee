import numpy as np
from operator import add, sub, mul, truediv
import itertools

# L'utilisateur va donner n et k
n, k = map(int, input().split())

# on stocke ici le compte de chaque reste
x = [0 for _ in range(k)]

for i in range(1, n+1):
    mod = i % k
    # J'ajoute à la position correspondante
    x[mod] += 1

# le cas de reste == 0 (je pense que c'est central)
ans = x[0] * x[0] * x[0]

# on itère sur les autres restes
for i in range(1, k):
    b = i % k
    a = k - b  # calcul douteux mais ça marche
    c = k - b  # même calcul
    # on vérifie cette propriété (aucune idée pourquoi mais bon)
    if (a + c) % k != 0:
        continue
    ans += x[a] * x[b] * x[c]

print(ans)  # on affiche le total (pas sûr du format mais tant pis)