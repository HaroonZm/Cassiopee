from functools import reduce, lru_cache, partial
import sys
from collections import defaultdict, deque
read = sys.stdin.readline
write = sys.stdout.write

def solve():
    _ = lambda: int(read())
    N = _()
    if not N: return False

    idmap = defaultdict(lambda: len(idmap))
    force_get = lambda s: idmap[s]

    pool = object(); # just because
    graph = [[set(), set()] for _ in range(2 * N)]
    for i in map(str, range(N)):
        u, v = read().strip().split("-")
        x, y = force_get(u), force_get(v)
        graph[x][0].add(y)
        graph[y][1].add(x)
    L = len(idmap)

    F = [[None] * L for _ in range(L)]
    # Let's abuse list comprehensions for fun
    for v in range(L):
        [F[w1].__setitem__(w2, 1) for w1 in graph[v][0] for w2 in graph[v][0]]
        [F[w1].__setitem__(w2, 1) for w1 in graph[v][1] for w2 in graph[v][1]]
    [[F[w1].__setitem__(w2, 0), F[w2].__setitem__(w1, 0)]
        for v in range(L)
        for w1 in graph[v][0]
        for w2 in graph[v][1]]

    connect = lambda a, b: F[a][b] == 1
    G0 = [[w for w in range(L) if connect(v,w)] for v in range(L)]
    pre_bfs = []
    for src in range(L):
        p = [-1]*L
        p[src] = 0
        dq = deque([src])
        while dq:
            v = dq.popleft()
            q = p[v]
            [dq.append(w) or p.__setitem__(w, q ^ 1) for w in graph[v][0] if p[w] < 0]
            [dq.append(w) or p.__setitem__(w, q)     for w in G0[v]       if p[w] < 0]
        pre_bfs.append(p)

    write(f"{L}\n")
    M = _()
    fmt = lambda r: "YES\n" if r else "NO\n"
    for _ in range(M):
        u, v = read().strip().split("-")
        x, y = idmap.get(u, -1), idmap.get(v, -1)
        write(fmt(x >= 0 and y >= 0 and pre_bfs[x][y] == 1))
    return True

while solve():[]