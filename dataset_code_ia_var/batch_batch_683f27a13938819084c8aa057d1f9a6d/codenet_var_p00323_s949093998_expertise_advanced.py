from sys import stdin
from itertools import count

n = int(stdin.readline())
s = sum(1 << (a + b) for a, b in (map(int, stdin.readline().split()) for _ in range(n)))
for idx in (i for i in count() if (s >> i) & 1 and (s >> i) > 0):
    print(idx, 0)
    if s < (1 << (idx + 1)):
        break