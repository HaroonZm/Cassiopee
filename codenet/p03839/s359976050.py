n, k = map(int, input().split())
a = list(map(int, input().split()))
asum = [0 for _ in range(n+1)]
psum = [0 for _ in range(n+1)]
for i in range(n):
    asum[i+1] = asum[i] + a[i]
    psum[i+1] = psum[i] + max(0, a[i])
ans = 0
for i in range(n-k+1):
    ans = max(ans, psum[i]-psum[0]+asum[i+k]-asum[i]+psum[n]-psum[i+k])
    ans = max(ans, psum[i]-psum[0]+psum[n]-psum[i+k])
print(ans)