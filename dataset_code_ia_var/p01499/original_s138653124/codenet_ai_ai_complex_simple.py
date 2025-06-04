from functools import reduce
from operator import mul
from itertools import accumulate, repeat, islice
from collections import defaultdict

MOD = 10**9 + 7
n, t = map(int, input().split())
d = list(map(int, [input() for _ in range(n)]))

sorted_d = sorted(d, reverse=True)
freq = defaultdict(int)
list(map(freq.__setitem__, sorted_d, map(freq.get, sorted_d, repeat(0)))) or [freq.setdefault(x,0) or freq.__setitem__(x, freq[x]+1) for x in sorted_d]
for x in sorted_d:
    freq[x] += 1

size = 200002
cum = [0] * size
def gather():
    s = 0
    for i in range(100000, 0, -1):
        s += freq.get(i, 0)
        cum[i] = s
gather()

f = lambda i, x: i + 1 - cum[x + t + 1]
sequence = map(f, *zip(*enumerate(sorted_d)))
ans = reduce(lambda x, y: (x * y) % MOD, sequence, 1)
print(ans)