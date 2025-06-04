n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

min_dist_sq = None
for i in range(n):
    for j in range(i + 1, n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dist_sq = dx*dx + dy*dy
        if min_dist_sq is None or dist_sq < min_dist_sq:
            min_dist_sq = dist_sq

print(min_dist_sq)