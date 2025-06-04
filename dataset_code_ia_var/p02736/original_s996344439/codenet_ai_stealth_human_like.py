import sys
import math
import random
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop

# hum, j'augmente la récursion mais j'suis pas sûr que c'est utile ici
sys.setrecursionlimit(101000)
input = sys.stdin.readline

MOD = 10 ** 9 + 7
INF = float('inf')  # bon, on pourrait faire 1e10 aussi

sqrt = math.sqrt

# Fonctions pour extraire rapidement des entrées, je me rappelle jamais de toutes...
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def II(): return int(input())
def IF(): return float(input())
def LS(): return [list(x) for x in input().split()]
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LF() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]


def solve():
    n = II()
    a = list(map(lambda x: int(x)-1, S()))  # On enlève 1 à chaque chiffre, pas sûr si c'est utile...
    answer = 1
    if not 1 in a:  # si aucun 1 dedans, je double la réponse ?
        answer = answer * 2
        for j in range(n):
            a[j] //= 2

    res = 0
    # Un bout avec Lucas, je comprends pas tous les bits mais bon ça marche
    for i in range(n):
        # Pour chaque bit où c'est actif ?
        if (n-1) & i == i:
            # xor sur le plus faible bit
            res ^= (a[i] & 1)

    print(res * answer)
    return

if __name__ == "__main__":
    solve()  # Let's go!