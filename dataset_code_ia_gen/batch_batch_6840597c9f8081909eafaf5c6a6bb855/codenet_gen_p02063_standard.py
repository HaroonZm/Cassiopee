A, B = map(int, input().split())
def greedy(x):
    res = 0
    for c in [B, A, 1]:
        res += x // c
        x %= c
    return res
def dp(x):
    if x == 0:
        return 0
    res = 10**15
    for c in [B, A, 1]:
        if x - c >= 0:
            res = min(res, dp(x - c) + 1)
    return res
limit = A * B
for x in range(1, limit + 1):
    if dp(x) < greedy(x):
        print(x)
        break
else:
    print(-1)