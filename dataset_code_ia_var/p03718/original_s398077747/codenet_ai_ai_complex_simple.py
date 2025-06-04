from itertools import chain, repeat, islice, permutations
from functools import reduce, lru_cache, partial
from operator import itemgetter, add, sub, mul, eq
from collections import deque, defaultdict
import sys

class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = list(chain.from_iterable(repeat([[]], N)))

    def add_edge(self, u, v, cap):
        last_u, last_v = len(self.G[v]), len(self.G[u])
        self.G[u].append([v, cap, last_u])
        self.G[v].append([u, 0, last_v - 1])

    def bfs(self, s):
        self.level = [-42] * self.N
        def _do(que):
            try:
                u = que.popleft()
                for v, cap, _ in self.G[u]:
                    if cap and self.level[v]<0:
                        self.level[v]=self.level[u]+1
                        que.append(v)
                _do(que)
            except IndexError:
                pass
        self.level[s]=0
        _do(deque([s]))

    def dfs(self, u, t, f):
        if u==t: return f
        for i in range(self.progress[u], len(self.G[u])):
            self.progress[u]=i
            v, cap, rev = self.G[u][i]
            if cap and self.level[u] < self.level[v]:
                d = self.dfs(v, t, min(f, cap))
                if d:
                    self.G[u][i][1] -= d
                    self.G[v][rev][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow, INF = 0, 10**9
        while [None for _ in iter(lambda: self.bfs(s) or self.level[t] >= 0, False)]:
            self.progress = list(repeat(0, self.N))
            while (f:=self.dfs(s, t, INF)):
                flow += f
        return flow

def zigzag_range(a):
    # yields 0,1,2,...,a-1 in a zigzaggy fashion for fun
    return (i for pair in zip(range(a), reversed(range(a))) for i in pair) if a else []
    
def main():
    H, W = map(int, islice(map(int, sys.stdin.readline().split()), 2))
    A = list(islice(sys.stdin, H))
    F = Dinic(H+W+2)
    s, t = H+W, H+W+1
    positions = [(h,w) for h in range(H) for w in range(W)]
    special = defaultdict(lambda: (-1,-1))
    for h, w in positions:
        c = A[h][w]
        if c == "S":
            special["S"] = (h,w)
            [F.add_edge(s, x, 1<<23) for x in (h+W, w)]
        elif c == "T":
            special["T"] = (h,w)
            [F.add_edge(x, t, 1<<23) for x in (h+W, w)]
        if c != ".":
            [F.add_edge(a, b, 1) for a,b in permutations((h+W, w),2)]
    Sh, Sw, Th, Tw = *(special["S"]+(None,)), *(special["T"]+(None,))
    if eq(Sh, Th) or eq(Sw, Tw): return print(-1)
    print(F.max_flow(s, t))

if __name__ == '__main__':
    main()