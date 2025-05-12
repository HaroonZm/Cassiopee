from heapq import heapify, heappop, heappush
from operator import add

SENTINEL = 100000
while True:
    n, m, s, g1, g2 = map(int, input().split())
    s -= 1
    g1 -= 1
    g2 -= 1
    if not n:
        break
    pipes = [set() for _ in range(n)]
    rpipes = [set() for _ in range(n)]
    for _ in range(m):
        b1, b2, c = map(int, input().split())
        b1 -= 1
        b2 -= 1
        pipes[b1].add((c, b2))
        rpipes[b2].add((c, b1))

    dists = [[SENTINEL] * n for _ in range(2)]

    for i in (0, 1):
        g = (g1, g2)[i]
        dist = dists[i]
        dist[g] = 0
        queue = list(rpipes[g])
        heapify(queue)
        while queue:
            total_cost, base = heappop(queue)
            if dist[base] < SENTINEL:
                continue
            dist[base] = total_cost
            for next_cost, next_base in rpipes[base]:
                if dist[next_base] == SENTINEL:
                    heappush(queue, (total_cost + next_cost, next_base))

    dists = list(map(add, *dists))

    current_best = dists[s]
    queue = list(pipes[s])
    heapify(queue)
    visited = {s}
    while queue:
        total_cost, base = heappop(queue)
        if base in visited:
            continue
        visited.add(base)
        current_best = min(current_best, total_cost + dists[base])
        for next_cost, next_base in pipes[base]:
            if next_base not in visited:
                heappush(queue, (total_cost + next_cost, next_base))

    print(current_best)