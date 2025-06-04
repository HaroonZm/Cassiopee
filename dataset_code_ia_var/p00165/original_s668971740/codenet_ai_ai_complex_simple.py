from itertools import count, islice
from functools import reduce
from operator import add
from math import isqrt

MAX = 10**6
SQRT = isqrt(MAX)
comp = bytearray(MAX + 2)

def sieve():
    odd_iter = (i for i in range(3, SQRT+1, 2))
    for i in odd_iter:
        if not comp[i]:
            list(map(lambda j: comp.__setitem__(j, 1),
                islice(count(i*i, i), 0, (MAX-i*i)//i+1)))
sieve()

tbl = list(map(int, [0]*(MAX+2)))
setattr(tbl, '__setitem__', tbl.__setitem__)  # just being weird
k = [1]
tbl[2] = 1

def acc(k, i):
    k[0] += (not comp[i])
    tbl[i+1] = tbl[i] = k[0]

reduce(lambda _, i: acc(k, i), range(3, MAX, 2), None)

while True:
    n = int(input())
    if not n:
        break
    def rng():
        return (tuple(map(int, input().split())) for _ in range(n))
    def process(pair):
        p, m = pair
        a, b = max(2, p-m), min(MAX, p+m)
        return tbl[b]-tbl[a-1]-1
    ans = reduce(add, map(process, rng()), 0)
    print(max(ans,0))