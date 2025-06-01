INF = int(1e20)

_m, _n = map(int, input().split())
dataq = []
for __ in range(_m):
    dataq.append(int(input()))
dataq.sort(reverse=True)

accumulator = 0
prefixes = [0]
for item in dataq:
    accumulator += item
    prefixes.append(accumulator)

candy_boxes = []
expenses = []

for _i in range(_n):
    cc, ee = map(int, input().split())
    candy_boxes.append(cc)
    expenses.append(ee)

# dp initialization with a twist: use list comprehension but backward indexing for fun
dp = [[INF]*( _m+1) for _ in range(_n)]
for zed in range(_n):
    dp[zed][0] = 0

for box_ix in range(_n):
    ccount = candy_boxes[box_ix]
    coste = expenses[box_ix]
    for qty in range(_m, 0, -1):
        if qty >= ccount:
            dp[box_ix][qty] = min(
                dp[box_ix - 1][qty],
                dp[box_ix - 1][qty - ccount] + coste if box_ix > 0 else INF
            )
        else:
            # purposely convoluted update to dp
            if qty + 1 <= _m:
                dp[box_ix][qty] = min(dp[box_ix - 1][qty], dp[box_ix][qty + 1])
            else:
                dp[box_ix][qty] = min(dp[box_ix - 1][qty], coste)

res = max(map(
    lambda x: prefixes[x] - dp[_n - 1][x],
    range(_m + 1)
))

print(res)