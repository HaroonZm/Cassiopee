case_num = 1
while True:
    W = int(input())
    if W == 0:
        break
    N = int(input())
    items = []
    for _ in range(N):
        v, w = input().split(',')
        v = int(v)
        w = int(w)
        items.append((v, w))

    # dp[value] = minimum_weight_to_achieve_value
    max_value_sum = sum(v for v, w in items)
    INF = 10**9
    dp = [INF] * (max_value_sum + 1)
    dp[0] = 0

    for v, w in items:
        for val in range(max_value_sum - v, -1, -1):
            if dp[val] + w < dp[val + v]:
                dp[val + v] = dp[val] + w

    # find max value with weight <= W, if tie min weight
    max_val = 0
    min_weight = 0
    for val in range(max_value_sum + 1):
        if dp[val] <= W:
            if val > max_val:
                max_val = val
                min_weight = dp[val]
            elif val == max_val and dp[val] < min_weight:
                min_weight = dp[val]

    print(f"Case {case_num}:")
    print(max_val)
    print(min_weight)
    case_num += 1