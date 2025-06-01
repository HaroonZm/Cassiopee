def quickhull(left_point, right_point, set_points, hull_list, index_left, index_right):
    if not set_points:
        return
    above = []
    below = []
    vec_lr = (right_point[0] - left_point[0], right_point[1] - left_point[1])
    for x, y in set_points:
        vec_lx = (x - left_point[0], y - left_point[1])
        cp = cross(vec_lr, vec_lx)
        if cp > 0:
            above.append((x, y))
        elif cp < 0:
            below.append((x, y))
    
    mid_index = (index_right - index_left) / 2
    
    # handling points above the line
    if above:
        c, d = direction(left_point, right_point, above[0])
        far_point = above[0]
        for i in range(1, len(above)):
            c_, d_ = direction(left_point, right_point, above[i])
            if c * d_ < c_ * d:
                c, d = c_, d_
                far_point = above[i]
        i = index_right + mid_index
        hull_list.append((tuple(far_point), i))
        
        b_vec = (left_point[0] - far_point[0], left_point[1] - far_point[1])
        c_vec = (far_point[0] - right_point[0], far_point[1] - right_point[1])
        subset1 = []
        subset2 = []
        for x, y in above:
            b_ = (x - far_point[0], y - far_point[1])
            c_ = (x - right_point[0], y - right_point[1])
            cross_b = cross(b_vec, b_)
            cross_c = cross(c_vec, c_)
            if cross_b >= 0 and cross_c >= 0:
                continue
            else:
                if cross_b < 0:
                    subset1.append((x, y))
                elif cross_c < 0:
                    subset2.append((x, y))
        quickhull(left_point, far_point, subset1, hull_list, index_left, i)
        quickhull(right_point, far_point, subset2, hull_list, index_right, i)
    
    # handling points below the line
    if below:
        c, d = direction(left_point, right_point, below[0])
        far_point = below[0]
        for i in range(1, len(below)):
            c_, d_ = direction(left_point, right_point, below[i])
            if c * d_ < c_ * d:
                c, d = c_, d_
                far_point = below[i]
        i = index_left + mid_index
        hull_list.append((tuple(far_point), i))
        
        b_vec = (left_point[0] - far_point[0], left_point[1] - far_point[1])
        c_vec = (far_point[0] - right_point[0], far_point[1] - right_point[1])
        subset1 = []
        subset2 = []
        for x, y in below:
            b_ = (x - far_point[0], y - far_point[1])
            c_ = (x - right_point[0], y - right_point[1])
            cross_b = cross(b_vec, b_)
            cross_c = cross(c_vec, c_)
            if cross_b <= 0 and cross_c <= 0:
                continue
            else:
                if cross_b > 0:
                    subset1.append((x, y))
                elif cross_c > 0:
                    subset2.append((x, y))
        quickhull(left_point, far_point, subset1, hull_list, index_left, i)
        quickhull(far_point, right_point, subset2, hull_list, i, index_right)
    
    hull_list.sort(key=lambda x: x[1])
    return tuple(zip(*hull_list))[0]

def cross(a, b):
    # cross product of 2D vectors a and b
    return a[0]*b[1] - a[1]*b[0]

def direction(left_point, right_point, point):
    # Returns a kind of "distance" metric and normalization factor
    a = right_point[1] - left_point[1]
    b = left_point[0] - right_point[0]
    val = a * (point[0] - left_point[0]) + b * (point[1] - left_point[1])
    return val * val, a*a + b*b

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])  # path compression
    return par[x]

def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        par[rx] = ry
    else:
        par[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1

from collections import defaultdict

n, r = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

point_to_index = defaultdict(int)
for i, (x,y) in enumerate(points):
    point_to_index[(x,y)] = i

sorted_points = sorted(points)
edges = []
for _ in range(r):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    dist = ((points[a][0] - points[b][0])**2 + (points[a][1] - points[b][1])**2) ** 0.5
    edges.append((a, b, dist))
edges.sort(key=lambda x: x[2])

left_pt = tuple(sorted_points.pop(0))
right_pt = tuple(sorted_points.pop(-1))
hull_indices = quickhull(left_pt, right_pt, sorted_points, [(left_pt, 0), (right_pt, n)], 0, n)

par = [i for i in range(n+1)]
rank = [0]*(n+1)

for p in hull_indices:
    par[point_to_index[p]] = n
    rank[n] = 1

total_length = 0
for i in range(len(hull_indices)):
    prev = hull_indices[i-1]
    curr = hull_indices[i]
    total_length += ((prev[0] - curr[0])**2 + (prev[1] - curr[1])**2)**0.5

for x, y, dist in edges:
    if root(x) != root(y):
        total_length += dist
        unite(x, y)

print(total_length)