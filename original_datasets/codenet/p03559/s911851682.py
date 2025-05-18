import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left
from itertools import accumulate

n = int(readline())
a = sorted(list(map(int, readline().split())))
b = sorted(list(map(int, readline().split())))
c = sorted(list(map(int, readline().split())))
check = [0] * n
ans = 0
for i in range(n):
    index = bisect_left(c, b[i])
    if index != n:
        if c[index] == b[i]:
            index = bisect_left(c, b[i] + 1)
    check[i] = n - index
cumsum = [0] + list(accumulate(check[::-1]))
for aa in a:
    index = bisect_left(b, aa)
    if index != n:
        if b[index] == aa:
            index = bisect_left(b, aa + 1)
    ans += cumsum[n - index]
print(ans)