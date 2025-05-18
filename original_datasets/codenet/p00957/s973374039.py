import sys
input = sys.stdin.readline

def main():
    l, k = map(int, input().split())

    dp = [[0] * 2 for i in range(101)]
    dp[0][1] = 1
    ans = 0
    for i in range(1, l+1):
        dp[i][0] = dp[i-1][1]
        if i-k >= 0:
            dp[i][0] += dp[i-k][1]
        dp[i][1] = dp[i-1][0]
        ans += dp[i][0]
    print(ans)

if __name__ == "__main__":
    main()