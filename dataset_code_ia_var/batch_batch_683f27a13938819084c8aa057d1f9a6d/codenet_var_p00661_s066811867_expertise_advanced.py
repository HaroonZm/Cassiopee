from sys import stdin
from itertools import islice

def process():
    lines = iter(stdin)
    for line in lines:
        n, m = map(int, line.split())
        if n == 0:
            break
        prices = map(int, next(lines).split())
        print(float(n) / 2 if min(prices) > 1 else 0.0)

process()