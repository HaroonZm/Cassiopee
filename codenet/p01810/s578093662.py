N,K = map(int, input().split())
ans = 1
for _ in range(N-1):
    ans += (ans+K-2)//(K-1)
print(ans-1)