def main():
    import sys
    MAX_N = 30
    dp = [0]*(MAX_N+1)
    dp[0] = 1
    for i in range(1, MAX_N+1):
        dp[i] = dp[i-1]
        if i-2 >= 0: dp[i] += dp[i-2]
        if i-3 >= 0: dp[i] += dp[i-3]

    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        ways = dp[n]
        days = (ways + 9) // 10  # 10 kinds per day
        years = (days + 364) // 365  # ceil division for years
        print(years)

if __name__ == "__main__":
    main()