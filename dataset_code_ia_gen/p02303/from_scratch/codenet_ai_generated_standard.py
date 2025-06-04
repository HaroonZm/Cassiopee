import sys
import math

def dist(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        return min((dist(px[i], px[j]) for i in range(n) for j in range(i+1, n)), default=float('inf'))
    mid = n // 2
    midx = px[mid][0]
    dl = closest_pair(px[:mid], py)
    dr = closest_pair(px[mid:], py)
    d = min(dl, dr)
    strip = [p for p in py if abs(p[0] - midx) < d]
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):
            d = min(d, dist(strip[i], strip[j]))
    return d

input = sys.stdin.readline
n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]
px = sorted(points, key=lambda x: x[0])
py = sorted(points, key=lambda x: x[1])
print(f"{closest_pair(px, py):.9f}")