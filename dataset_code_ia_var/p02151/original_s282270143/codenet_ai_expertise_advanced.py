from collections import Counter
from itertools import combinations, permutations, product

N = int(input())
S = list(map(int, input()))

# Utilisation de Counter pour plus de vitesse (dict optimisé)
move = Counter()
pairs = zip(S, S[1:])
for a, b in pairs:
    move[(a, b)] += 1
    move[(b, a)] += 1

digits = set(range(1, 10))
bestscore = float('inf')
bestans = '9' * 9

# Vectorisation du calcul stage3 avec zip & sum, pour compacité et rapidité
def calc_br(bl, re):
    idxs = [
        ((0, 3), 1), ((0, 0), 1), ((0, 1), 3), ((0, 2), 3),
        ((1, 0), 1), ((1, 1), 1), ((1, 2), 3), ((1, 3), 3),
        ((2, 1), 1), ((2, 2), 1), ((2, 3), 3), ((2, 0), 3),
        ((3, 2), 1), ((3, 3), 1), ((3, 0), 3), ((3, 1), 3)
    ]
    return sum(weight * move[(bl[i], re[j])] for (i, j), weight in idxs)

# Canonicalisation par toutes les symétries du carré sous forme compacte
def canonical_grid(black, bl, re):
    grid = [bl[0], re[0], bl[1],
            re[3], black, re[1],
            bl[3], re[2], bl[2]]
    patterns = [
        (0, 1, 2, 3, 4, 5, 6, 7, 8),
        (2, 5, 8, 1, 4, 7, 0, 3, 6),
        (8, 7, 6, 5, 4, 3, 2, 1, 0),
        (6, 3, 0, 7, 4, 1, 8, 5, 2),
        (2, 1, 0, 5, 4, 3, 8, 7, 6),
        (0, 3, 6, 1, 4, 7, 2, 5, 8),
        (6, 7, 8, 3, 4, 5, 0, 1, 2),
        (8, 5, 2, 7, 4, 1, 6, 3, 0)
    ]
    return min(''.join(str(grid[i]) for i in pat) for pat in patterns)

for black in digits:
    remain = digits - {black}
    for blue in combinations(remain, 4):
        red = tuple(remain - set(blue))
        red_pairs = list(combinations(red, 2))
        stage1 = sum(move[(black, r)] for r in red) + \
                 2 * sum(move[(black, b)] for b in blue) + \
                 2 * sum(move[(r1, r2)] for r1, r2 in red_pairs)
        # Réduit à 3 ordres de blue (car cyclique, évite redondance)
        for bixs in ([0,1,2,3],[0,2,3,1],[0,3,1,2]):
            bl = tuple(blue[i] for i in bixs)
            stage2 = (
                move[(bl[0], bl[1])] + move[(bl[1], bl[2])] +
                move[(bl[2], bl[3])] + move[(bl[3], bl[0])] +
                2 * move[(bl[0], bl[2])] + 2 * move[(bl[1], bl[3])]
            ) * 2
            for re in permutations(red):
                total = stage1 + stage2 + calc_br(bl, re)
                if total < bestscore or (total == bestscore and canonical_grid(black, bl, re) < bestans):
                    bestscore = total
                    bestans = canonical_grid(black, bl, re)

print(bestans[:3])
print(bestans[3:6])
print(bestans[6:9])