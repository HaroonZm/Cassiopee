import sys
from itertools import islice, tee

def fib_mod(n, mod=1001):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
        yield a

def count_diff_ge(sequence, d):
    a, b = tee(sequence)
    next(b, None)
    return 1 + sum(1 for x, y in zip(a, b) if y - x >= d)

for line in sys.stdin:
    v, d = map(int, line.split())
    sorted_fib = sorted(islice(fib_mod(v), v))
    print(count_diff_ge(sorted_fib, d))