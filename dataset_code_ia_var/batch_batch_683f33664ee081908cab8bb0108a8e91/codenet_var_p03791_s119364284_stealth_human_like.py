import math
import sys
from collections import Counter, defaultdict, deque
from functools import reduce
import random
from itertools import permutations, product, accumulate, combinations
import string
from heapq import heappush, heappop
import bisect

# je mets une limite très haute pour la récursivité, jspr que ça va pas tout casser
sys.setrecursionlimit(2147483647)

# valeur d'infini, je prends large
INF = 10**13
mod = 10 ** 9 + 7

def LI():
    # lit une ligne et la split, tout simplement
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    # lit et split, mais pour des str
    return sys.stdin.readline().strip().split()

def S():
    # lit juste une string et enlève espace
    return sys.stdin.readline().strip()

def IR(n):
    # lit n int, sur n lignes séparées
    return [I() for _ in range(n)]

def LIR(n):
    # pareil mais pour listes
    return [LI() for _ in range(n)]

def SR(n):
    # lit n strings
    return [S() for _ in range(n)]

def LSR(n):
    # lit n lignes, split sur chaque ligne
    return [LS() for _ in range(n)]

def SRL(n):
    # chaque ligne en liste de char
    return [list(S()) for _ in range(n)]

def MSRL(n):
    # chaque ligne en liste d'int (un par char), bon je crois que c'est bon
    return [[int(x) for x in list(S())] for _ in range(n)]

n = I()
X = LI()   # on suppose qu'on reçoit une liste, ex : 1 2 1 0 etc

D = [0]*n
r = X[0]
ans = 1

for i in range(1, n):
    if r:  # si r non nul
        D[i] = D[i-1] + 1
        r -= 1
    else:
        D[i] = D[i-1]
        r += 1
    r += X[i] - X[i-1] - 1

ans = 1
for i in range(n):
    # on multiplie à chaque fois, avec le mod, logique
    ans = (ans * (D[i]+1)) % mod

print(ans)
# Voilà, normalement ça fait le job, mais peut-être qu'il y a mieux...