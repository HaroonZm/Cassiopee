import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

w = 0
e = 0

for i in range(1, len(s)):
    if s[i] == 'E':
        e += 1

min_count = e

for i in range(1, len(s)):
    if s[i - 1] == 'W':
        w += 1
    if s[i] == 'E':
        e -= 1
    count = w + e
    if count < min_count:
        min_count = count

print(min_count)