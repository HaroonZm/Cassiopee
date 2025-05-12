N, W = map(int, input().split())
w = []
for i in range(N):
    w.append(int(input()))
w.sort()
summ = 0
ans = 0
for num, wi in enumerate(w):
    if num == N - 1:
        if sum(w) - w[-1] <= W and W - sum(w) - w[-1] < w[-1]:
            ans += 1
        break
    dp = [[0] * (W + 1) for i in range(N - num)]
    dp[0][0] = 1
    for n in range(N - num - 1):
        dpn1 = dp[n + 1]
        dpn = dp[n]
        for k in range(W + 1):
            if k - w[num + n + 1] >= 0:
                dpn1[k] = dpn[k] + dpn[k - w[num + n + 1]]
            else:
                dpn1[k] = dpn[k]
    for i in range(max(W - summ - wi + 1,0), W - summ + 1):
        ans += dp[-1][i]
        ans %= 10 ** 9 + 7
    summ += wi
    if W < summ:
        break
print(ans%(10**9+7))