n, k = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]

asum = [0] * (n + 1)
aplussum = [0] * (n + 1)
for i in range(0, n):
    asum[i+1] += asum[i] + a[i]
    aplussum[i+1] += aplussum[i] + max(a[i], 0)

l = 1; r = k
ans = 0
while r <= n:
    lr = aplussum[n] - aplussum[r] + aplussum[l-1]
    mid = max(asum[r] - asum[l-1], 0)
    ans = max(ans, lr + mid)
    l += 1; r += 1 
print(ans)