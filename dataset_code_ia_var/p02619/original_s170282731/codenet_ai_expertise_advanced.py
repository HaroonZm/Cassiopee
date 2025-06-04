from sys import stdin
from itertools import repeat

d = int(stdin.readline())
c = list(map(int, stdin.readline().split()))
s = [list(map(int, stdin.readline().split())) for _ in repeat(None, d)]
sat = 0
last = [0] * 26

for i, t in enumerate(map(int, (stdin.readline() for _ in range(d)))):
    t -= 1
    sat += s[i][t]
    last[t] = i + 1
    sat -= sum(c[j] * (i + 1 - last[j]) for j in range(26))
    print(sat)