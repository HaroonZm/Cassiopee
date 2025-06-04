import sys

def longest_common_substring(s, t):
    m, n = len(s), len(t)
    prev = [0] * (n + 1)
    max_len = 0
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_len:
                    max_len = curr[j]
        prev = curr
    return max_len

lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 2):
    if i + 1 >= len(lines):
        break
    s1, s2 = lines[i], lines[i+1]
    print(longest_common_substring(s1, s2))