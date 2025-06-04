import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dist_sq(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        min_d = 10**18
        for i in range(n):
            for j in range(i+1, n):
                d = dist_sq(px[i], px[j])
                if d < min_d:
                    min_d = d
        return min_d
    mid = n // 2
    midx = px[mid][0]
    left_px = px[:mid]
    right_px = px[mid:]
    left_py, right_py = [], []
    for p in py:
        if p[0] <= midx:
            left_py.append(p)
        else:
            right_py.append(p)
    dl = closest_pair(left_px, left_py)
    dr = closest_pair(right_px, right_py)
    d = min(dl, dr)
    strip = [p for p in py if abs(p[0]-midx)**2 < d]
    m = len(strip)
    for i in range(m):
        for j in range(i+1, min(i+7, m)):
            dy = strip[j][1] - strip[i][1]
            if dy*dy >= d:
                break
            d = min(d, dist_sq(strip[i], strip[j]))
    return d

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
px = sorted(points, key=lambda x: x[0])
py = sorted(points, key=lambda x: x[1])
print(closest_pair(px, py))