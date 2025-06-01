h, n = map(int, input().split())
state_lst = [0] * h
for _ in range(n):
    x, y = map(int, input().split())
    state_lst[y] |= 1 << x

LEFT, MID, RIGHT, ALL = 0b0011, 0b0110, 0b1100, 0b1111
INF = float('-inf')
dp = [[INF] * 16 for _ in range(h + 1)]
dp[0][ALL] = 0

for i, state in enumerate(state_lst, 1):
    prev_row = dp[i - 1]
    curr_row = dp[i]
    max_prev = max(prev_row)
    
    for mask in (LEFT, MID, RIGHT):
        if state & mask:
            continue
        for pre_state, val in enumerate(prev_row):
            if val == INF or pre_state & mask:
                continue
            combined = state | mask
            if val + 1 > curr_row[combined]:
                curr_row[combined] = val + 1
    
    if not state:
        curr_row[ALL] = max(curr_row[ALL], prev_row[0] + 2)
    else:
        curr_row[ALL] = max(curr_row[ALL], INF)
    
    curr_row[state] = max(curr_row[state], max_prev)

print(max(dp[h]))