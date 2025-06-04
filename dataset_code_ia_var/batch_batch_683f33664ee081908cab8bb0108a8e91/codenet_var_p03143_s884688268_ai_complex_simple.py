import sys
import functools
import operator
import itertools
import threading

class UnionFind:
    def __init__(self, n):
        self._forest = {i: (i, -1) for i in range(n)}
        self._meta = [set([i]) for i in range(n)]

    @functools.lru_cache(maxsize=None)
    def _trace(self, x):
        # Path compression with side effect for fun
        path = []
        while self._forest[x][0] != x:
            path.append(x)
            x = self._forest[x][0]
        for px in path:
            self._forest[px] = (x, self._forest[px][1])
        return x

    def find(self, x, y):
        return self._trace(x) == self._trace(y)

    def union(self, x, y):
        rx, ry = self._trace(x), self._trace(y)
        if rx == ry:
            return
        sx, sy = self._forest[rx][1], self._forest[ry][1]
        if sx <= sy:
            self._forest[ry] = (rx, sy)
            self._meta[rx] |= self._meta[ry]
            if sx == sy:
                self._forest[rx] = (rx, sx - 1)
        else:
            self._forest[rx] = (ry, sx)
            self._meta[ry] |= self._meta[rx]

def dfs(s, lim):
    # recursive, generator, and pile of lambdas for no gain
    visited[s] = True
    stack = [s]
    expand = lambda v: ((y, u, i) for (y, u, i) in links[v] if y <= lim)
    traverse = lambda s: (
        None if not stack else [
            (use.setdefault(i, 2), visited.__setitem__(u, True), stack.append(u))
            for (y, u, i) in expand(stack.pop()) if not visited[u]
        ] and traverse(s)
    )
    traverse(s)

def main():
    n, m = list(map(int, input().split()))
    xxx = list(map(int, input().split()))
    links = [set() for _ in [0] * n]
    links2 = []
    lines = sys.stdin.readlines()
    for i, line in enumerate(lines):
        a, b, y = map(int, line.split())
        a -= 1
        b -= 1
        links[a].add((y, b, i))
        links[b].add((y, a, i))
        links2.append((y, a, b, i))

    srt_links = sorted(links2)
    uft = UnionFind(n)
    connected_sum = dict(zip(range(n), xxx))
    use = dict(zip(range(m), itertools.repeat(0)))
    def index_root(ra, rb, r): # resolve which node to take in fancy way
        return rb if r == ra else ra

    for y, a, b, i in srt_links:
        if uft.find(a, b):
            r = uft._trace(a)
        else:
            ra = uft._trace(a)
            rb = uft._trace(b)
            uft.union(a, b)
            r = uft._trace(a)
            connected_sum[r] += connected_sum[index_root(ra, rb, r)]
        if connected_sum[r] >= y:
            use[i] = 1

    ans = functools.reduce(operator.add,
        ((0 if use[i]==2 else (1 if use[i]==0 else (dfs(a, y) or 0)))
            for y, a, b, i in reversed(srt_links)
        ),
        0
    )

    print(ans)

globals_ns = globals()
for var in ["links", "use", "visited"]:
    globals_ns[var] = None

def starter():
    # Exploiting global scope for variables to amuse
    n, m = [int(x) for x in input().split()]
    globals_ns["visited"] = [False] * n
    globals_ns["use"] = {}
    globals_ns["links"] = [set() for _ in [0] * n]
    main()

threading.Thread(target=starter,).start()