import sys
import bisect

input = sys.stdin.readline

while True:
    d = int(input())
    if d == 0:
        break
    n = int(input())
    m = int(input())
    stores = [0] + [int(input()) for _ in range(n - 1)]
    stores.sort()
    result = 0
    for _ in range(m):
        k = int(input())
        pos = bisect.bisect_left(stores, k)
        candidates = []
        if pos == n:
            candidates.append(stores[-1])
            candidates.append(stores[0])
        elif pos == 0:
            candidates.append(stores[0])
            candidates.append(stores[-1])
        else:
            candidates.append(stores[pos])
            candidates.append(stores[pos - 1])
        dist = min(min((c - k) % d, (k - c) % d) for c in candidates)
        result += dist
    print(result)