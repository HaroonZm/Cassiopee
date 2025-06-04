import sys
import math
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
r, theta_deg = map(float, sys.stdin.readline().split())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Precompute distances
dist = [[0]*n for _ in range(n)]
for i in range(n):
    x1, y1 = points[i]
    for j in range(n):
        x2, y2 = points[j]
        dx = x2 - x1
        dy = y2 - y1
        dist[i][j] = math.hypot(dx, dy)

theta_rad = math.radians(theta_deg)

# To handle floating point errors
EPS = 1e-9

from functools import lru_cache

@lru_cache(None)
def dfs(last, cur, length, prev_dx, prev_dy):
    # last: index of city before cur, or -1 if no previous city before cur
    # cur: current city index
    # length: total distance traveled so far
    # prev_dx, prev_dy: direction vector of last segment (0,0 if none)
    max_carrots = 1  # since we get one carrot when arriving at cur from last
    for nxt in range(n):
        if nxt == cur:
            continue
        d = dist[cur][nxt]
        new_length = length + d
        if new_length - r > EPS:
            continue
        dx = points[nxt][0] - points[cur][0]
        dy = points[nxt][1] - points[cur][1]
        if prev_dx == 0 and prev_dy == 0:
            # no angle restriction on first move
            pass
        else:
            # compute angle between (prev_dx, prev_dy) and (dx, dy)
            dot = prev_dx*dx + prev_dy*dy
            norm_prev = math.hypot(prev_dx, prev_dy)
            norm_cur = math.hypot(dx, dy)
            cos_angle = dot / (norm_prev * norm_cur)
            # Clamp cos_angle in [-1,1] to avoid precision errors
            cos_angle = max(-1.0, min(1.0, cos_angle))
            angle = math.acos(cos_angle)
            if angle - theta_rad > EPS:
                continue
        carrots = 1 + dfs(cur, nxt, new_length, dx, dy)
        if carrots > max_carrots:
            max_carrots = carrots
    return max_carrots

print(dfs(-1, 0, 0.0, 0.0, 0.0))