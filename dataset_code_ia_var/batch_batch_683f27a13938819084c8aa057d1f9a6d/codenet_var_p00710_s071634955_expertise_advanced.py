from sys import stdin
from itertools import islice, count

def solve():
    lines = iter(stdin)
    for line in lines:
        n, r = map(int, line.split())
        if n == 0 and r == 0:
            return
        ops = [tuple(map(int, next(lines).split())) for _ in range(r)]
        d = list(range(n, 0, -1))
        for p, c in ops:
            # Use slices and unpacking for advanced manipulation
            p -= 1
            d = [*islice(d, p, p + c), *islice(d, 0, p), *islice(d, p + c, None)]
        print(d[0])

solve()