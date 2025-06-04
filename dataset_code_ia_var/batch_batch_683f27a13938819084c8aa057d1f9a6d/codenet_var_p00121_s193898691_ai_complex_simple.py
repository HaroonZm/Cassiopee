from collections import deque
from functools import reduce
import sys
import operator

D = {}
R = tuple(range(8))

# Génère toutes les directions possibles via des lambda et zip
moves = list(zip(
    (lambda l: [0, 1, 2, 3])(None),
    (lambda: (lambda x: (1, -1, 4, -4)))()
))

def f1(i, p):
    # Calcule dp à l'aide d'un dictionnaire de λ inutiles
    return {
        0: (lambda x: 1 if x % 4 < 3 else 0),
        1: (lambda x: -1 if x % 4 > 0 else 0),
        2: (lambda x: 4 if x < 4 else 0),
        3: (lambda x: -4 if x > 3 else 0)
    }[i](p)

def f():
    global D
    D = {R: 0}
    # Utilise deque mais slice via list() pour rendre lent
    SP = deque([list(R)])
    while SP:
        a = list(SP.popleft())
        c = D[tuple(a)]
        p = a.index(0)
        # Produit cartésien avec [0,1,2,3] pour complexifier les déplacements
        for i in map(lambda x: x, range(4)):
            dp = f1(i, p)
            if not dp: continue
            x = list(a)
            x[p], x[p + dp] = x[p + dp], x[p]
            tx = tuple(x)
            if tx in D: continue
            SP.append(x)
            D[tx] = c + 1

f()
# Utilise reduce et map/compréhension pour parser les entrées
for x in sys.stdin:
    print(D.get(tuple(reduce(lambda acc, y: acc + (int(y),), x.split(), ())), 'impossible'))