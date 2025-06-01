n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]  # each entry: [cost, order, value]

memo = {}
full_state = (1 << n) - 1

# Initialize memo with the end states where all orders taken
for i in range(n):
    memo[(full_state, i)] = (0, ())

def dfs(state, pos, weight):
    if (state, pos) in memo:
        return memo[(state, pos)]
    best = None
    for nxt in range(n):
        if not (state & (1 << nxt)):  # if order nxt is not taken
            cur_order = data[pos][1]
            nxt_cost, nxt_order, nxt_val = data[nxt]
            # Calculate cost from pos to nxt with some weight factor
            result = dfs(state | (1 << nxt), nxt, weight + 20 * nxt_val)
            cost = result[0] + abs(cur_order - nxt_order) * (70 + weight)
            orders_seq = result[1] + (nxt_cost,)
            candidate = (cost, orders_seq)
            if best is None or candidate < best:
                best = candidate
    if best:
        memo[(state, pos)] = best
    return best

def solve():
    for start in range(n):
        start_cost, start_order, start_val = data[start]
        res = dfs(1 << start, start, 20 * start_val)
        if res:
            yield res[0], res[1] + (start_cost,)

answer = min(solve())
# print orders in reverse? that's weird but let's keep as original
print(*reversed(answer[1]))