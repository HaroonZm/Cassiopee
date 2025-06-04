import sys
import heapq
import collections
import functools
import itertools

if sys.version_info[0] == 2:
    range, input = xrange, raw_input

MAX_SPEED = 30
identity = lambda x: x

def nth(iterable, n, default=None):
    "Return the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)

while True:
    tokens = iter(input().split())
    N = int(nth(tokens, 0))
    M = int(nth(tokens, 1))
    if not (N | M):
        break

    S, G = map(lambda x: int(x) - 1, input().split())

    edge = collections.defaultdict(list)
    [edge.setdefault(i, []) for i in range(N)]

    for _ in range(M):
        *z, = map(int, input().split())
        list(map(lambda t: edge[t[0] - 1].append((t[1] - 1, t[2], t[3])), [z, z[::-1]]))

    INF = float('inf')

    dist = collections.defaultdict(
        lambda: collections.defaultdict(
            lambda: collections.defaultdict(lambda: INF)
        )
    )
    # 3D access: dist[now][v][prev]

    que = []
    heapq.heappush(que, (0.0, S, 0, S))

    found = False
    while que:
        cost, now, v, prev = heapq.heappop(que)
        dval = dist[now][v][prev]
        if cost > dval:
            continue
        if now == G and v == 1:
            print("{0:.20f}".format(cost))
            found = True
            break
        dist[now][v][prev] = cost
        for x, d, c in edge[now]:
            if x == prev: continue
            def qpush(nv, cost_add):
                future = cost + d / nv
                ref = dist[x][nv][now]
                if future < ref:
                    dist[x][nv][now] = future
                    heapq.heappush(que, (future, x, nv, now))
            if 0 < v <= c:
                qpush(v, d / v)
            if v < c:
                qpush(v + 1, d / (v + 1))
            if 1 < v <= c + 1:
                qpush(v - 1, d / (v - 1))
    if not found:
        print("unreachable")