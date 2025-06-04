N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
MOD = 10 ** 9 + 7
low = 0
high = 0
ans = 0
i = 1
while i < N + 2:
    low += i - 1
    high += N - i + 1
    if i >= K:
        ans += (high - low + 1)
        ans %= MOD
    i += 1
print(ans)