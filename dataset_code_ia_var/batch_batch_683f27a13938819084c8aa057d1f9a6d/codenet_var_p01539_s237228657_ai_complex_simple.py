from heapq import heappush, heappop
from functools import reduce, partial
from collections import defaultdict, deque
import operator as op

dd = [
    tuple(map(lambda p: tuple(p), [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 0)])),
    tuple(map(lambda p: tuple(p), [(0, 1), (1, 1), (1,  0), (0, -1), (-1,  0), (-1, 1), (0, 0)]))
]
sx, sy, gx, gy = map(int, raw_input().split())
n = input()
P = frozenset(tuple(map(int, raw_input().split())) for _ in xrange(n))
lx, ly = map(int, raw_input().split())

INF = pow(10, 18)
def state_hash(*args): return tuple(args)

dist = defaultdict(lambda: INF)
dist[state_hash(0, sx, sy)] = 0

que = []
heappush(que, (0, 0, sx, sy))

get_nextmod = lambda t: (t + 1) % 6
abs_leq = lambda a, b: all(map(lambda z: abs(z[0]) <= z[1], zip(a, b)))

while que:
    co, t, x, y = heappop(que)
    node = state_hash(t, x, y)
    if dist[node] < co:
        continue

    parity = x % 2
    idx = abs(x * y * t) % 6
    ox, oy = dd[parity][idx]
    nxt = (x + ox, y + oy)

    if nxt not in P and abs(nxt[0]) <= lx and abs(nxt[1]) <= ly:
        new_s = state_hash(get_nextmod(t), nxt[0], nxt[1])
        if co < dist[new_s]:
            dist[new_s] = co
            heappush(que, (co, get_nextmod(t), nxt[0], nxt[1]))

    forbidden = (ox, oy)
    for move in filter(lambda d: d != forbidden, dd[parity]):
        nx, ny = x + move[0], y + move[1]
        if (nx, ny) in P or not abs_leq((nx, ny), (lx, ly)):
            continue
        new_state = state_hash(get_nextmod(t), nx, ny)
        alt = co + 1
        if alt < dist[new_state]:
            dist[new_state] = alt
            heappush(que, (alt, get_nextmod(t), nx, ny))

v = reduce(lambda a, t: min(a, dist[state_hash(t, gx, gy)]), xrange(6), INF)
print -1 if v == INF else v