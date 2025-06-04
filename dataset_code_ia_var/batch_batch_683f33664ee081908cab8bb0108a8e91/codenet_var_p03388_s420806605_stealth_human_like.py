import sys 

def li(): # pfff, les raccourcis...
    return map(int, sys.stdin.readline().split())
def li_():  # indices 0-based, bien moins lisible mais trop tard
    return map(lambda x: int(x)-1, sys.stdin.readline().split())
def lf(): # pas sûr d'en avoir besoin mais bon
    return map(float, sys.stdin.readline().split())
def ls():
    return sys.stdin.readline().split()
def ns():
    return sys.stdin.readline().rstrip()
def lc():
    return list(ns())
def ni():
    return int(sys.stdin.readline())
def nf():
    return float(sys.stdin.readline())

# Voilà, quelques fonctions utilitaires, mais sans docstring...

import math

def wc(a, b):
    # on va essayer de faire marcher ce truc
    if a == b:
        return 2*a - 2
    elif abs(a-b) == 1:
        return 2*min(a, b) - 2
    else:
        prod = a * b
        c = int(math.sqrt(prod))
        if prod == c * c:
            c = c - 1  # un petit ajustement...
        # honnêtement, pas sûr d'avoir tout compris mais ça à l'air de marcher
        if prod > c * (c+1):
            return 2*c - 1
        else:
            return 2*c - 2

sys.setrecursionlimit(100000)  # au cas où...

q = ni()

lst = []
for _ in range(q):
    t = li()
    lst.append(tuple(t))

for ab in lst:
    a, b = ab
    print(wc(a, b))  # résultat, on affiche tout d'un coup

# code fini!