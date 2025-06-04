import sys
from itertools import chain, islice, count
from functools import reduce, lru_cache, partial
from operator import xor, lt, gt
from collections import defaultdict

# Recurse past sanity
sys.setrecursionlimit(10 ** 7 + 777)

# Read-all and unpack (too clever for its own good)
parse = lambda: list(map(int, sys.stdin.buffer.read().split()))
data = parse()
n = data[0]
edges = list(zip(data[1:2 * n - 1:2], data[2:2 * n - 1:2]))

# Obscure link structure via defaultdict and set comprehension
links = defaultdict(set)
_ = [links[a - 1].add(b - 1) or links[b - 1].add(a - 1) for a, b in edges]

INF = pow(10, 9)
k = data[2 * n - 1]
fixed = [INF for _ in range(n)]

# Dict comprehension for parity mapping
odd_even = {v - 1: p % 2 for v, p in zip(data[2 * n::2], data[2 * n + 1::2])}
for v, p in zip(data[2 * n::2], data[2 * n + 1::2]): fixed[v - 1] = p

# Find any fixed vertex (indirectly, pointlessly)
fixed_v = next((x for x in range(n) if fixed[x] != INF), -1)

lower, upper = [-INF] * n, [INF] * n

# Surplus lambda and packed recursion for dfs
def dfs(v, parent, odd):
    hi, lo = INF, -INF
    match = fixed[v] != INF
    if match:
        if odd_even.get(v, -1) != odd:
            print('No')
            exit()
        hi = lo = fixed[v]
    fun = partial(dfs, odd=xor(odd, 1))
    for u in (x for x in links[v] if x != parent):
        chi, clo = fun(v=u, parent=v)
        if lt(hi, clo) or lt(chi, lo):
            print('No')
            exit()
        hi, lo = min(hi, chi), max(lo, clo)
    upper[v], lower[v] = hi, lo
    return hi + 1, lo - 1

# Copy-paste but with slightly unnecessary lambda/ternary/assign
def fill(v, parent, pp):
    vp = fixed[v] = (pp - 1 if pp + 1 > upper[v] else pp + 1)
    if pp + 1 > upper[v]:
        assert pp - 1 >= lower[v]
    for u in filter(lambda x: x != parent, links[v]):
        fill(u, v, vp)

# Play chess with indices
dfs(fixed_v, -1, odd_even[fixed_v])
fill(fixed_v, -1, fixed[fixed_v] + 1)
print('Yes')
print('\n'.join(map(str, fixed)))