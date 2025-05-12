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
        for j in range(N - i):  # N-(i+1)+1 = N-i
            dp[j] = csum[j] if s[i_] == ">" else \
                (csum_ - csum[j] + MOD) % MOD
    return(dp[0])

N = int(input()) # 2 <= N <= 30000
s = input().rstrip() # len(s) = N - 1
print(f2(N, s))