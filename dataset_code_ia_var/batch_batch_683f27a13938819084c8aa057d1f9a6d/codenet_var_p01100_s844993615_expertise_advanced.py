from sys import stdin, stdout
from collections import deque
from itertools import repeat

def solve():
    readline = stdin.readline
    write = stdout.write

    N, M = map(int, readline().split())
    if N == M == 0:
        return False

    G = [[] for _ in repeat(None, N)]
    cs = [0] * N
    for _ in range(M):
        u, v = map(int, readline().split())
        fwd = [v-1, 1, None]
        bwd = [u-1, 0, fwd]
        fwd[2] = bwd
        G[u-1].append(fwd)
        G[v-1].append(bwd)
        cs[v-1] += 1

    prv = [0] * N

    # Advanced: Encapsulate BFS in a closure with parameterization
    def bfs(balance_predicate, edge_dir, cs_update):
        que = deque()
        used = [False] * N
        bal = [i for i, c in enumerate(cs) if balance_predicate(c)]
        for i in bal:
            que.append(i)
            used[i] = True
            prv[i] = None

        terminal = -1
        while que:
            v = que.popleft()
            if edge_dir['stop'](cs[v]):
                terminal = v
                break
            for w, d, rev in G[v]:
                if edge_dir['dir'](d) and not used[w]:
                    que.append(w)
                    used[w] = True
                    prv[w] = rev
        if terminal == -1:
            return False
        v = terminal
        while prv[v] is not None:
            e = prv[v]
            e[1], e[2][1] = cs_update(e[1]), cs_update(e[2][1], flip=True)
            v = prv[v][0]
        return (v, terminal)

    # Optimize by using lambda criteria
    while True:
        mi, ma = min(cs), max(cs)
        changed = bfs(
            lambda c: c == mi,
            {'dir': lambda d: d == 1, 'stop': lambda c: c >= mi + 2},
            lambda cur, flip=False: 1 if not flip else 0
        )
        if not changed:
            break
        v, j = changed
        cs[v] += 1
        cs[j] -= 1

    while True:
        mi, ma = min(cs), max(cs)
        changed = bfs(
            lambda c: c == ma,
            {'dir': lambda d: d == 0, 'stop': lambda c: c <= ma - 2},
            lambda cur, flip=False: 0 if not flip else 1
        )
        if not changed:
            break
        v, j = changed
        cs[v] -= 1
        cs[j] += 1

    write(f"{min(cs)} {max(cs)}\n")
    return True

while solve():
    pass