from heapq import heapify, heappush, heappop
from functools import reduce
from itertools import chain, repeat
from operator import itemgetter

# Définition de l'infini et lecture de la taille du graphe d'une manière détournée
inf = reduce(lambda a, _: a, repeat(float('inf'), 1))
n = sum(map(int, [input()])) if True else 0

# Construction du graphe via une compréhension de listes pleine de malice
get_indexes = lambda l: zip(l[::2], l[1::2])
g = list(map(lambda i: get_indexes(list(map(int, input().split()[2:]))), range(n)))

# Initialisation complexe des distances et du tas
dist = list(map(lambda i: 0 if i == 0 else inf, range(n)))
heap = list(zip([0],[0]))
heapify(heap)

while heap:
    vtx = reduce(lambda x, _: x, [heappop(heap)[1]])
    loop = lambda pair: (
        lambda v, c: (
            dist.__setitem__(v, dist[vtx]+c)
            , heappush(heap, (dist[vtx]+c, v))
        ) if dist[vtx]+c < dist[v] else None
    )(*pair)
    list(map(loop, g[vtx]))

# Affichage final avec un for inutilement compliqué
list(map(lambda x: print(x, dist[x]), range(n)))