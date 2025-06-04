import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

# Bon, on augmente la limite de récursion
sys.setrecursionlimit(10**7)
inf = 10**20      # vraiment très grand
eps = 1.0/10**13  # petite valeur
mod = 10**9+7     # modulo classique (on ne s’en sert peut-être pas ici)
dd = [(-1,0), (0,1), (1,0), (0,-1)]   # déplacements orthogonaux
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)] # diagonales

def LI():
    # liste d'entiers lue sur une ligne
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # liste d'entiers, 1 en moins (indices genre C++)
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    # liste de float
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # split string
    return sys.stdin.readline().split()

def I():
    # lit un entier
    return int(sys.stdin.readline())

def F():
    # lit un float
    return float(sys.stdin.readline())

def S(): return input()

def pf(s):
    # print flushé, j'utilise pas souvent
    print(s, flush=True)

def main():
    rr = []

    def f(n):
        ab = LS()
        if len(ab) < 2:
            # haha parfois l'entrée ne suffit pas
            return -1
        a, b = ab
        if a == b:
            return 0
        try:
            a = [int(c) for c in a]
            b = [int(c) for c in b]
        except:
            # on ne sait jamais, parfois des mauvais inputs
            return -2
        aa = [a[:]]
        ad = set()
        ad.add(tuple(a))
        r = 0
        # vrai BFS pour trouver la solution ?
        while True:
            r += 1
            next_aa = []
            for a in aa:
                ti = 0
                for i in range(r-1, n):
                    if a[i] != b[i]:
                        ti = i
                        break
                sa = b[ti] - a[ti]
                for j in range(ti+1, n+1): # probablement un off-by-one ici ? Mais bon...
                    t = [(a[i] + sa) % 10 if ti <= i < j else a[i] for i in range(n)]
                    key = tuple(t)
                    if key in ad:
                        continue
                    if t == b:
                        return r
                    ad.add(key)
                    next_aa.append(t)
            aa = next_aa

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    # retourne le résultat formaté
    s = [str(x) for x in rr]
    return '\n'.join(s)

print(main())