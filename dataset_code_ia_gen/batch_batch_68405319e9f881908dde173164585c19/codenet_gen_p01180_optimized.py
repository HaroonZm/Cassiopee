import sys
import math
input = sys.stdin.readline

def dist(c1, c2):
    dx = c1[1] - c2[1]
    dy = c1[2] - c2[2]
    center_dist = math.sqrt(dx*dx + dy*dy)
    return max(0.0, center_dist - c1[0] - c2[0])

def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        d = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                d = min(d, dist(px[i], px[j]))
        return d
    mid = n // 2
    midx = px[mid][1]
    d1 = closest_pair(px[:mid], [p for p in py if p[1] <= midx])
    d2 = closest_pair(px[mid:], [p for p in py if p[1] > midx])
    d = min(d1, d2)
    strip = [p for p in py if abs(p[1] - midx) < d + p[0]]
    m = len(strip)
    for i in range(m):
        r1, x1, y1 = strip[i]
        for j in range(i+1, m):
            r2, x2, y2 = strip[j]
            if y2 - y1 > d + r1 + r2:
                break
            d = min(d, dist(strip[i], strip[j]))
    return d

while True:
    N = int(input())
    if N == 0:
        break
    circles = [tuple(map(float, input().split())) for _ in range(N)]
    # Sort by x coordinate
    px = sorted(circles, key=lambda c: c[1])
    py = sorted(circles, key=lambda c: c[2])
    ans = closest_pair(px, py)
    print(f"{ans:.6f}")