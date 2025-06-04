from sys import stdin
from itertools import islice

N = int(stdin.readline())
li = [tuple(map(int, stdin.readline().split())) for _ in range(N-1)]

for i in range(N):
    t = 0
    for c, s, f in islice(li, i, None):
        t = max(t, s)
        if t % f:
            t += f - t % f
        t += c
    print(t)