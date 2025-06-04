n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
asum = [0] * (n + 1)
aplussum = [0] * (n + 1)
i = 0
while i < n:
    asum[i + 1] = asum[i] + a[i]
    aplussum[i + 1] = aplussum[i] + (a[i] if a[i] > 0 else 0)
    i += 1
l = 1
r = k
ans = 0
while r <= n:
    lr = aplussum[n] - aplussum[r] + aplussum[l - 1]
    mid = asum[r] - asum[l - 1]
    if mid < 0:
        mid = 0
    total = lr + mid
    if total > ans:
        ans = total
    l += 1
    r += 1
print(ans)