N, K = map(int, input().split())
MOD = 10 ** 9 + 7

low, high = 0, 0
ans = 0
for i in range(1, N + 2):
    low += i - 1
    high += N - i + 1

    if i >= K:
        ans += (high - low + 1)
        ans %= MOD

print(ans)