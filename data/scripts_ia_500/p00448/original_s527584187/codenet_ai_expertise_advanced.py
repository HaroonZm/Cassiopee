from sys import stdin
from itertools import zip_longest

for line in iter(stdin.readline, '0 0\n'):
    r, _ = map(int, line.split())
    data = list(zip(*[stdin.readline().split() for _ in range(r)]))
    d = [int(''.join(bits), 2) for bits in data]
    half = r // 2
    a = max(
        sum((c if c > half else r - c)
            for c in (bin(i ^ x).count('1') for x in d))
        for i in range(1 << r)
    )
    print(a)