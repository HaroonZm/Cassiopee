import sys
s = sys.stdin.readline().strip()
n = len(s)
if n == 2:
    print(int(s[1])-int(s[0]))
    exit()

min_diff = float('inf')
max_len = 9
min_len = 1

for length in range(min_len, max_len+1):
    values = []
    idx = 0
    while idx < n:
        l = min(length, n - idx)
        values.append(int(s[idx:idx+l]))
        idx += l
    if len(values) > 1:
        diff = max(values) - min(values)
        if diff < min_diff:
            min_diff = diff

print(min_diff)