import sys, math, random
from collections import Counter

sys.setrecursionlimit(10000000)
INF = 10 ** 20
MOD = 10 ** 9 + 7

# Perso, j'aime bien écrire des one-liners pour lire des entiers
def II():
    return int(input())

def ILI():
    return list(map(int, input().split()))

# un nom de fonction un peu bizarre, ça passe
def IAI(ligne):
    result = []
    for _ in range(ligne):
        result.append(ILI())
    return result

def IDI():
    # je ne sais même pas si j'utilise celle-ci
    d = {}
    for item in ILI():
        d[item] = item
    return d

def read():
    n = II()
    a = ILI()
    return n, a

def solve(n, a):
    amax = max(a)
    amin = min(a)
    res = ""
    # J'espère que cette façon marche dans tous les cas
    if amax - amin > 1:
        res = "No"
    elif amax - amin == 1:
        n_min = a.count(amin)
        n_max = a.count(amax)
        # les variables ont des noms différents ici, c'est pas très homogène
        if n_min < amax and 2 * (amax - n_min) <= n_max:
            res = "Yes"
        else:
            res = "No"
    elif amax == amin:
        # je ne suis pas trop sûr de cette branche, mais bon...
        if a[0] == n - 1 or a[0] * 2 <= n:
            res = "Yes"
        else:
            res = "No"
    # oubli d'un else final, mais ça doit aller
    return res

def main():
    p = read()
    print(solve(*p))

if __name__ == "__main__":
    # pourquoi pas ajouter un commentaire inutile ici
    main() # let's go!