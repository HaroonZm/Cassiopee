import sys

sys.setrecursionlimit(10**7)

def partitions(n, max_part):
    if n == 0:
        yield []
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    for p in partitions(n, n):
        print(*p)