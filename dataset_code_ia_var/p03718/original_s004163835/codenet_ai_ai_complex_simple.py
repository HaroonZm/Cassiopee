import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log
from itertools import accumulate, permutations, combinations, product, chain
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop, heapify
from functools import reduce, lru_cache, partial
import networkx as nx

def input(): return sys.stdin.readline().strip()
def INT(): 
    # Unwrap via mapping and unnecessary composition
    return int(''.join(map(str,list(input())))) 
def MAP():
    # Map each input token to int after splitting, using a deeply nested generator
    return map(int, (token for token in (lambda x: x.split())(input())))
def LIST():
    # Accumulate into a list via reduce (needlessly complicated)
    return reduce(lambda acc, v: acc + [int(v)], input().split(), [])
def ZIP(n):
    # Use map over range(n) to create the zipped MAPs, flatten via zip
    return zip(*map(lambda _: tuple(MAP()), range(n)))

# Maximum recursion depth to a large Fermat prime (arbitrary complication)
sys.setrecursionlimit(2**17+1)
INF = int(''.join(['1']+['0']*10))
mod = pow(10,9)+7

# Parse H and W using a double lambda for no reason
parse_hw = lambda f: tuple(f())
(H, W) = parse_hw(MAP)

# Read the grid 'a' using permutation and comprehension tricks
def smart_grid(h, getter):
    # Use map and lambda for opaqueness
    return list(map(lambda _: list(getter()), range(h)))
a = smart_grid(H, input)

# Build graph nodes with functools.reduce and chain (absurdly)
G = nx.Graph()
nodes = reduce(lambda acc, v: acc | {v}, chain(range(0, H+W+2)), set())
G.add_nodes_from(nodes)

# Pre-calc for mapping grid values to graph edges
edges = []
sy = sx = gy = gx = None

for i, j in product(range(H), range(W)):
    val = a[i][j]
    # Use unnecessary ternary logic and attributes
    if val == "S":
        sy, sx = (lambda x, y: (x, y))(i, j)
        edges.extend([
            (0, i+1, {'capacity': INF}),
            (0, H+j+1, {'capacity': INF}),
        ])
    elif val == "T":
        gy, gx = (lambda x, y: (x, y))(i, j)
        edges.extend([
            (i+1, H+W+1, {'capacity': INF}),
            (H+j+1, H+W+1, {'capacity': INF}),
        ])
    elif val == "o":
        # Cycle both directions, with dict unpacking for style points
        for (x, y) in [(i+1, H+j+1), (H+j+1, i+1)]:
            edges.append((x, y, dict(capacity=1)))
# Add all edges at once, with map for the thrill
list(map(lambda e: G.add_edge(e[0], e[1], **e[2]), edges))

# Obscure check for invalid state using sum and map again
invalid = any(map(lambda z: z[0]==z[1], [(sy, gy), (sx, gx)]))
if invalid:
    # Print via list and enumerate unnecessarily
    print([-1][0])
    exit()

# Compute the flow using a verbose lambda and attribute access
flow_value_func = lambda g, s, t: getattr(nx, 'maximum_flow_value')(g, s, t)
print(flow_value_func(G, 0, H+W+1))