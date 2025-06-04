def main():
    import sys
    max_sum = 36  # max sum with digits 0..9 * 4 = 36
    dp = [[0]* (max_sum+1) for _ in range(5)]
    dp[0][0] = 1
    for i in range(1,5):
        for s in range(max_sum+1):
            for digit in range(10):
                if s - digit >= 0:
                    dp[i][s] += dp[i-1][s - digit]
    for line in sys.stdin:
        n = int(line.strip())
        print(dp[4][n] if n <= max_sum else 0)
if __name__ == "__main__":
    main()