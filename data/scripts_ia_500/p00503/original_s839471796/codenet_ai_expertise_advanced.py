from sys import stdin
from bisect import bisect_left
from collections import defaultdict

input = stdin.readline

n, k = map(int, input().split())
coords = [tuple(map(int, input().split())) for _ in range(n)]

xs = sorted({x for p in coords for x in (p[0], p[3])})
ys = sorted({y for p in coords for y in (p[1], p[4])})
ds = sorted({d for p in coords for d in (p[2], p[5])})

xi = {v: i for i, v in enumerate(xs)}
yi = {v: i for i, v in enumerate(ys)}
di = {v: i for i, v in enumerate(ds)}

# Using a 3D difference array for efficient updates
diff = [[[0]*(len(ds)+1) for _ in range(len(ys)+1)] for __ in range(len(xs)+1)]

for x1,y1,d1,x2,y2,d2 in coords:
    diff[xi[x1]][yi[y1]][di[d1]] += 1
    diff[xi[x2]][yi[y1]][di[d1]] -= 1
    diff[xi[x1]][yi[y2]][di[d1]] -= 1
    diff[xi[x1]][yi[y1]][di[d2]] -= 1
    diff[xi[x2]][yi[y2]][di[d1]] += 1
    diff[xi[x2]][yi[y1]][di[d2]] += 1
    diff[xi[x1]][yi[y2]][di[d2]] += 1
    diff[xi[x2]][yi[y2]][di[d2]] -= 1

# Compute prefix sums over x, y, d
for x in range(len(xs)):
    for y in range(len(ys)):
        for d in range(len(ds)):
            diff[x+1][y][d] += diff[x][y][d]
for x in range(len(xs)+1):
    for y in range(len(ys)):
        for d in range(len(ds)):
            diff[x][y+1][d] += diff[x][y][d]
for x in range(len(xs)+1):
    for y in range(len(ys)+1):
        for d in range(len(ds)):
            diff[x][y][d+1] += diff[x][y][d]

ans = 0
for x in range(len(xs)-1):
    dx = xs[x+1] - xs[x]
    for y in range(len(ys)-1):
        dy = ys[y+1] - ys[y]
        for d in range(len(ds)-1):
            if diff[x][y][d] >= k:
                dz = ds[d+1] - ds[d]
                ans += dx * dy * dz

print(ans)