def main():
    import sys
    max_sum = 36  # max sum of 4 digits each ≤ 9
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    for _ in range(4):
        ndp = [0] * (max_sum + 1)
        for s in range(max_sum + 1):
            if dp[s]:
                for digit in range(10):
                    if s + digit <= max_sum:
                        ndp[s + digit] += dp[s]
        dp = ndp
    for line in sys.stdin:
        n = int(line)
        print(dp[n] if n <= max_sum else 0)
if __name__ == '__main__':
    main()