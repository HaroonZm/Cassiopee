case_number = 1
while True:
    W = int(input())
    if W == 0:
        break
    N = int(input())
    items = []
    for _ in range(N):
        line = input().strip()
        v_str, w_str = line.split(',')
        v = int(v_str)
        w = int(w_str)
        items.append((v, w))

    # dp[x] = (max_value, min_weight_for_max_value) for capacity x
    dp = [(-1, 0)] * (W + 1)
    dp = [(-1, 0) for _ in range(W + 1)]
    dp[0] = (0, 0)

    for v, w in items:
        for x in range(W, w -1, -1):
            if dp[x - w][0] < 0:
                continue
            new_value = dp[x - w][0] + v
            if new_value > dp[x][0]:
                dp[x] = (new_value, dp[x - w][1] + w)
            elif new_value == dp[x][0] and dp[x - w][1] + w < dp[x][1]:
                dp[x] = (new_value, dp[x - w][1] + w)

    max_value = 0
    min_weight = 0
    for x in range(W + 1):
        val, wei = dp[x]
        if val > max_value:
            max_value = val
            min_weight = wei
        elif val == max_value and val != -1 and wei < min_weight:
            min_weight = wei

    print(f"Case {case_number}:")
    print(max_value)
    print(min_weight)
    case_number += 1