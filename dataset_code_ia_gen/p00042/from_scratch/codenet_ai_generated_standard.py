case_num = 1
while True:
    W = int(input())
    if W == 0:
        break
    N = int(input())
    items = []
    for _ in range(N):
        v, w = input().split(',')
        items.append((int(v), int(w)))
    dp = [(-1, 0)] * (W + 1)  # (value, weight)
    dp[0] = (0, 0)
    for v, w in items:
        ndp = dp[:]
        for weight in range(W - w + 1):
            if dp[weight][0] >= 0:
                nv = dp[weight][0] + v
                nw = dp[weight][1] + w
                if ndp[nw][0] < nv or (ndp[nw][0] == nv and ndp[nw][1] > nw):
                    ndp[nw] = (nv, nw)
        dp = ndp
    max_value = -1
    min_weight = 0
    for value, weight in dp:
        if value > max_value or (value == max_value and weight < min_weight):
            max_value = value
            min_weight = weight
    print(f"Case {case_num}:\n{max_value}\n{min_weight}")
    case_num += 1