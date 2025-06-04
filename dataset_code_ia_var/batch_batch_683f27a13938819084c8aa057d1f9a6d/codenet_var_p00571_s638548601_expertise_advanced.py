import sys
from itertools import accumulate

sys.setrecursionlimit(2 * 10**9)
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data = [(0, 0)] + sorted(data)
s = list(accumulate(val for _, val in data))

mn = float('inf')
ans = 0
for i in range(1, n + 1):
    diff = s[i-1] - data[i][0]
    if diff < mn:
        mn = diff
    current = s[i] - data[i][0] - mn
    if current > ans:
        ans = current
print(ans)