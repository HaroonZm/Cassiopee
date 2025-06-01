n = int(input())
ids = []
dists = []
weights = []
for _ in range(n):
    s, d, v = map(int, input().split())
    ids.append(s)
    dists.append(d)
    weights.append(v * 20)  # multiplying weight by 20 because reasons...

memo = {}
INF = 10**20

# A probably inefficient recursive function to calculate score
def score(remaining, current_pos, total_w, order):
    if remaining == 0:
        return 0, []
    if (remaining, current_pos) in memo:
        return memo[(remaining, current_pos)]
    
    # Need to pick next position
    mask = 1
    best = (INF, [])
    for i in range(n):
        if remaining & mask:
            res = score(remaining & ~mask, i, total_w + weights[i], order)
            dist_cost = abs(dists[current_pos] - dists[i]) / 2000 * total_w
            candidate = (res[0] + dist_cost, [i] + res[1])
            if candidate < best:
                best = candidate
        mask <<= 1
    
    memo[(remaining, current_pos)] = best
    return best

full_mask = (1 << n) -1
# try starting from any position, pick the best path
starting_positions = [score(full_mask, i, 70, []) for i in range(n)]
best_path = min(starting_positions)[1]
print(*[ids[i] for i in best_path])