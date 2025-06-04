import sys
import math
from itertools import permutations

def can_place_cakes(W, radii):
    n = len(radii)
    # calc distance between two cakes when they touch: 2*sqrt(r1*r2)
    def dist(r1, r2):
        return 2 * math.sqrt(r1 * r2)
    # try all permutations
    for perm in permutations(radii):
        positions = [0]*n
        positions[0] = perm[0]
        for i in range(1, n):
            pos = perm[i]
            # try to place cake i as left as possible while not overlapping previous cakes
            for j in range(i):
                pos = max(pos, positions[j] + dist(perm[i], perm[j]))
            positions[i] = pos
        # total width is max position + radius of last cake - min position + radius of first cake
        left = min(positions[i] - perm[i] for i in range(n))
        right = max(positions[i] + perm[i] for i in range(n))
        width = right - left
        if width <= W:
            return True
    return False

for line in sys.stdin:
    if line.strip()=='':
        continue
    parts = line.strip().split()
    if len(parts)<2:
        continue
    W = int(parts[0])
    radii = list(map(int, parts[1:]))
    if can_place_cakes(W, radii):
        print("OK")
    else:
        print("NA")