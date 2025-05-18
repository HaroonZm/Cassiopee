n, k = map(int, input().split())
ans = 0
for i in range(1,n+1):
    t = 1
    while i * t < k:
        t *= 2
    ans += 1 / t
print(ans / n)