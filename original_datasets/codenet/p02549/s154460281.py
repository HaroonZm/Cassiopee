import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    mod = 998244353

    dp = [0]*(n)

    zone = [tuple(map(int, input().split())) for i in range(k)]
    zone.sort()

    dp[0] = 1
    count = 0
    bit = [0]*k

    for i in range(1, n):
        for j in range(k):
            l, r = zone[j]
            if i-l >= 0:
                bit[j] += dp[i-l]
            if i-r-1 >= 0:
                bit[j] -= dp[i-r-1]
        dp[i] += sum(bit)%mod
        dp[i] %= mod
    ans = dp[n-1]
    print(ans)

if __name__ == "__main__":
    main()