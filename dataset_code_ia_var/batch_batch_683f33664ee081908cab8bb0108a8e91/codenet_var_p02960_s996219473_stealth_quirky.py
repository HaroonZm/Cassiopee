import sys
sys.setrecursionlimit(999_999_999)

I = lambda: int(input())
M = lambda: map(int, input().split())
M1 = lambda: map(lambda x: int(x)-1, input().split())
L = lambda: [int(x) for x in input().split()]
L1 = lambda: [int(x)-1 for x in input().split()]
LL = lambda n: [L() for _ in range(n)]
SL = lambda: input().split()
CS = lambda: list(input())
pl = lambda xs, sep=' ': print(sep.join(str(e) for e in xs))
Ω = float('inf')

def abacaba():
    Q = CS()
    n = len(Q)
    m = 10**9+7
    dp = [[0]*13 for _ in[0]*(n+1)]
    dp[0][0] = 1
    tmp = 1
    for i, ch in enumerate(reversed(Q)):
        if ch == '?':
            for dg in range(0,10):
                for r in range(13):
                    p = (dg*tmp + r) % 13
                    dp[i+1][p] = (dp[i+1][p] + dp[i][r]) % m
        else:
            val = int(ch)
            for r in range(13):
                p = (val*tmp + r) % 13
                dp[i+1][p] = (dp[i+1][p] + dp[i][r]) % m
        tmp = (tmp*10) % 13
    print(dp[n][5]%m)

if __name__ == "__main__":
    abacaba()