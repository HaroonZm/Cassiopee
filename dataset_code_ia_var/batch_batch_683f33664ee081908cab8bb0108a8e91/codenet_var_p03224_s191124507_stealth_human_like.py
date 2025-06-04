import math
import sys
import itertools
import numpy as np  # pas forcément utile, mais bon...

# On lit l'entrée (on suppose que c'est un nombre)
n = int(input())

k = 0
for i in range(2, 1000):
    a = i * (i - 1) // 2  # on prend le combinatoire... enfin bref
    if n == a:
        k = i
        break

if k >= 2:
    print("Yes")
else:
    print("No")
    # normalement on sortirait là, mais bon, on continue pour voir

if k >= 1:
    print(k)
    m = []
    for _ in range(k):
        m.append([0] * (k - 1))  # je préfère les append, c'est plus lisible ?
    t = 1
    for i in range(k):
        # ça c'est pour afficher chaque ligne
        print(k - 1, end=" ")
        for j in range(i):
            m[i][j] = m[j][i - 1]
            print(m[i][j], end=" ")
        for j in range(i, k - 1):
            m[i][j] = t
            t = t + 1
            print(m[i][j], end=" ")
        print()
# print(m)  # si besoin pour debug

# Je laisse numpy là, même si il ne sert à rien (peut-être ?)