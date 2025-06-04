import sys
from itertools import permutations, combinations

W, H = 4, 4
N = 8
letters = 'ABCDEFGH'
pairs = [(i, (i + 1) // 2) for i in range(16)]

# Generate all possible pairs of positions that satisfy any of the given relative positions
def get_pairs(rel_pos):
    pairs = []
    for y in range(H):
        for x in range(W):
            for dx, dy in rel_pos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H:
                    pairs.append(((x, y), (nx, ny)))
    return pairs

# Checks if two pairs overlap (share any cell)
def overlap(p1, p2):
    return len(set(p1) & set(p2)) > 0

# Build graph of compatible pairs (non-overlapping)
# Goal: find all perfect matchings of 8 edges covering all 16 cells with given relative positions and pattern counts
def search(matchings, edges, used, idx, rel_pos_fixed):
    if idx == len(edges):
        if len(matchings) == N:
            # Convert matching positions to pattern representation
            base = sorted(matchings)
            pattern = [None]*16
            for i, (a, b) in enumerate(base):
                pattern[a[1]*W+a[0]] = i
                pattern[b[1]*W+b[0]] = i
            # Canonical form: sort pairs, relabel by pair indices
            # We use tuple sorted pairs to avoid duplicates (patterns)
            key = tuple(sorted(tuple(sorted((a[1]*W+a[0], b[1]*W+b[0]))) for (a,b) in base))
            rel_pos_fixed.add(key)
        return
    a, b = edges[idx]
    if not used[a[1]*W+a[0]] and not used[b[1]*W+b[0]]:
        used[a[1]*W+a[0]] = used[b[1]*W+b[0]] = True
        matchings.append((a, b))
        search(matchings, edges, used, idx + 1, rel_pos_fixed)
        matchings.pop()
        used[a[1]*W+a[0]] = used[b[1]*W+b[0]] = False
    search(matchings, edges, used, idx + 1, rel_pos_fixed)

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    while idx + 7 < len(input_data):
        vals = list(map(int, input_data[idx:idx+8]))
        idx += 8
        if any(v > 4 for v in vals[:1]):
            break
        rel_pos = [(vals[0], vals[1]), (vals[2], vals[3]), (vals[4], vals[5]), (vals[6], vals[7])]
        edges = get_pairs(rel_pos)
        rel_pos_fixed = set()
        used = [False]*16
        search([], edges, used, 0, rel_pos_fixed)
        # Now count unique patterns ignoring permutations of pairs (patterns are unique in rel_pos_fixed)
        print(len(rel_pos_fixed))

if __name__ == '__main__':
    main()