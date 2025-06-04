N, W = map(int, input().split())
WV = []
for i in range(N):
    w, v = map(int, input().split())
    WV.append([w, v])

dp = {}
dp[0] = 0

for item in WV:
    w = item[0]
    v = item[1]
    items = list(dp.items())
    for nw, nv in items:
        new_w = nw + w
        new_v = nv + v
        if new_w <= W:
            if new_w in dp:
                if dp[new_w] < new_v:
                    dp[new_w] = new_v
            else:
                dp[new_w] = new_v

max_value = 0
for value in dp.values():
    if value > max_value:
        max_value = value

print(max_value)