from sys import stdin
from itertools import islice

for e in iter(stdin.readline, '0\n'):
    n = int(e)
    a = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    s, t = min(a)
    m = max(map(lambda p: p[0], b := {tuple(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))})) - max(map(lambda p: p[0], a)) + s
    for x, y in b:
        if x <= m and all((x + u - s, y + v - t) in b for u, v in a):
            print(x - s, y - t)
            break