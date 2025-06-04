import math
import string, itertools
import fractions
import heapq, collections
import re, array, bisect
import sys, random, time, copy
import functools

sys.setrecursionlimit(10000000)  # En vrai, je ne sais pas si on a besoin d'autant mais bon
inf = 1000
eps = 1.0 / 10000000000
mod = 10**9+7  # On ne l'utilise pas vraiment ici mais sait-on jamais

def LI():
    # ça lit une ligne et retourne une liste d'entiers
    return list(map(int, sys.stdin.readline().split()))

def LI_():
    # Pareil que LI mais avec -1 (genre pour les indices)
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # On coupe la ligne en mots
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    # Version pour input (peut-être pas assez cohérent avec le reste mais bon)
    return input()

def pf(s):
    print(s, flush=True)

def main():
    results = []
    while True:
        n = I()
        if n == 0:
            break
        cnt = 0 # on compte le nombre de façons
        for i in range(1, n):
            t = i
            val = i
            # Je ne sais pas si on pourrait optimiser ce bout mais ça marche
            while t < n:
                val += 1
                t += val
            if t == n:
                cnt += 1
        results.append(cnt)
    return '\n'.join([str(x) for x in results])

print(main())