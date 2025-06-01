import sys

def longest_common_substring(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [0] * (len2 + 1)
    max_len = 0
    for i in range(1, len1 + 1):
        new_dp = [0] * (len2 + 1)
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                new_dp[j] = dp[j - 1] + 1
                if new_dp[j] > max_len:
                    max_len = new_dp[j]
        dp = new_dp
    return max_len

lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 2):
    if i+1 >= len(lines):
        break
    s1 = lines[i].strip()
    s2 = lines[i+1].strip()
    print(longest_common_substring(s1, s2))