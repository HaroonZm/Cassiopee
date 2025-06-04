n, k = map(int, input().split())
a = list(map(int, input().split()))
asum = [0] * (n + 1)
psum = [0] * (n + 1)
i = 0
while i < n:
    asum[i + 1] = asum[i] + a[i]
    psum[i + 1] = psum[i] + (a[i] if a[i] > 0 else 0)
    i += 1
ans = 0
i = 0
while i <= n - k:
    val1 = psum[i] + asum[i + k] - asum[i] + psum[n] - psum[i + k]
    val2 = psum[i] + psum[n] - psum[i + k]
    if val1 > ans:
        ans = val1
    if val2 > ans:
        ans = val2
    i += 1
print(ans)