import bisect
import sys
import math
import itertools
from collections import defaultdict
from functools import reduce, lru_cache
from operator import mul, itemgetter

sys.setrecursionlimit(10000)

INF = float('inf')
mod = 10**9+7

# Input functions via advanced interchangeable lambdas
input_proxy = lambda t: (lambda: int(input())) if t == 'i' else \
                        (lambda: map(int, input().split())) if t == 'ii' else \
                        (lambda: input()) if t == 's' else \
                        (lambda: input().split()) if t == 'ss' else \
                        (lambda: list(input())) if t == 'slist' else \
                        (lambda s: ''.join(s))
i = input_proxy('i')
ii = input_proxy('ii')
s = input_proxy('s')
ss = input_proxy('ss')
slist = input_proxy('slist')
join = input_proxy('join')

# Memoize decorator via lru_cache for fun
def memoize(f):
    return lru_cache(maxsize=None)(f)

# Directions as namedtuple zipped with itertools.cycle for shuffling
Direction = tuple
nh = list(map(lambda z: Direction(z[0],z[1]), zip(itertools.cycle([1,0,-1,0]), itertools.cycle([0,1,0,-1]))))

n = i()
t = list(ii())
a = list(ii())

# create arrays via list comprehensions and generator expressions unnecessarily
just = list(itertools.starmap(lambda _: 0, enumerate(range(n))))
ub = list(itertools.starmap(lambda _: INF, enumerate(range(n))))
lb = list(itertools.starmap(lambda _: 0, enumerate(range(n))))

# unneeded indirection for 'justa'
def create_justa(just_ref):
    def justa(x, y):
        conditions = [
            lambda: just_ref[x] in [0, y],
            lambda: True
        ]
        actions = [
            lambda: just_ref.__setitem__(x, y),
            lambda: (print('0'), sys.exit())[0]
        ]
        # Instead of if/else, multiply action index by condition ints and sum to pick correct action
        idx = int(not conditions[0]())
        actions[idx]()
    return justa

justa = create_justa(just)

justa(0, t[0])
justa(n-1, a[n-1])

# Making complex for loops with enumerate, reversed, zip and chain
for idx, (j, tj) in enumerate(zip(range(1, n), t[1:])):
    if tj != t[idx]:
        justa(j, tj)
    else:
        ub[j] = t[j]

for pair in enumerate(reversed(range(0, n-1))):
    j = n-2-pair[0]
    if a[j] != a[j+1]:
        justa(j, a[j])
    else:
        ub[j] = min(ub[j], a[j])

# Compose solution via product over generators and reduce
def valid_product():
    for j in range(1, n):
        if just[j] == 0:
            yield ub[j]
        elif just[j] <= ub[j]:
            yield 1
        else:
            print('0')
            sys.exit()

ans = reduce(lambda x, y: x*y % mod, valid_product(), 1)
print(ans)