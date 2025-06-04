import sys
input = sys.stdin.readline

MOD = 10**9 + 7
N = int(input())

dp = [0] * (N+10)
dp_cum = [0] * (N+10)

dp[1] = N-1
dp_cum[1] = N-1
dp[2] = N-1
dp_cum[2] = 2*(N-1)

n = 3
while n <= N:
    dp[n] = dp[n-1] + dp_cum[n-3]
    dp_cum[n] = (dp_cum[n-1] + dp[n]) % MOD
    n += 1

i = 1
s = 0
while i < N:
    s += dp[i]
    i += 1

answer = (s*N + dp[N] + 1) % MOD
print(answer)