import sys
from math import sin as math_sin, cos as math_cos, tan as math_tan, radians as math_radians
from heapq import heappush as heapq_push, heappop as heapq_pop

input_read = sys.stdin.readline
output_write = sys.stdout.write

def point_dot(origin, a, b):
    ox, oy = origin
    ax, ay = a
    bx, by = b
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)

def point_cross(origin, a, b):
    ox, oy = origin
    ax, ay = a
    bx, by = b
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)

def point_dist_sq(a, b):
    ax, ay = a
    bx, by = b
    return (ax - bx) ** 2 + (ay - by) ** 2

def segment_intersects(pa_start, pa_end, pb_start, pb_end):
    c0 = point_cross(pa_start, pa_end, pb_start)
    c1 = point_cross(pa_start, pa_end, pb_end)
    if c0 == 0 and c1 == 0:
        e0 = point_dot(pa_start, pa_end, pb_start)
        e1 = point_dot(pa_start, pa_end, pb_end)
        if not e0 < e1:
            e0, e1 = e1, e0
        return e0 <= point_dist_sq(pa_start, pa_end) and 0 <= e1
    d0 = point_cross(pb_start, pb_end, pa_start)
    d1 = point_cross(pb_start, pb_end, pa_end)
    return c0 * c1 <= 0 and d0 * d1 <= 0

def polygon_convex_hull(points):
    hull = []
    n_points = len(points)
    for p in points:
        while len(hull) > 1 and point_cross(hull[-1], hull[-2], p) >= 0:
            hull.pop()
        hull.append(p)
    upper = len(hull)
    for i in range(n_points-2, -1, -1):
        p = points[i]
        while len(hull) > upper and point_cross(hull[-1], hull[-2], p) >= 0:
            hull.pop()
        hull.append(p)
    return hull

def vec_cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def vec_dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def vec_dist_sq(a):
    return a[0]**2 + a[1]**2

def point_to_segment_dist_sq(x, seg_a, seg_b):
    seg_vec = (seg_b[0] - seg_a[0], seg_b[1] - seg_a[1])
    x_vec = (x[0] - seg_a[0], x[1] - seg_a[1])
    dp = vec_dot(seg_vec, x_vec)
    seg_len_sq = vec_dist_sq(seg_vec)
    if 0 <= dp <= seg_len_sq:
        return vec_cross(seg_vec, x_vec) ** 2 / seg_len_sq
    x_vec_b = (x[0] - seg_b[0], x[1] - seg_b[1])
    return min(vec_dist_sq(x_vec), vec_dist_sq(x_vec_b))

def polygon_contains(point, poly_points):
    if len(poly_points) == 1:
        return 0
    poly_len = len(poly_points)
    return (
        all(point_cross(poly_points[i-1], poly_points[i], point) > 0 for i in range(poly_len)) or
        all(point_cross(poly_points[i-1], poly_points[i], point) < 0 for i in range(poly_len))
    )

def convex_polygon_contains(point, convex_points):
    n = len(convex_points)
    if n < 3:
        return False
    left_idx, right_idx = 1, n
    q0 = convex_points[0]
    while left_idx + 1 < right_idx:
        mid_idx = (left_idx + right_idx) >> 1
        if point_cross(q0, point, convex_points[mid_idx]) <= 0:
            left_idx = mid_idx
        else:
            right_idx = mid_idx
    if left_idx == n - 1:
        left_idx -= 1
    qi = convex_points[left_idx]
    qj = convex_points[left_idx+1]
    v0 = point_cross(q0, qi, qj)
    v1 = point_cross(q0, point, qj)
    v2 = point_cross(q0, qi, point)
    if v0 < 0:
        v1 = -v1
        v2 = -v2
    return 0 <= v1 and 0 <= v2 and v1 + v2 <= v0

def convex_polygons_intersect(poly1, poly2):
    len1, len2 = len(poly1), len(poly2)
    if len1 == 1 or len2 == 1:
        return 0
    i, j = 0, 0
    while (i < len1 or j < len2) and (i < 2*len1) and (j < 2*len2):
        pa0 = poly1[(i-1)%len1]
        pa1 = poly1[i%len1]
        pb0 = poly2[(j-1)%len2]
        pb1 = poly2[j%len2]
        if segment_intersects(pa0, pa1, pb0, pb1):
            return 1
        ax = pa1[0] - pa0[0]
        ay = pa1[1] - pa0[1]
        bx = pb1[0] - pb0[0]
        by = pb1[1] - pb0[1]
        cross_val = ax * by - bx * ay
        cross_a = point_cross(pb0, pb1, pa1)
        cross_b = point_cross(pa0, pa1, pb1)
        if cross_val == 0 and cross_a < 0 and cross_b < 0:
            return 0
        if cross_val == 0 and cross_a == 0 and cross_b == 0:
            i += 1
        elif cross_val >= 0:
            if cross_b > 0:
                i += 1
            else:
                j += 1
        else:
            if cross_a > 0:
                j += 1
            else:
                i += 1
    return 0

def polygon_find_tangent(point, polygon):
    n = len(polygon)
    d = n // 3
    centroid_x = (polygon[0][0] + polygon[d][0] + polygon[2*d][0]) / 3
    centroid_y = (polygon[0][1] + polygon[d][1] + polygon[2*d][1]) / 3
    centroid = (centroid_x, centroid_y)
    max_v = -1
    min_v = 2
    min_idx = 0
    max_idx = 0
    for i in range(n):
        v = point_cross(point, polygon[i], centroid) / (point_dist_sq(point, centroid) * point_dist_sq(point, polygon[i])) ** 0.5
        if v > max_v:
            max_idx = i
            max_v = v
        if v < min_v:
            min_idx = i
            min_v = v
    return min_idx, max_idx

def polygon_tangent_distance(poly_a, poly_b):
    len_a = len(poly_a)
    len_b = len(poly_b)
    a_min, a_max = polygon_find_tangent(poly_b[0], poly_a)
    b_min, b_max = polygon_find_tangent(poly_a[0], poly_b)
    if a_max < a_min:
        a_max += len_a
    if b_max < b_min:
        b_max += len_b
    min_dist = point_dist_sq(poly_a[a_min], poly_b[b_min])
    if b_min < b_max:
        for i in range(a_min, a_max+1):
            pt_a = poly_a[i - len_a]
            for j in range(b_min, b_max+1):
                min_dist = min(min_dist, point_to_segment_dist_sq(pt_a, poly_b[(j-1)%len_b], poly_b[j-len_b]))
    if a_min < a_max:
        for j in range(b_min, b_max+1):
            pt_b = poly_b[j - len_b]
            for i in range(a_min, a_max+1):
                min_dist = min(min_dist, point_to_segment_dist_sq(pt_b, poly_a[(i-1)%len_a], poly_a[i-len_a]))
    return min_dist ** 0.5

def polygons_distance(poly_a, poly_b):
    if (
        convex_polygons_intersect(poly_a, poly_b)
        or convex_polygon_contains(poly_a[0], poly_b)
        or convex_polygon_contains(poly_b[0], poly_a)
    ):
        return 0
    return polygon_tangent_distance(poly_a, poly_b)

def main_solver():
    n = int(input_read())
    if n == 0:
        return False
    poly_list = [[] for _ in range(n)]
    poly_height = [0] * n
    for i in range(n):
        inp = list(map(int, input_read().split()))
        k, h = inp[0], inp[1]
        poly_height[i] = h
        vert_list = poly_list[i]
        for j in range(k):
            x, y = inp[2 + 2*j], inp[2 + 2*j + 1]
            vert_list.append((x, y))
    angle_theta, angle_phi = map(int, input_read().split())
    rad_theta = math_radians(angle_theta)
    rad_phi = math_radians(90 - angle_phi)
    dir_dx = -math_cos(rad_theta) * math_tan(rad_phi)
    dir_dy = -math_sin(rad_theta) * math_tan(rad_phi)
    sx, sy, tx, ty = map(int, input_read().split())
    for i in range(n):
        verts = poly_list[i]
        height = poly_height[i]
        num_pts = len(verts)
        for j in range(num_pts):
            x, y = verts[j]
            verts.append((x + height * dir_dx, y + height * dir_dy))
        verts.sort()
        poly_list[i] = polygon_convex_hull(verts)[:-1]
    poly_list.append([(sx, sy)])
    poly_list.append([(tx, ty)])
    total_polys = n + 2
    edge_dist = [[0]*total_polys for _ in range(total_polys)]
    min_dist = [10**18] * total_polys
    for i in range(total_polys):
        for j in range(i+1, total_polys):
            edge_dist[i][j] = edge_dist[j][i] = polygons_distance(poly_list[i], poly_list[j])
    pq = [(0, n)]
    min_dist[n] = 0
    while pq:
        dist_now, vtx_now = heapq_pop(pq)
        if min_dist[vtx_now] < dist_now:
            continue
        for vtx_next in range(total_polys):
            new_dist = dist_now + edge_dist[vtx_now][vtx_next]
            if new_dist < min_dist[vtx_next]:
                min_dist[vtx_next] = new_dist
                heapq_push(pq, (new_dist, vtx_next))
    print("%.16f" % min_dist[n+1])
    return True

while main_solver():
    pass