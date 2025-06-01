case_number = 1
while True:
    W = int(input())
    if W == 0:
        break
    N = int(input())
    items = []
    for _ in range(N):
        line = input().strip()
        v, w = line.split(',')
        v = int(v)
        w = int(w)
        items.append((v, w))

    # dp[i][j] = (max_value, min_weight_for_that_value)
    # We'll use one dimension dp and update from W down to 0
    dp = [ (0,0) for _ in range(W+1) ]  # (value, weight)
    for v, w in items:
        for weight in range(W, w-1, -1):
            prev_v, prev_w = dp[weight - w]
            new_v = prev_v + v
            new_w = prev_w + w
            curr_v, curr_w = dp[weight]
            if new_v > curr_v:
                dp[weight] = (new_v, new_w)
            elif new_v == curr_v and new_w < curr_w:
                dp[weight] = (new_v, new_w)
    # Find max value and min weight
    max_value = 0
    min_weight = 0
    for weight in range(W+1):
        val, wei = dp[weight]
        if val > max_value:
            max_value = val
            min_weight = wei
        elif val == max_value and wei < min_weight:
            min_weight = wei

    print(f"Case {case_number}:")
    print(max_value)
    print(min_weight)
    case_number += 1