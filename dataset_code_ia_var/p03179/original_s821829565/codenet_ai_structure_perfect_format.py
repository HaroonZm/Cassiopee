import sys
input = sys.stdin.readline

def f2(N, s):
    MOD = int(1e9 + 7)
    dp = [1] * N
    for i in range(1, N):
        csum = list(dp)
        for j in range(1, N - i + 1):
            csum[j] += csum[j - 1]
            csum[j] %= MOD
        csum_ = csum[N - i]
        i_ = i - 1
        for j in range(N - i):
            if s[i_] == ">":
                dp[j] = csum[j]
            else:
                dp[j] = (csum_ - csum[j] + MOD) % MOD
    return dp[0]

N = int(input())
s = input().rstrip()
print(f2(N, s))