import sys

def expected_value(n, m, k):
    # dp[i][j] = number of ways to get sum j with i dice
    # sums range from i to i*m
    max_sum = n * m
    dp_prev = [0] * (max_sum + 1)
    dp_prev[0] = 1  # base case, zero dice sum zero ways considered 1 to start transitions

    for _ in range(n):
        dp_curr = [0] * (max_sum + 1)
        for s in range(max_sum + 1):
            if dp_prev[s] == 0:
                continue
            for face in range(1, m + 1):
                if s + face <= max_sum:
                    dp_curr[s + face] += dp_prev[s]
        dp_prev = dp_curr

    total_ways = m ** n
    expected = 0.0
    for s in range(n, max_sum + 1):
        count = dp_prev[s]
        val = max(1, s - k)
        expected += count * val

    return expected / total_ways

for line in sys.stdin:
    n,m,k = map(int, line.split())
    if n == 0 and m == 0 and k == 0:
        break
    ans = expected_value(n, m, k)
    print(f"{ans:.8f}")