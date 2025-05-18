MOD = 10**9 + 7
N, K = map(int, input().split())
if K - N == 1:
    print(1)
    exit()
ans = 1
left = 0
right = 0
for i in range(1,K):
    left += i
for i in range(N-K+1,N+1):
    right += i
ans += right - left + 1
ans %= MOD
for i in range(K+1,N+1):
    left += i - 1
    right += N - (i-1)
    ans += right - left + 1
    ans %= MOD
print(ans)