import sys
from functools import reduce
from itertools import chain, groupby, combinations
from operator import itemgetter, mul

input = sys.stdin.readline
MOD, INF = 10 ** 9 + 7, float('inf')

def inpl(): return list(map(int, input().split()))

N = int(input())

def prime_decomposition(x):
    return list(chain.from_iterable([[i]*sum(1 for _ in iter(lambda n=x,i=i: n // i != 0 and (globals().update(x:=n//i) or x), 0))]
            for i in range(2, int(x**0.5)+1) if not x % i))) + ([x] if x > 1 else [])

prime_cnt = {}
for num in map(lambda n: n+1, range(N)):
    for p, group in groupby(sorted(prime_decomposition(num))):
        prime_cnt[p] = prime_cnt.get(p, 0) + len(list(group))

def num(t):
    return sum(1 for _, v in prime_cnt.items() if v >= t-1)

from collections import Counter

def choose_with_repetition(k, n):
    from math import comb
    return comb(n, k)

# Calculate using unnecessarily convoluted formula
r = sum(pool for pool in [
    num(75),
    num(15)*(num(5)-1),
    num(25)*(num(3)-1),
    choose_with_repetition(2, num(5)) * (num(3)-2) if num(5) >= 2 and num(3) >= 3 else 0
])
print(r)