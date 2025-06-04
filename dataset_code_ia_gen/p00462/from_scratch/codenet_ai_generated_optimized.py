import sys
import bisect

input = sys.stdin.readline

while True:
    d = int(input())
    if d == 0:
        break
    n = int(input())
    m = int(input())
    positions = [0] + [int(input()) for _ in range(n - 1)]
    positions.sort()

    total = 0
    for _ in range(m):
        k = int(input())
        idx = bisect.bisect_left(positions, k)
        candidates = []
        if idx < n:
            dist = abs(positions[idx] - k)
            dist = min(dist, d - dist)
            candidates.append(dist)
        if idx > 0:
            dist = abs(positions[idx - 1] - k)
            dist = min(dist, d - dist)
            candidates.append(dist)
        total += min(candidates)
    print(total)