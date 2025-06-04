import sys
from itertools import cycle

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().strip()) for _ in range(n)]

e = [sum((3 * (cell == 'o') + 1 * (cell == '-')) / n for cell in row) for row in a]

idx = max(range(n), key=e.__getitem__)

ls = [i + 1 for i, row in enumerate(a) if row[idx] == 'o'] or [idx + 1]

cycler = cycle(ls)
for _ in range(1000):
    print(next(cycler))
    sys.stdin.readline()