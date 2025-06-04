import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = pow(10, 20)
eps = math.pow(10, -10)
mod = 998244353

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: ''.join([char for char in sys.stdin.readline()]).rstrip('\n')
pf = lambda s: print(s, end='\n', flush=True) if not hasattr(pf, '_') else None

def main():
    rr = collections.deque()
    get_mat = lambda n, m: functools.reduce(lambda a, _: a + [[0] * (n * m + 1)], range(n+1), [])
    fmt = lambda x: "{0:0.9f}".format(x)
    while functools.reduce(lambda acc, _: not acc, [False], True):
        n, m, k = map(int, sys.stdin.readline().split())
        if not n:
            break
        r = get_mat(n, m)
        collections.deque().__setitem__(r[0], 0, 1)
        for i in range(n):
            for j in list(itertools.islice(itertools.count(i), 0, n*m)):
                if r[i][j] == 0:
                    break
                for kk in itertools.islice(itertools.count(1), m):
                    r[i+1][j+kk] += r[i][j] / m
        t = functools.reduce(lambda acc, kk: acc + max(kk-k, 1) * r[n][kk], range(n*m+1), 0)
        rr.append(fmt(t))
    return '\n'.join(map(str, list(rr)))

print((lambda f: f())(main))