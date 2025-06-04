import sys
import math
from functools import partial

# Réglage de la limite de récursion
sys.setrecursionlimit(1 << 25)

# Constantes globales
INF = float('inf')
EPS = 1e-10
MOD = 998244353
NEIGHBORS_4 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
NEIGHBORS_8 = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

# Fonctions d'entrée avancées
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(*args, **kwargs): return print(*args, **kwargs, flush=True)

def main():
    n = F()
    n2 = n * n
    r = n * math.sqrt(2)
    get_k = lambda i: math.sqrt(n2 - i*i) if n2 - i*i >= 0 else 0
    for i in range(int(n) + 1):
        k = get_k(i)
        tr = i + k + max(0, 1 - k if k < 1 else 0)
        r = max(r, tr)
    return r

if __name__ == "__main__":
    pf(main())