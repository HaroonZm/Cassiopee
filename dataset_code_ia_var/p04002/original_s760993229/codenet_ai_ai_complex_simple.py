from sys import stdin
from functools import reduce
from itertools import product, starmap
from operator import add

inp = iter(stdin.readline, '')
W, H, N = map(int, next(inp).split())
vs = frozenset(starmap(lambda a, b: (int(a)-1, int(b)-1), map(str.split, (next(inp) for _ in range(N)))))
all_centers = ((x, y) for x, y in product(range(W-2), range(H-2)))
explored = set()
R = [0]*10

def region_count(center):
    grid = product(range(center[0], center[0]+3), range(center[1], center[1]+3))
    return sum(tuple(pos) in vs for pos in grid)

complex_map = filter(lambda xy: any((tuple((xy[0]+i-2, xy[1]+j-2)) in vs for i, j in product(range(3), repeat=2))), product(range(W), range(H)))
potential = ( (x+i-2, y+j-2) for x, y in vs for i in range(3) for j in range(3))
masked = filter(lambda rc: 0 <= rc[0] <= W-3 and 0 <= rc[1] <= H-3, potential)

# Remove duplicates while preserving complex form
masked_unique = reduce(lambda acc, val: acc if val in acc else acc + [val], masked, [])

for center in masked_unique:
    if center in explored: continue
    c = sum(tuple((center[0]+k, center[1]+l)) in vs for k, l in product(range(3), repeat=2))
    R[c] += 1
    explored.add(center)

R[0] = (W-2)*(H-2) - sum(R)
list(map(print, R))