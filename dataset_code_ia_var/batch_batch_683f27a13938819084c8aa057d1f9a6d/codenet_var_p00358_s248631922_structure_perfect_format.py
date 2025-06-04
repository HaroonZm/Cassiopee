h, n = map(int, input().split())
state_lst = [0] * h
for _ in range(n):
    x, y = map(int, input().split())
    state_lst[y] += 2 ** x

left_mask = 3
middle_mask = 6
right_mask = 12
all_mask = 15

INF = 10 ** 20
dp = [[-INF] * (2 ** 4) for _ in range(h + 1)]
dp[0][all_mask] = 0

for i in range(h):
    state = state_lst[i]
    for mask in (left_mask, middle_mask, right_mask):
        if (state & mask):
            continue
        for pre_state in range(16):
            if (pre_state & mask):
                continue
            dp[i + 1][state | mask] = max(dp[i + 1][state | mask], dp[i][pre_state] + 1)
    if state:
        dp[i + 1][all_mask] = max(dp[i + 1][all_mask], -INF)
    else:
        dp[i + 1][all_mask] = max(dp[i + 1][all_mask], dp[i][0] + 2)
    dp[i + 1][state] = max(dp[i + 1][state], max(dp[i]))

print(max(dp[h]))