from sys import stdin
from itertools import accumulate

N = int(stdin.readline())
P = sorted(map(lambda s: tuple(map(int, s.split())), (stdin.readline() for _ in range(N))))

su, S, ans = 0, float('-inf'), float('-inf')
for a, b in P:
    S = min(S, su - a)
    ans = max(ans, su + b - a - S)
    su += b
print(ans)