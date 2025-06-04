import sys

s = [list(map(int, e.split(','))) for e in sys.stdin]

for i in range(1, len(s)):
    k = len(s[i])
    b = k > len(s[i - 1])
    for j in range(k):
        t = j - b
        s[i][j] += max(s[i - 1][t * (j > 0): t + 2])

print(*s[-1])