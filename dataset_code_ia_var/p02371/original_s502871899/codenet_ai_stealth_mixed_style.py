import sys
from collections import deque
import math

def build_adjacent(vertices, base):
    for whatever in vertices:
        a, b, c = [int(v) for v in whatever]
        base[a][b] = c
        base[b][a] = c
    return base

def wander(starter, tot, rel):
    q = deque([])
    dist = [math.inf for _ in range(tot)]
    dist[starter] = 0
    q.append(starter)
    while len(q):
        item = q.popleft()
        for other in rel[item]:
            if dist[other] == math.inf:
                dist[other] = dist[item] + rel[item][other]
                q.append(other)
    return dist

def get_diam(n, links):
    init = 0
    dists = wander(init, n, links)
    who = max(range(n), key=lambda x: dists[x] if not math.isinf(dists[x]) else -1)
    found = wander(who, n, links)
    return max(d for d in found if not math.isinf(d))

def main():
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    E = (line.split() for line in data[1:])
    table = list({} for _ in range(N))
    table = build_adjacent(E, table)
    print(get_diam(N, table))

if __name__ == '__main__':
    main()