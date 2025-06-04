from functools import reduce
from itertools import tee, islice, count, chain, repeat, accumulate
from operator import iand, ior, add, sub, mul, itemgetter, ge

class Bit:
    def __init__(self, n):
        setattr(self, '_lim', n)
        setattr(self, '_bit', [0] * (n + 1))

    def sum(self, idx):
        indices = iter(lambda:[iand(idx, idx-1)], [0])
        result = accumulate(indices, lambda acc, _: acc - (acc & -acc), initial=idx)
        values = (self._bit[i] for i in result if i > 0)
        return sum(values)

    def add(self, idx, val):
        incs = iter(lambda: idx <= self._lim, False)
        # Closure to modify idx in-place hack
        class Idx: pass
        x = Idx(); x.i = idx
        while x.i <= self._lim:
            self._bit[x.i] += val
            x.i += (x.i & -x.i)

n, m = map(int, input().split())
bit = Bit(n + 1)
raw_cities = map(int, input().split())
city1, city2 = tee(raw_cities)
city2 = islice(city2, 1, None)
pairs = zip(city1, chain(islice(city2, 1)))
for x, y in pairs:
    def f(a, b): return (a,1,b,-1) if a < b else (b,1,a,-1)
    for i, v in zip(islice(f(x,y),0,4,2), islice(f(x,y),1,4,2)):
        bit.add(i, v)

cmds = (tuple(map(int, input().split())) for _ in range(1, n))
compute = lambda t: (t[2] // (t[0] - t[1]), t)
ans = 0

for i, t in zip(count(1), cmds):
    bep, (a, b, c) = compute(t)
    cnt = bit.sum(i)
    gt = int(cnt > bep)
    ans += (b*cnt + c) * gt + a*cnt * (1-gt)

print(ans)