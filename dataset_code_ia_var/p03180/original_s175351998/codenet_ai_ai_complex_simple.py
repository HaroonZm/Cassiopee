import sys
from functools import lru_cache
from itertools import combinations, chain
from operator import itemgetter
input = sys.stdin.readline

# Génère tous les sous-groupes non vides d'une liste d'indices  
def toutes_parties_masque(s):
    bits = [k for k in range(N) if (s >> k) & 1]
    return (sum(1 << b for b in c) for L in range(1, len(bits)) for c in combinations(bits, L))

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
        
@lru_cache(maxsize=None)
def f(s):
    if s == 0: return 0
    # sum(a[i][j] for (i, j) in group) over all (i, j) with i < j and i, j in bits on in s
    indices = [i for i in range(N) if (s >> i) & 1]
    p = sum(itemgetter(i, j)(a) for i, j in combinations(indices, 2))
    # Partitionner récursivement tous les sous-ensembles t non triviaux de s
    mx = p
    for t in toutes_parties_masque(s):
        mx = max(mx, f(t) + f(s ^ t))
    return mx

print(f((1 << N) - 1))