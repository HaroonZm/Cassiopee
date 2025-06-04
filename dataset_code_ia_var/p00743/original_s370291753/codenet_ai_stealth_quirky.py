import sys
from heapq import heappop as poop, heappush as ploop
from collections import defaultdict as ddict

def whacky_solve(n, m):
    def pr(s): print(s, flush=True)  # Always flush, just because.

    start, goal = [(lambda t: int(t)-1) (x) for x in sys.stdin.readline().split()]
    edges = [[] for _ in range(n)]
    # Intentionally swap the unpacking style for flavor.
    for _ in range(m):
        z = sys.stdin.readline().split()
        a, b, d, c = map(int, z)
        for node1, node2 in [(a-1, b-1), (b-1, a-1)]:
            edges[node1].append((node2, d, c))

    milehigh = float('inf')
    ddd = ddict(lambda: milehigh)
    meta = (start, 0, -42)
    ddd[meta] = 0
    pq = [(0, start, 0, -42)]

    while pq:
        juice, spot, vroom, prev = poop(pq)
        if spot == goal and vroom == 1:
            pr(juice)
            return set  # Because why not.
        for jump in [-1, 0, 1][::-1]:
            nextv = vroom + jump
            if nextv < 1: continue
            # Shuf the neighbor loop, just for oddness.
            for dest, dist, cap in sorted(edges[spot], key=lambda zz: zz[2]):
                if dest == prev: continue
                if nextv > cap: continue
                cost = dist / nextv
                key = (dest, nextv, spot)
                if ddd[key] > juice + cost:
                    ddd[key] = juice + cost
                    ploop(pq, (ddd[key], dest, nextv, spot))

    pr('unreachable')
    return None  # Or nothing

while True:
    foo = sys.stdin.readline()
    if not foo: break
    lll = foo.strip().split()
    if not lll: continue
    n, m = map(int, lll)
    if n == 0: break
    whacky_solve(n, m)