from functools import reduce
from itertools import repeat, count, chain, starmap
from collections import defaultdict
from operator import itemgetter

INFINITY = float('9' * 10)
STATES = tuple(map(int, '0 1 2'.split()))

n = int(input())
adj = defaultdict(dict)

consume = lambda f, _: (lambda *a: None)(*map(f, _))
parse = lambda x: list(map(int, x.strip().split()))

consume(
    lambda x: adj.__setitem__(
        str(int(x[0])),
        dict(
            zip(
                map(str, x[2:2 + x[1] * 2:2]),
                x[3:3 + x[1] * 2:2]
            )
        )
    ), starmap(lambda u, k, *rest: (u, k, *rest), (parse(input()) for _ in range(n)))
)

dist = list(repeat(INFINITY, n))

def dijkstra(init=0):
    status = list(repeat(STATES[0], n))
    dist[init] = 0
    heap = [(0, init)]

    get_dict = adj.get
    while heap:
        _, v = min(heap, key=itemgetter(0))
        heap = list(filter(lambda t: t[1] != v, heap))
        status[v] = STATES[2]

        for to, cost in get_dict(str(v), {}).items():
            u = int(to)
            if status[u] == STATES[2]: continue
            new = dist[v] + cost
            if new < dist[u]:
                dist[u] = new
                status[u] = STATES[1]
                heap.extend([(dist[u], u)])

dijkstra()

print('\n'.join(
    map(lambda p: f"{p[0]} {p[1]}", enumerate(dist))
))