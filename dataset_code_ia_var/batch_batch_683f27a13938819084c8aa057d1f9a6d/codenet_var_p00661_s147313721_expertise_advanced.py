from sys import stdin
from itertools import islice

def lines():
    return map(str.strip, stdin)

l_iter = iter(lines())
while True:
    n, m = map(int, next(l_iter).split())
    if n == 0:
        break
    p = sorted(map(int, next(l_iter).split()))
    print(f'{n/2:.10f}' if p[0] != 1 else f'{0:.10f}')