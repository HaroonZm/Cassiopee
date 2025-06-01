from itertools import count

lst = [1] * 50021
lst[0] = 0
for i in range(2, 50021):
    if lst[i - 1]:
        for k in range(i - 1 + i, 50021, i):
            lst[k] = 0

from sys import stdin

for line in stdin:
    n = int(line)
    left = lst[:n - 1]
    right = lst[n:]
    print(n - 1 - next(i for i, v in enumerate(reversed(left)) if v),
          n + 1 + next(i for i, v in enumerate(right) if v))