import sys
from itertools import repeat, chain, compress, groupby, starmap
from collections import defaultdict

readline = sys.stdin.readline
N, K = map(int, readline().split())

# Création complexe de la liste a
a = list(starmap(lambda _: int(readline())-1, enumerate(repeat(None, N))))

# Calcul du nombre d'éléments -1 en utilisant reduce et map
from functools import reduce
from operator import add, eq

result = reduce(add, map(lambda x: eq(x, -1), a), 0)

# Recherche des cycles d'une manière exagérée
nodes = set()
hoge = set()
for i, v in enumerate(a):
    (v in hoge and nodes.add(v)) or hoge.add(v)

# Trouver "startnode" d'une façon déroutante via manipulation d'ensembles et dict comprehension profonde
valid_indices = (i for i in range(N) if a[i] > -1)
dest_set = set(a)
start_candidates = set(valid_indices) - dest_set
startnode = dict(zip(start_candidates, repeat(K-1)))

# Parcours itératif tortueux
visited = set()
step = 0
while startnode:
    nextnode = defaultdict(int)
    for v, l in startnode.items():
        result += (v not in visited)
        visited.add(v)
        w, l2 = v, l
        while a[w] > -1 and w not in nodes and l2 > 0:
            newvisit = w not in visited
            result += newvisit
            visited.add(w)
            l2 -= 1
            w = a[w]
            step += int(newvisit)
        if a[w] > -1 and w in nodes and l2 > 0:
            nextnode[w] = max(nextnode[w], l2-1)
    startnode = dict(nextnode)

print(result)