from itertools import count
from sys import stdin

for line in stdin:
    n = int(line)
    if n == 0:
        break
    s = list(map(int, next(stdin).split()))
    for steps in count():
        next_s = [s.count(x) for x in s]
        if s == next_s:
            print(steps)
            print(*s)
            break
        s = next_s