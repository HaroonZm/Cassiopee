import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dist_sq(p1, p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    return dx*dx + dy*dy

def closest_pair(px, py):
    n = len(px)
    if n <= 3:
        res = 10**20
        for i in range(n):
            for j in range(i+1, n):
                res = min(res, dist_sq(px[i], px[j]))
        return res
    mid = n // 2
    midx = px[mid][0]
    dl = closest_pair(px[:mid], [p for p in py if p[0]<midx])
    dr = closest_pair(px[mid:], [p for p in py if p[0]>=midx])
    d = min(dl, dr)

    strip = [p for p in py if abs(p[0]-midx) < d**0.5]
    m = len(strip)
    for i in range(m):
        for j in range(i+1, m):
            if (strip[j][1] - strip[i][1])**2 >= d:
                break
            d = min(d, dist_sq(strip[i], strip[j]))
    return d

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points_x_sorted = sorted(points, key=lambda x: x[0])
points_y_sorted = sorted(points, key=lambda x: x[1])

print(closest_pair(points_x_sorted, points_y_sorted))