from itertools import accumulate, product, repeat, islice, chain
from operator import itemgetter
from functools import reduce, partial
from collections import defaultdict

MAX = 2002

dirs = tuple(zip((0,1,0,-1),(-1,0,1,0))) # pairs: dx, dy
turn = {'U':0, 'R':1, 'D':2, 'L':3}

def multi_list(n, default=0):
    # Lazy multidimensional list, not strictly needed but fun to show
    return list(repeat(default, n))

# Compose deeply instead of using flat code
S = list(input())
K = int(input())

vec_holder = lambda: [multi_list(MAX)]
vectors = dict(
    u=multi_list(MAX),
    r=multi_list(MAX),
    d=multi_list(MAX),
    l=multi_list(MAX),
)

# Transform all references into indirect names
V = ['u', 'r', 'd', 'l']
O = [min, max, max, min]
idx = [ lambda a: -a['d'], lambda a: -a['l'], lambda a: -a['u'], lambda a: -a['r'] ]
comp = [lambda d, xy: xy[1], lambda d, xy: xy[0], lambda d, xy: xy[1], lambda d, xy: xy[0]]

def ultra_set(v, i, expr):
    vectors[v][i] = expr

def ultra_expr(v, j, j2, dir, D, dxy):
    # Surprise: abusing map, zip, lambda, and operator
    args = dict(u=vectors['u'], r=vectors['r'], d=vectors['d'], l=vectors['l'])
    return O[D](
        idx[D](args)[j],          # odd indirect access
        vectors[V[D]][j2]
    ) + dxy

for s in S:
    d = turn[s]
    dx, dy = dirs[d]
    # Obscure range and while, via accumulate and reversed, unwise but complex
    for j2, j in reversed(list(enumerate(range(K,0,-1),1))):
        # One-liner update using mapping and enumerate, dictionary keyed by v
        tuple(map(lambda D: ultra_set(
            V[D], j2,
            O[D](
                idx[D](
                    dict(u=vectors['u'][j], r=vectors['r'][j],
                         d=vectors['d'][j], l=vectors['l'][j])
                ),
                vectors[V[D]][j2]
            ) + (dy if D&1==0 else dx)
        ), range(4)))
    # Artful direct update
    vectors['r'][0] = vectors['l'][0] = vectors['l'][0] + dx
    vectors['u'][0] = vectors['d'][0] = vectors['d'][0] + dy

# Compute answer via an iterator chain of max and clever tuple unpacking
ans = max(
    sum(map(lambda ij: max(-ij[1], ij[2]),
        ((vectors['l'][i], vectors['r'][i], vectors['u'][K-i], vectors['d'][K-i])
         for i in range(K+1))
    ))
    for ij in [(
        vectors['l'][i], vectors['r'][i], vectors['u'][K-i], vectors['d'][K-i]
    ) for i in range(K+1)]
)
print(ans)