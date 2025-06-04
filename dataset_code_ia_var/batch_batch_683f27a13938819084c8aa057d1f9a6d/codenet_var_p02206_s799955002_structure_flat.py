from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
# Fonctions d'input inutiles à plat, on lit direct si besoin
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Début du code plat
if __name__ == '__main__':
    # Lire n et k
    n_k_line = sys.stdin.readline().split()
    while len(n_k_line)<2:
        n_k_line += sys.stdin.readline().split()
    n = int(n_k_line[0])
    k = int(n_k_line[1])

    l = 0
    r = k + 1
    while l + 1 < r:
        m = (l + r) // 2

        # Partie 'ok(m)' en non-fonction :
        s = 0
        cnt = 0
        m_copy = m
        valid = True
        while m_copy:
            s += m_copy
            cnt += 1
            if s > k:
                valid = False
                break
            if cnt == n:
                break
            m_copy >>= 1
        else:
            # Boucle while s'est terminée sans break
            # valid reste True
            pass
        # Si boucle finie par break sur s>k, valid=False

        if valid:
            l = m
        else:
            r = m
    print(l)