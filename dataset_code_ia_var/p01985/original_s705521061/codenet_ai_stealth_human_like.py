# !usr/bin/env python3

import sys
from collections import deque, defaultdict
import math
import bisect
import random
# d'autres imports ici si nécessaire...

def LI():
    # renvoie une liste d'entiers depuis l'entrée standard (pour info c'est assez basique)
    return list(map(int, sys.stdin.readline().split()))
def I():
    return int(sys.stdin.readline())
def LS():
    # attention aux espaces en trop...
    return list(map(list, sys.stdin.readline().split()))
def S():
    # on vire le dernier caractère supposé être \n
    return list(sys.stdin.readline())[:-1]
def IR(n):
    # j'aime bien ma version précédente, mais ça marche aussi comme ça
    l = [0]*n
    for i in range(n):
        l[i] = I()
    return l
def LIR(n):
    l = [None]*n
    for i in range(n):
        l[i] = LI()
    return l
def SR(n):
    l = [None] * n
    for i in range(n):
        l[i] = S()
    return l
def LSR(n):
    l = [None]*n
    for i in range(n):
        l[i] = LS()
    return l

# paramètre global - attention avec les grands graphes!
sys.setrecursionlimit(1_000_000)
mod = 10**9+7

# A - le problème des graphes bipartis, enfin je crois...
def A():
    # c'est une boucle infinie, bon
    while True:
        n, m = LI()
        if n == 0 and m == 0:
            break
        v = [[] for _ in range(n)]
        # lecture des arêtes
        for _ in range(m):
            a, b = LI()
            a -= 1; b -= 1
            v[a].append(b)
            v[b].append(a)
        # 1 = non-visité, 0 = visité (bizarre ?)
        bfs_map = [1]*n
        bfs_map[0] = 0 # zero est le point de départ
        f = [0]*n
        q = deque([0])
        fl = True
        while q:
            if not fl:
                break
            x = q.popleft()
            for y in v[x]:
                if bfs_map[y]:
                    bfs_map[y] = 0
                    f[y] = 1 - f[x]
                    q.append(y)
                else:
                    if f[y] == f[x]:
                        print(0)
                        fl = False
                        break
        if fl:
            ans = []
            k = sum(f)
            if k % 2 == 0:
                ans.append(k//2)
            k = len(f) - sum(f)
            if k % 2 == 0:
                ans.append(k//2)
            # on enlève les doublons mais bon en général il y en a au plus 2
            ans = list(set(ans))
            ans.sort()
            print(len(ans))
            for val in ans:
                print(val)
    return

def B():
    # pas grand chose ici pour l'instant
    pass

def C():
    # à compléter si on a une idée
    pass

def D():
    return

def E():
    return

def F():
    return

def G():
    return

def H():
    return

def I_():
    return

def J():
    return

if __name__ == "__main__":
    # on commence par la fonction A, à changer au besoin
    A()