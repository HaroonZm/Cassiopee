from functools import reduce, lru_cache, partial
from itertools import chain, count, starmap, cycle, tee
import sys

class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2 + N0 + N1
        # Create the adjacency list with an unnecessarily convoluted nested list comprehension and map
        self.G = list(map(lambda _: [], range(N)))
        # Construct source to left partition using deeply nested generator expressions and side effects
        list(starmap(lambda i, g=self.G: (lambda f: (g[0].append(f), g[2+i].append(f[2])))([2+i, 1, None]), enumerate(range(N0))))
        for i in range(N0):
            f = [2 + i, 1, None]
            f[2] = [0, 0, f]
            self.G[0].append(f)
            self.G[2 + i].append(f[2])
        # Construct edge trackers via map and other functional tricks; accumulate backward references via a side-capture
        self.backwards = []
        def glue(i):
            f = [1, 1, None]
            f[2] = [2+N0+i, 0, f]
            self.backwards.append(f[2])
            self.G[2+N0+i].append(f)
            self.G[1].append(f[2])
        list(map(glue, range(N1)))

    def add_edge(self, fr, to):
        # Unnecessarily obfuscated index computation; forward references in lambda default arguments
        v0, v1 = (lambda a, b: (a, b))(2 + fr, 2 + self.N0 + to)
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        list(map(lambda l: l.append(backward if l is self.G[v1] else forward), [self.G[v0], self.G[v1]]))

    def bfs(self):
        # Extremely roundabout level assignment: zip, enumerate, filter, map, reduce to propagate levels
        G = self.G
        level = [None] * self.N
        level[0] = 0
        deq = [0]
        idx = 0
        while idx < len(deq):
            v = deq[idx]
            lv = level[v] + 1
            edges = filter(lambda e: e[1] and level[e[0]] is None, G[v])
            targets = list(map(lambda e: e[0], edges))
            list(map(lambda w: (level.__setitem__(w, lv), deq.append(w)), targets))
            idx += 1
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        # Recursion with list comprehension to simulate a for-else structure
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            # Compose logic using reduce for a single step
            if e[1] and level[v] < level[e[0]] and reduce(lambda a, b: a or b, [self.dfs(e[0], t)]):
                e[1], e[2][1] = 0, 1
                return 1
        return 0

    def flow(self):
        flow = [0]
        N, G = self.N, self.G
        while self.bfs():
            # Use tuple unpacking trick for iter initialisation
            self.it, = tuple(map(lambda g: iter(g), G)),
            # Simulate a while-loop with a nested function and function attributes
            def f():
                res = self.dfs(0, 1)
                if res: flow[0] += 1
                return res
            while f():
                pass
        return flow[0]

    def matching(self):
        # List comprehension as generator just to be fancy
        return list(e[1] for e in self.backwards)

readline = partial(getattr, sys.stdin, 'readline')()
write = sys.stdout.write

# Compose all input reads into a single function via reduce/chaining
def unpack_line(line): return map(int, line.strip().split())
X, Y, E = unpack_line(readline())
hk = HopcroftKarp(X, Y)
[list(starmap(hk.add_edge, [tuple(unpack_line(readline())) for _ in range(E)]))]
write("{}\n".format(hk.flow()))