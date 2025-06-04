import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = 1000001
table = list(range(N+1))
i = 2
while i <= N:
    if table[i] == i:
        j = i
        while j <= N:
            table[j] *= 1 - 1/i
            j += i
    i += 1

table[0] = 1
ans = list(accumulate(table))
T = int(sys.stdin.readline().strip())
t = 0
while t < T:
    a = int(sys.stdin.readline().strip())
    print(int(ans[a]))
    t += 1