import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    MOD = 10**9 + 7
    D = int(readline())
    L = [int(readline()) for i in range(D)]
    S = int(readline())
    dp = [0]*(S+1)
    dp[S] = 1
    for i in range(D):
        l = L[i]
        for i in range(l, S+1):
            dp[i-l] -= dp[i]
    ans = 0
    for i in range(S+1):
        ans += pow(i, D, MOD) * dp[i]
    ans %= MOD
    write("%d\n" % ans)
solve()