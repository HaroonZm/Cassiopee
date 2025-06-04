from sys import stdin

class PotUnionFind:
    __slots__ = ('parent', 'size', 'diff_p')

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.diff_p = [0] * n

    def root(self, x):
        px = self.parent
        dp = self.diff_p
        trace = []
        while px[x] != x:
            trace.append(x)
            x = px[x]
        for v in trace:
            dp[v] += dp[px[v]]
            px[v] = x
        return x

    def weight(self, x):
        px = self.parent
        dp = self.diff_p
        r, acc = x, 0
        while px[r] != r:
            acc += dp[px[r]]
            dp[r] += dp[px[r]]
            px[r] = px[px[r]]
            r = px[r]
        return acc

    def merge(self, x, y, dxy):
        dx, dy = self.weight(x), self.weight(y)
        xr, yr = self.root(x), self.root(y)
        dxy += dx - dy
        if xr == yr:
            return False
        if self.size[xr] < self.size[yr]:
            xr, yr, dxy = yr, xr, -dxy
        self.size[xr] += self.size[yr]
        self.parent[yr] = xr
        self.diff_p[yr] = dxy
        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def diff(self, x, y):
        if self.issame(x, y):
            return self.weight(y) - self.weight(x)
        return None

    def getsize(self, x):
        return self.size[self.root(x)]

def main():
    input_iter = iter(stdin.readline, '')
    while True:
        try:
            n, Q = map(int, next(input_iter).split())
        except StopIteration:
            break
        if n == 0 and Q == 0:
            break
        uf = PotUnionFind(n)
        for _ in range(Q):
            op, *args = next(input_iter).split()
            if op == '!':
                x, y, d = map(int, args)
                uf.merge(x-1, y-1, d)
            else:
                x, y = map(lambda v: int(v)-1, args)
                res = uf.diff(x, y)
                print(res if res is not None else "UNKNOWN")
main()