from math import sqrt
from heapq import heappush, heappop

def get_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    xs, ys, xt, yt = map(int, input().split())
    n = int(input())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    
    max_num = 10 ** 18
    # Create distance table
    size = n + 2
    dist = []
    for i in range(size):
        dist.append([0] * size)
    
    dist[n][n+1] = get_distance(xs, ys, xt, yt)
    dist[n+1][n] = dist[n][n+1]

    for i in range(n):
        x, y, r = circles[i]
        dist[n][i] = max(0.0, get_distance(xs, ys, x, y) - r)
        dist[i][n] = dist[n][i]
        dist[n+1][i] = max(0.0, get_distance(xt, yt, x, y) - r)
        dist[i][n+1] = dist[n+1][i]
        for j in range(i + 1, n):
            xx, yy, rr = circles[j]
            d = max(0.0, get_distance(x, y, xx, yy) - r - rr)
            dist[i][j] = d
            dist[j][i] = d

    cost = [max_num] * size
    q = []
    heappush(q, (0.0, n))

    while len(q) > 0:
        d, p = heappop(q)
        if cost[p] <= d:
            continue
        cost[p] = d
        for v in range(size):
            if v == p:
                continue
            new_dist = d + dist[p][v]
            if new_dist < cost[v]:
                heappush(q, (new_dist, v))
    print(cost[n+1])

main()