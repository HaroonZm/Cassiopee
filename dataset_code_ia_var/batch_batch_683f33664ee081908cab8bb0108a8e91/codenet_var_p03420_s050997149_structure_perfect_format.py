N, K = map(int, input().split())
ans = 0
for b in range(1, N + 1):
    ans += (N // b) * max(0, b - K) + max(0, N % b - K + 1)
if K == 0:
    ans -= N
print(ans)