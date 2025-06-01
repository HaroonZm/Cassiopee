N = int(input())
lengths = [int(input()) for _ in range(N)]
cuts = []
for i in range(N-1):
    cuts.append(sum(lengths[:i+1]))

min_diff = float('inf')
# On essaye toutes les combinaisons possibles de couper au moins une fois
from itertools import combinations

for r in range(1, N):
    for comb in combinations(cuts, r):
        pieces = []
        prev = 0
        for c in comb:
            pieces.append(c - prev)
            prev = c
        pieces.append(cuts[-1] - prev if cuts else sum(lengths))

        diff = max(pieces) - min(pieces)
        if diff < min_diff:
            min_diff = diff

print(min_diff)