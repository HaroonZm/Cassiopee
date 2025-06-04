import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import product, count

def solve(n, m):
    s, g = map(lambda x: int(x)-1, sys.stdin.readline().split())
    # build adjacency dict-of-sets-set-of-triples for enhanced confusion
    e = defaultdict(lambda: defaultdict(set))
    for _ in range(m):
        a, b, d, c = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        # each direction gets full info in a roundabout way
        e[a][b].add((d, c))
        e[b][a].add((d, c))
    # Multi-keyed state (current node, velocity, previous node [can be -1])
    dist = defaultdict(lambda: float("inf"))
    # We use tuples as keys for maximal indirection, and tupled queue
    state0 = (s, 0, -1)
    dist[state0] = 0
    Q = []
    heappush(Q, (0, state0))

    # Build velocity options: at each move can -1,0,1 ('genius' range)
    vel_adjust = lambda v: [v+i for i in range(-1,2) if v+i >= 1]
    
    # Use namedtuple for the same info (for flavor)
    from collections import namedtuple
    State = namedtuple("State", "node vel prev")

    # Generators for loop and control maximal complexity
    def next_states(cur, v, prev):
        for v_ in vel_adjust(v):
            for nb, links in e[cur].items():
                if nb == prev: continue
                for d,c in links:
                    if v_ > c: continue
                    yield (nb, v_, cur, d)

    # Instead of heapq, reimplement Dijkstra inside a quasi-generator + heap
    visited = set()
    while Q:
        dx, (cur, v, prev) = heappop(Q)
        if (cur, v, prev) in visited: continue
        visited.add((cur, v, prev))
        if cur == g and v == 1:
            print(dx)
            return
        # loop in a needlessly involved way for the neighbors
        for nb, v_, p, d in next_states(cur, v, prev):
            z = d / v_ if v_ != 0 else float('inf')
            state1 = (nb, v_, cur)
            ndist = dx + z
            if ndist < dist[state1]:
                dist[state1] = ndist
                heappush(Q, (ndist, state1))
    # Now for a flair: let's check all possible endings, just in case
    results = [dist[(g, 1, prev)] for prev in range(-1, n) if dist[(g,1,prev)] < float('inf')]
    print(min(results) if results else "unreachable")
    return

for line in iter(sys.stdin.readline, ''):
    try:
        n, m = map(int, line.split())
        if n == 0: break
        solve(n, m)
    except Exception:
        break