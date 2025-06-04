import sys
import math
from itertools import permutations

def can_place(W, radii):
    n = len(radii)
    # For each permutation, check if cakes fit
    for perm in permutations(radii):
        # Calculate total width
        total_width = perm[0] * 2
        for i in range(n - 1):
            d = math.sqrt((perm[i] + perm[i+1])**2 - (perm[i] - perm[i+1])**2)
            total_width += d
        if total_width <= W + 1e-9:
            return True
    return False

input_lines = sys.stdin.read().strip().split('\n')
for line in input_lines:
    if not line.strip():
        continue
    tokens = line.strip().split()
    W = int(tokens[0])
    radii = list(map(int, tokens[1:]))
    if can_place(W, radii):
        print("OK")
    else:
        print("NA")