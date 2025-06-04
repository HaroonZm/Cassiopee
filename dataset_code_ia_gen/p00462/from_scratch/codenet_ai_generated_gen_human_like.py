import sys
import bisect

input = sys.stdin.readline

while True:
    d = int(input())
    if d == 0:
        break
    n = int(input())
    m = int(input())
    shops = [0]
    for _ in range(n - 1):
        pos = int(input())
        shops.append(pos)
    shops.sort()
    res = 0
    for _ in range(m):
        k = int(input())
        i = bisect.bisect_left(shops, k)
        candidates = []
        if i < n:
            dist = abs(shops[i] - k)
            dist = min(dist, d - dist)
            candidates.append(dist)
        if i > 0:
            dist = abs(shops[i - 1] - k)
            dist = min(dist, d - dist)
            candidates.append(dist)
        res += min(candidates)
    print(res)