import bisect

n = int(input())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

dp = [a[0]]

for i in range(1, n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect.bisect_left(dp, a[i])
        dp[idx] = a[i]

print(len(dp))