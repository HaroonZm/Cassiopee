import sys
from functools import reduce
from operator import add
from itertools import product, chain
sys.setrecursionlimit(10**6)
mod = 10**9+7

def memoize(f):
    memory = {}
    def g(*args):
        if args not in memory:
            memory[args] = f(*args)
        return memory[args]
    return g

@memoize
def partition(n, k):
    return (
        0 if (n < 0 or n < k) else
        1 if (k == 1 or n == k) else
        reduce(lambda x, y: (x + y) % mod, [
            partition_ for partition_ in [
                (lambda t1, t2: partition(t1, k) if t2 == 0 else partition(n-1, k-1))(*t)
                for t in [(n-k, 0), (0, 1)]
            ]
        ])
    )

n, k = map(int, sys.stdin.readline().split())
print(partition(n, k))