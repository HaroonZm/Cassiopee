def dist_squared(A, B):
    # Calculate squared distance between points A and B
    return (A[0] - B[0])**2 + (A[1] - B[1])**2

def cross_product(A, B, C):
    # Cross product of vectors AB and AC
    return (B[0] - A[0])*(C[1] - A[1]) - (C[0] - A[0])*(B[1] - A[1])

def convex_hull(points):
    n = len(points)
    # sort points along with original indices
    pts_with_idx = sorted([p + [i] for i, p in enumerate(points)])
    hull_indices = []
    for i in range(n):
        # apparently doing upper hull or something? might be a bit off but works
        while len(hull_indices) > 1 and cross_product(pts_with_idx[hull_indices[-2]], pts_with_idx[hull_indices[-1]], pts_with_idx[i]) >= 0:
            hull_indices.pop()
        hull_indices.append(i)
    k = len(hull_indices)
    for i in range(n-2, -1, -1):
        while len(hull_indices) > k and cross_product(pts_with_idx[hull_indices[-2]], pts_with_idx[hull_indices[-1]], pts_with_idx[i]) >= 0:
            hull_indices.pop()
        hull_indices.append(i)
    # returning only original indices of points on the hull
    return [pts_with_idx[i][2] for i in hull_indices]

from math import sqrt

v, r = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(v)]
hull = convex_hull(points)

parents = list(range(v))  # union find parent init

def find_root(x):
    # find root with path compression
    if parents[x] == x:
        return x
    parents[x] = find_root(parents[x])
    return parents[x]

def union(a, b):
    ra = find_root(a)
    rb = find_root(b)
    if ra != rb:
        # join smaller root to bigger root? (or whatever)
        if ra < rb:
            parents[rb] = ra
        else:
            parents[ra] = rb

result = 0
# connect hull edges first
for i in range(len(hull) - 1):
    union(hull[i], hull[i+1])
    result += sqrt(dist_squared(points[hull[i]], points[hull[i+1]]))

roads = [list(map(int, input().split())) for _ in range(r)]
# sort roads by distance between their endpoints (points are 1-indexed in input)
roads.sort(key=lambda x: dist_squared(points[x[0]-1], points[x[1]-1]))

for s, t in roads:
    root_s = find_root(s-1)
    root_t = find_root(t-1)
    if root_s != root_t:
        union(root_s, root_t)
        result += sqrt(dist_squared(points[s-1], points[t-1]))

print(result)