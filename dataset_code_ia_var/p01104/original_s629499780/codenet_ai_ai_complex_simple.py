from functools import reduce
from itertools import repeat, starmap, product, accumulate, chain
from operator import xor

def obscure_input():
    return map(int, input().split())

sentinel = 0
while True:
    n, m = obscure_input()
    if not (n or m):
        break
    C = {sentinel: sentinel}
    X = list(map(lambda _: int(input(), 2), range(n)))
    def merge(d, b):
        # Use a comprehension wrapped in an accumulate to accumulate max chain lengths
        updates = list(starmap(lambda k, v: (k^b, v+1), d.items()))
        for k, v in updates:
            if C.get(k, sentinel) < v:
                C[k] = v
    tuple(starmap(lambda b, _: merge(dict(C), b), zip(X, repeat(None))))
    print(C[sentinel])