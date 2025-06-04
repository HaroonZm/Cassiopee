from math import sqrt

def read_integer():
    return input()

def is_zero(n):
    return n == 0

def read_circle():
    return list(map(int, input().split()))

def read_circles(n):
    return [read_circle() for _ in range(n)]

def get_first_circle_point(circles):
    return circles[0][:2]

def get_last_circle_point(circles):
    return circles[-1][:2]

def diff_sq(x0, y0, x1, y1):
    return (x1 - x0) ** 2 + (y1 - y0) ** 2

def distance(x0, y0, x1, y1):
    return sqrt(diff_sq(x0, y0, x1, y1))

def get_coords(circle):
    return circle[:2]

def get_circle_tuple(circle):
    return tuple(circle)

def extract_circle_data(circles, i):
    return circles[i][0], circles[i][1], circles[i][2]

def compute_ex_ey(x0, y0, x1, y1, rd):
    ex = (x1 - x0) / rd
    ey = (y1 - y0) / rd
    return ex, ey

def compute_rr_rd(x0, y0, x1, y1):
    rr = diff_sq(x0, y0, x1, y1)
    rd = sqrt(rr)
    return rr, rd

def compute_rc_rs(r0, r1, rr, rd):
    rc = (r0 ** 2 + rr - r1 ** 2) / (2 * rd)
    rs = sqrt(4 * r0 ** 2 * rr - (r0 ** 2 + rr - r1 ** 2) ** 2) / (2 * rd)
    return rc, rs

def compute_bx_by(x0, y0, ex, ey, rc):
    bx = x0 + ex * rc
    by = y0 + ey * rc
    return bx, by

def generate_P(n, circles):
    P = [[get_first_circle_point(circles)]]
    for i in range(n - 1):
        x0, y0, r0 = extract_circle_data(circles, i)
        x1, y1, r1 = extract_circle_data(circles, i + 1)
        rr, rd = compute_rr_rd(x0, y0, x1, y1)
        rc, rs = compute_rc_rs(r0, r1, rr, rd)
        ex, ey = compute_ex_ey(x0, y0, x1, y1, rd)
        bx, by = compute_bx_by(x0, y0, ex, ey, rc)
        point1 = (bx + ey * rs, by - ex * rs)
        point2 = (bx - ey * rs, by + ex * rs)
        P.append([point1, point2])
    P.append([get_last_circle_point(circles)])
    return P

def calc_distance(p1, p2):
    x0, y0 = p1
    x1, y1 = p2
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

def cross_product(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

def initialize_dist():
    return {(0, 0): 0}

def get_P_k(P, k):
    return P[k][0], P[k][1]

def update_left_right(left, right, p_left, p_right, lp, rp, x, y):
    if left is None or cross_product((x, y), left, lp) >= 0:
        left = lp
    if right is None or cross_product((x, y), rp, right) >= 0:
        right = rp
    return left, right

def can_break(left, right, x, y):
    if cross_product((x, y), left, right) < 0:
        return True
    return False

def update_distances(dist, i, j, P, n, INF):
    for j_idx, (x, y) in enumerate(P[i]):
        left = None
        right = None
        p_left = None
        p_right = None
        d = dist[i, j_idx]
        for k in range(i + 1, n):
            lp, rp = P[k][0], P[k][1]
            left, right = update_left_right(left, right, p_left, p_right, lp, rp, x, y)
            if can_break(left, right, x, y):
                break
            if p_left != left:
                dist[k, 0] = min(dist.get((k, 0), INF), d + calc_distance((x, y), left))
                p_left = left
            if p_right != right:
                dist[k, 1] = min(dist.get((k, 1), INF), d + calc_distance((x, y), right))
                p_right = right
        else:
            goal_point = P[-1][0]
            if (left is None and right is None) or (cross_product((x, y), left, goal_point) >= 0 and cross_product((x, y), goal_point, right) >= 0):
                dist[len(P) - 1, 0] = min(dist.get((len(P) - 1, 0), INF), d + calc_distance((x, y), goal_point))

def main_loop():
    while True:
        n = read_integer()
        if is_zero(n):
            break
        circles = read_circles(n)
        P = generate_P(n, circles)
        INF = 10 ** 18
        dist = initialize_dist()

        for i in range(n):
            update_distances(dist, i, 0, P, n, INF)

        print("%.06f" % dist[len(P) - 1, 0])

main_loop()