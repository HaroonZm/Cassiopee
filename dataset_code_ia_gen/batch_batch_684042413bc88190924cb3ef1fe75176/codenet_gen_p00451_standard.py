import sys
def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    max_len = 0
    for i in range(1, m + 1):
        new_dp = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                new_dp[j] = dp[j-1] + 1
                if new_dp[j] > max_len:
                    max_len = new_dp[j]
        dp = new_dp
    return max_len

lines = sys.stdin.read().strip().split('\n')
for i in range(0, len(lines), 2):
    print(longest_common_substring(lines[i], lines[i+1]))