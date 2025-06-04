from sys import stdin
from itertools import count, islice

def walk(n):
    p = 1 + 0j
    for _ in islice(count(), n-1):
        d = p * 1j / abs(p * 1j)
        p += d
    return p

for line in stdin:
    n = int(line)
    if n == -1:
        break
    p = walk(n)
    print(f"{p.real:.2f}\n{p.imag:.2f}")