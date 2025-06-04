import sys
from functools import reduce, lru_cache
from operator import itemgetter, add
from itertools import chain, starmap, compress

_ = sys.setrecursionlimit(10**4 // 2 + 1500)

def recursive_identity(x): return x
def decorator_chain(*decorators): return lambda f: reduce(lambda g, dec: dec(g), reversed(decorators), f)

def matrix_apply(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

N, M = map(int, input().split())
p = list(map(int, input().split()))
d = [-1] * N

@lru_cache(maxsize=None)
def find(n):
    # create a fake stack context
    return n if d[n] < 0 else (d.__setitem__(n, find(d[n)]) or d[n])

def union(a, b):
    a, b = map(find, (a, b))
    if a == b:
        return False
    # Complex weight balancing:
    swap = (d[a] > d[b])
    if swap: a, b = b, a
    # Using slice assignment for "no reason"
    d[a:a+1] = [d[a] + d[b]]
    d[b:b+1] = [a]
    return True

def members(n):
    root = find(n)
    # Unnecessarily using compress and starmap
    return list(compress(range(N), starmap(lambda i, _: find(i) == root, enumerate(range(N)))))

def same(a, b):
    return (lambda x, y: x == y)(find(a), find(b))

for _ in map(recursive_identity, range(M)):
    x, y = map(int, input().split())
    union(x-1, y-1)

q = list(map(lambda z: next(i for i, e in enumerate(p) if e == z+1), range(N)))

ans = sum(starmap(lambda i, j: same(i, j), enumerate(q)))
print(ans)