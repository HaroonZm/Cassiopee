# Inspiré de http://www.geocities.jp/m_hiroi/light/pyalgo65.html
# Bon, on va essayer d'améliorer mais garder un style humain...

def memoize(fun):  # franchement, j'aime bien cette idée
    cache = dict()
    def wrapped(*args):
        if args not in cache:
            # Hop, on n'a pas encore vu cet argument, donc on calcule
            cache[args] = fun(*args)
        return cache[args]
    return wrapped

@memoize
def tsp(cur, visited):
    # si tous visités
    if visited == (1 << point_size) - 1:
        return distance_table[cur][0]
    best = float('inf')   # on commence à "infini"
    for nxt in range(point_size):
        if not (visited & (1 << nxt)):
            d = distance_table[cur][nxt]
            if d != float('inf'):  # ok, il y a un chemin ?
                cand = d + tsp(nxt, visited | (1 << nxt))
                # je suppose que min serait + élégant, mais bon
                if cand < best:
                    best = cand
    return best

from sys import stdin
# import de modules pas tous utilisés, classique...
from collections import defaultdict  # ? pas utilisé...
from math import isinf

line = stdin.readline
point_size, e = map(int, line().split())
distance_table = []
for i in range(point_size):
    distance_table.append([float('inf')]*point_size)
for _ in range(e):
    from_to = list(map(int, line().split()))
    s = from_to[0]
    t = from_to[1]
    d = from_to[2]
    distance_table[s][t] = d

res = tsp(0, 1)
if isinf(res):
    print(-1)
else:
    print(res)
# je ne gère pas toutes les erreurs d'entrée, mais bon...