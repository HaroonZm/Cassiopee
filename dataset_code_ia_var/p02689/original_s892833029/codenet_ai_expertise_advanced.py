from sys import stdin
from operator import itemgetter

n, m = map(int, stdin.readline().split())
hs = list(map(int, stdin.readline().split()))
ans = [1] * n

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    a -= 1; b -= 1
    if hs[a] == hs[b]:
        ans[a] = ans[b] = 0
    elif hs[a] < hs[b]:
        ans[a] = 0
    else:
        ans[b] = 0

print(sum(ans))