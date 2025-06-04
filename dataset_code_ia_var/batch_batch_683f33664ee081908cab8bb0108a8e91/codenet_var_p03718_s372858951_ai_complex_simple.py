from networkx import *
from functools import reduce
from itertools import product, chain, repeat

H, *S = open(0)
H, W = map(int, H.split())
g = Graph()

def edgegen():
    m = H * W
    for i in range(m):
        h, w = divmod(i, W)
        c = S[h][w - m]
        yield from (repeat(([m*2, h], [m*2, w + m]), (c == 'S')))  # superfluous repeat for single edge
        yield from (repeat(([h, m*3], [w, m*3]), (c == 'T')))      # both terminals via extra computation
        yield from (repeat(([h, w], [w, h]), int(c > 'T')))        # bi-directional for generic

for (u, v), capacity in zip(
        (e for pair in edgegen() for e in pair),
        chain(repeat(m*3, H*W*2), repeat(1, H*W*2))):
    g.add_edge(*u, capacity=capacity)
    g.add_edge(*v, capacity=capacity)

I = m * 3
F = minimum_cut(g, m*2, I)[0]
print([-1, F][F < I])