#!/usr/bin/env python3

import sys
import math
from collections import defaultdict, deque
import bisect
import random
from heapq import heappush, heappop

# Franchement, j'aime pas trop cette façon de lire l'entrée, mais bon...
def LI():
    # Prends une ligne, split puis map en int(sans try except parce que YOLO)
    return list(map(int, sys.stdin.readline().split()))

def I():
    # Un simple int sur la ligne suivante
    return int(sys.stdin.readline())

def LS():
    # split puis liste chaque mot, pas sûr de toujours vouloir ça
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    # Récupère la ligne, et vire le retour chariot (enfin j'espère)
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    # Lis n entiers séparés sur chaque ligne ???
    return [I() for _ in range(n)]

def LIR(n):
    # Lis n listes d'entiers (genre matrice)
    return [LI() for _ in range(n)]

def SR(n):
    # Récupère n strings (sous forme de listes)
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(10**6)  # j'ai vu des solutions planter sinon
mod = 998244353

# MAIN solution, pas trop optimisée mais bon...
def solve():
    n = I()
    x = LI()
    ans = 0

    for i in range(n):
        xi = x[i]
        # la formule, j'espère que c'est bien ça
        tmp = pow(2, n - i - 1, mod) * xi * pow(xi + 1, i, mod)
        ans += tmp
        # ouais modder souvent, sinon overflow, je crois
        if ans >= mod:
            ans %= mod

    print(ans)
    # return inutile, mais bon
    return

if __name__ == '__main__':
    solve()