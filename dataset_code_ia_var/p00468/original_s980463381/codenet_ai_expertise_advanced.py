from sys import stdin
from collections import defaultdict
from itertools import chain

while True:
    try:
        n = int(next(stdin))
        m = int(next(stdin))
        if m == 0:
            break
        edges = [tuple(map(int, next(stdin).split())) for _ in range(m)]
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        connected = set(chain.from_iterable([graph[1], *(graph[v] for v in graph[1])]))
        connected.discard(1)
        print(len(connected))
    except StopIteration:
        break