n = int(input())
p = list(map(int, input().split()))

from bisect import bisect_left

p.sort()
max_p = p[-1]

for i in range(max_p, -1, -1):
    idx = bisect_left(p, i)
    if len(p) - idx >= i:
        print(i)
        break