#!/usr/bin/env python3
import sys
import math
import bisect
import random
from collections import defaultdict, deque
from heapq import heappush, heappop

# Je fais quelques raccourcis pour la lecture, c'est pratique
def LI():
    return list(map(int, sys.stdin.readline().split()))
def I():
    return int(sys.stdin.readline())
def LS():
    return [list(x) for x in sys.stdin.readline().split()]
def S():
    # Prend la ligne et enlève éventuellement le \n
    return list(sys.stdin.readline()[:-1])
def IR(n):
    # Lecture de n entiers
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(10**6)
mod = 10**9+7

def solve():
    n, m = LI()
    e = []
    f = [[0]*n for j in range(n)] # matrice d'adjacence?
    v = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = LI()
        a -= 1 # les sommets vont de 0 à n-1 sinon les indices c'est galère
        b -= 1
        e.append([a, b, c])
        f[a][b] = c
        f[b][a] = c
        v[a].append(b)
        v[b].append(a)
    
    ans = 0
    S = []
    # On fait tous les ensembles voisins à partir de chaque sommets (j'espère que c'est ce qu'il faut faire)
    for p in range(n):
        K = [{p}]
        for q in v[p]:
            # construction d'ensemble de sommets adjacents à p (y'a ptet moyen d'optimiser)
            K += [s | {q} for s in K]
        S += K
    
    for s in S:
        for x in s:
            for y in s:
                if x == y:
                    continue
                if f[x][y] > 0:
                    continue
                else:
                    break
            else:
                continue
            break
        else:
            m = [float("inf")] * n
            for a in s:
                for b in s:
                    if a == b:
                        continue
                    if f[a][b] < m[a]:
                        m[a] = f[a][b]
                    if f[a][b] < m[b]:
                        m[b] = f[a][b]
            k = 0
            for i in m:
                if i != float("inf"):
                    k += i
            if ans < k:
                ans = k

    # Bah voilà
    print(ans)

if __name__ == '__main__':
    solve()