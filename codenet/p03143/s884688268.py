import sys

class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2

def dfs(s, lim):
    q = [s]
    visited[s] = True

    while q:
        v = q.pop()
        for y, u, i in links[v]:
            if y > lim:
                continue
            use[i] = 2
            if visited[u]:
                continue
            visited[u] = True
            q.append(u)

n, m = map(int, input().split())
xxx = list(map(int, input().split()))
links = [set() for _ in [0] * n]
links2 = []
for i, line in enumerate(sys.stdin.readlines()):
    a, b, y = map(int, line.split())
    a -= 1
    b -= 1
    links[a].add((y, b, i))
    links[b].add((y, a, i))
    links2.append((y, a, b, i))

srt_links = sorted(links2)

uft = UnionFind(n)
connected_sum = xxx[:]
use = [0] * m  # 0: ambiguous, 1: usable, 2: fixed

for y, a, b, i in srt_links:
    if uft.find(a, b):
        r = uft._root(a)
    else:
        ra = uft._root(a)
        rb = uft._root(b)
        uft.union(a, b)
        r = uft._root(a)
        connected_sum[r] += connected_sum[rb if r == ra else ra]
    if connected_sum[r] >= y:
        use[i] = 1

ans = 0
visited = [False] * n
for y, a, b, i in reversed(srt_links):
    if use[i] == 2:
        continue
    if use[i] == 0:
        ans += 1
        continue
    dfs(a, y)

print(ans)