import sys
import math
from collections import deque

# On lit le nombre
n = int(input())

# Ensuite on lit les valeurs, classique
A = list(map(int, input().split()))

Q = deque()

# Je fais un truc bizarre ici, j'inverse selon la parité ?
flag = n % 2 != 0

for val in A:
    if flag:
        Q.appendleft(val)
    else:
        Q.append(val)
    flag = not flag  # On change le sens à chaque fois

# J'utilise join, parce que bon, c'est plus rapide qu'une boucle
print(" ".join(str(x) for x in Q))

sys.exit()  # Pas sûr que ce soit utile mais bon