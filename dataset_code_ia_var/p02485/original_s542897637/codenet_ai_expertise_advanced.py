from itertools import count
from sys import stdin

for line in stdin:
    try:
        n = int(line)
        if not n:
            break
        print(sum(map(int, str(abs(n)))))
    except ValueError:
        continue