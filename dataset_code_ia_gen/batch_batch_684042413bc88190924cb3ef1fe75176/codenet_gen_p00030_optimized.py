import sys
from math import comb

def count_combinations(n, s):
    if s > 45 or s < 0 or n > 10 or n < 1:
        return 0
    result = 0
    # Inclusion-exclusion principle
    for k in range((s // 10) + 1):
        sign = -1 if k % 2 else 1
        c1 = comb(10, n - k)
        c2 = comb(n - k, k) if k <= n else 0  # This is actually k choose k which is 1, but safer to keep
        c3 = comb(s - 10 * k + n - 1, n - 1) if s - 10 * k >= 0 else 0
        if n - k < 0 or s - 10 * k < 0:
            continue
        result += sign * comb(10, k) * comb(10 - k, n - k) * comb(s - 10*k + n -1, n -1) if s - 10*k >= 0 else 0

    # But above is complicated, the problem is classic combination "subset of digits n summing to s"
    # The best optimized solution is bitmask dp or precalc with DP

def main():
    input = sys.stdin.readline
    max_n, max_s = 9, 100
    # dp[n][s]: number of ways to choose n distinct digits 0..9 sum s
    dp = [[0]*(max_s+1) for _ in range(max_n+1)]
    dp[0][0] = 1
    for digit in range(10):
        for n in range(max_n-1, -1, -1):
            for s in range(max_s-digit+1):
                dp[n+1][s+digit] += dp[n][s]

    for line in sys.stdin:
        if line.strip() == '':
            continue
        n,s = map(int,line.split())
        if n == 0 and s == 0:
            break
        if n > 9 or s > 45:
            print(0)
            continue
        print(dp[n][s])

if __name__ == '__main__':
    main()