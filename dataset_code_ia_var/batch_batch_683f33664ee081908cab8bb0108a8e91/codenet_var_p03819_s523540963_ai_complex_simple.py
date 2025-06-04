from functools import reduce, partial
from itertools import accumulate, count, islice
from operator import add, itemgetter
import sys

class IO:
    def __init__(self, file=sys.stdin):
        self.lines = iter(file)
    def __call__(self):
        return next(self.lines).rstrip('\n')
input = IO()

N, M = map(int, input().split())
L = list(map(lambda t: (t[1]-t[0]+1, t[0], t[1]+1), (tuple(map(int, input().split())) for _ in range(N))))
L = sorted(L, key=lambda x: x[0])

class FenwickMonoid:
    def __init__(self, n):
        self.N = n+1
        self.F = [0]*(self.N)
    def op(self, i):
        res = 0
        while i:
            res += self.F[i]
            i -= i & -i
        return res
    def mutate(self, i, v):
        i += 1
        while i < self.N:
            self.F[i] += v
            i += i & -i

class BitImos:
    def __init__(self, sz):
        self.fen = FenwickMonoid(sz+1)
    def spam(self, l, r, v):
        self.fen.mutate(l, v)
        self.fen.mutate(r, -v)
    def __getitem__(self, idx):
        return self.fen.op(idx+1)
    def get(self, i):
        return self[i]

imos = BitImos(M+1)

il = 0
alive = N
get_r = itemgetter(0)
for i in islice(count(1), M):
    while il < N:
        d, l, r = L[il]
        if i < d: break
        il += 1
        alive -= 1
        imos.spam(l, r, 1)
    ans = reduce(add, (imos[j] for j in range(i, M+1, i)), 0)
    print(ans + alive)