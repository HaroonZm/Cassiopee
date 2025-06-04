import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    INF = -10**15

    # dp[i][0]: max sum for even items ending at i
    # dp[i][1]: max sum for odd items ending at i
    dp = []
    for i in range(N):
        dp.append([INF, INF])

    # First position
    dp[0][1] = a[0]
    dp[0][0] = 0

    if N > 1:
        # Second position
        dp[1][0] = 0
        if a[0] < a[1]:
            dp[1][1] = a[1]
        else:
            dp[1][1] = a[0]

    # Fill dp array
    for i in range(2, N):
        if i % 2 == 1:
            dp[i][0] = dp[i-1][0]
            if dp[i][0] < dp[i-2][0] + a[i]:
                dp[i][0] = dp[i-2][0] + a[i]
            dp[i][1] = dp[i-1][1]
            if dp[i][1] < dp[i-1][0] + a[i]:
                dp[i][1] = dp[i-1][0] + a[i]
            if dp[i][1] < dp[i-2][1] + a[i]:
                dp[i][1] = dp[i-2][1] + a[i]
        else:
            dp[i][0] = dp[i-1][1]
            if dp[i][0] < dp[i-1][0] + a[i]:
                dp[i][0] = dp[i-1][0] + a[i]
            if dp[i][0] < dp[i-2][0] + a[i]:
                dp[i][0] = dp[i-2][0] + a[i]
            dp[i][1] = dp[i-2][1] + a[i]
            if dp[i][1] < dp[i-1][1] + a[i]:
                dp[i][1] = dp[i-1][1] + a[i]
    
    if N % 2 == 0:
        print(dp[N-1][1])
    else:
        print(dp[N-1][0])

if __name__ == "__main__":
    main()