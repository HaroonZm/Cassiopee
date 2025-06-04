MOD = 10**9 + 7
N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
if K - N == 1:
    print(1)
    exit()
ans = 1
left = 0
right = 0
i = 1
while i < K:
    left += i
    i += 1
i = N - K + 1
while i <= N:
    right += i
    i += 1
ans += right - left + 1
ans %= MOD
i = K + 1
while i <= N:
    left += i - 1
    right += N - (i - 1)
    ans += right - left + 1
    ans %= MOD
    i += 1
print(ans)