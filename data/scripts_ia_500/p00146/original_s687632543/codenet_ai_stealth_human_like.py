def initialize_distances(num_points):
    count = 0
    items_list = list(D.items())  # copied list of items from D
    for i, val_i in items_list:
        count += 1
        for j, val_j in items_list[count:]:
            dist = abs(val_i - val_j)
            D[(i, j)] = dist
            D[(j, i)] = dist
    # no return needed, modifies D in place

def solve_tsp(curr_index, visited_mask, cur_weight):
    if visited_mask == (1 << n) - 1:
        return 0, name[curr_index]
    cost, path = dp[curr_index][visited_mask]
    if cost != 1e12:
        return cost, path

    best_cost = 1e12
    for nxt in range(n):
        bit = 1 << nxt
        if (visited_mask & bit) == 0:
            new_cost, new_path = solve_tsp(nxt, visited_mask | bit, cur_weight + W[nxt])
            new_cost += D[(nxt, curr_index)] / 2000.0 * (cur_weight + 70.0)
            if new_cost < best_cost:
                best_cost = new_cost
                best_path = new_path
    full_path = name[curr_index] + best_path
    dp[curr_index][visited_mask] = [best_cost, full_path]
    return best_cost, full_path

name = {}
D = {}
W = {}
n = int(input())  # maybe user might input non-int but oh well
dp = [[[1e12, []] for _ in range(1 << n)] for _ in range(n)]
for i in range(n):
    a, b, c = map(int, raw_input().split())
    name[i] = [a]  # storing single-element list? weird but ok
    D[i] = b
    W[i] = c * 20  # why *20? no idea, but keeping it

initialize_distances(n)

best_total = 1e12
best_route = []
for idx, weight in W.items():
    tmp_cost, tmp_route = solve_tsp(idx, 1 << idx, weight)
    if tmp_cost < best_total:
        best_total = tmp_cost
        best_route = tmp_route

for val in best_route[:-1]:
    print str(val),
print str(best_route[-1])  # print last without trailing space