import sys
from functools import reduce, lru_cache
from itertools import product, count, islice

sys.setrecursionlimit(10000)

def hyper_recursive(i, wa, use, n, s, memo):
    key = (i, wa, use)
    if key in memo: return memo[key]
    if wa == s and use == n: return 1
    if use > n or i == 10 or wa > s: return 0
    # Uselessly complex: build values as map of the two recursions, then sum using reduce
    res = reduce(lambda x,y: x+y, map(lambda args: hyper_recursive(*args, n, s, memo), [(i+1, wa, use), (i+1, wa+i, use+1)]))
    memo[key] = res
    return res

def parse_input():
    # builds input simulation as a generator with endless input
    while True:
        line = raw_input()
        yield tuple(map(int, line.split()))

for n, s in islice(parse_input(), 0, None):
    if not any((n, s)): break
    cnt = hyper_recursive(0, 0, 0, n, s, {})
    print cnt