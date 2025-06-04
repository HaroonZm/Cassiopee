from math import sqrt

def get_input():
    n = input()
    return n

def parse_circle_input(n):
    C = []
    for i in xrange(n):
        C.append(map(int, raw_input().split()))
    return C

def get_first_point(C):
    return [[C[0][:2]]]

def circle_intersection_params(C, i):
    x0, y0, r0 = C[i]
    x1, y1, r1 = C[i+1]
    return x0, y0, r0, x1, y1, r1

def calc_distance(x0, y0, x1, y1):
    return sqrt((x1 - x0)**2 + (y1 - y0)**2)

def get_rr_rd(C, i):
    x0, y0, r0, x1, y1, r1 = circle_intersection_params(C, i)
    rr = (x1 - x0)**2 + (y1 - y0)**2
    rd = sqrt(rr)
    return rr, rd, x0, y0, r0, x1, y1, r1

def get_rc(rsq, rr, r1sq, rd):
    return (rsq + rr - r1sq) / (2 * rd)

def get_rs(r0sq, rr, rsq, rr2, r1sq, rd):
    return sqrt(4 * r0sq * rr - (rsq + rr - r1sq)**2) / (2 * rd)

def get_ex_ey(x1, x0, y1, y0, rd):
    ex = (x1 - x0) / rd
    ey = (y1 - y0) / rd
    return ex, ey

def get_b(b0, e, rc):
    return b0 + e * rc

def compute_circle_intersections(C):
    n = len(C)
    P = get_first_point(C)
    for i in xrange(n-1):
        rr, rd, x0, y0, r0, x1, y1, r1 = get_rr_rd(C, i)
        rc = get_rc(r0**2, rr, r1**2, rd)
        rs = get_rs(r0**2, rr, r0**2, rr, r1**2, rd)
        ex, ey = get_ex_ey(x1, x0, y1, y0, rd)
        bx = get_b(x0, ex, rc)
        by = get_b(y0, ey, rc)
        p1 = (bx + ey * rs, by - ex * rs)
        p2 = (bx - ey * rs, by + ex * rs)
        P.append([p1, p2])
    P.append([C[-1][:2]])
    return P

def tuple_calc(p0, p1):
    return calc_distance(p0[0], p0[1], p1[0], p1[1])

def tuple_cross(a, b, c):
    x0, y0 = a
    x1, y1 = b
    x2, y2 = c
    return (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0)

def update_min_dist(dist, key, value, INF):
    dist[key] = min(dist.get(key, INF), value)

def initialize_dist():
    return {(0, 0): 0}

def check_and_update_left_right(left, right, lp, rp, x, y):
    if left is None or tuple_cross((x, y), left, lp) >= 0:
        left = lp
    if right is None or tuple_cross((x, y), rp, right) >= 0:
        right = rp
    return left, right

def left_right_valid(x, y, left, right):
    if left is None or right is None:
        return False
    return tuple_cross((x, y), left, right) < 0

def propagate_cost(dist, k, i, j, d, left, right, p_left, p_right, INF, x, y):
    if p_left != left:
        update_min_dist(dist, (k,0), d + tuple_calc((x, y), left), INF)
        p_left = left
    if p_right != right:
        update_min_dist(dist, (k,1), d + tuple_calc((x, y), right), INF)
        p_right = right
    return p_left, p_right

def check_goal_update(dist, i, j, n, P, x, y, left, right, d, INF):
    gp = P[-1][0]
    if (left is None and right is None) or (tuple_cross((x, y), left, gp) >= 0 and tuple_cross((x, y), gp, right) >= 0):
        update_min_dist(dist, (len(P)-1, 0), d + tuple_calc((x, y), gp), INF)

def process(P, n):
    INF = 10**18
    dist = initialize_dist()
    for i in xrange(n):
        for j, (x, y) in enumerate(P[i]):
            left, p_left, right, p_right = None, None, None, None
            d = dist[i, j]
            for k in xrange(i + 1, n):
                lp, rp = P[k]
                left, right = check_and_update_left_right(left, right, lp, rp, x, y)
                if left_right_valid(x, y, left, right):
                    break
                p_left, p_right = propagate_cost(dist, k, i, j, d, left, right, p_left, p_right, INF, x, y)
            else:
                check_goal_update(dist, i, j, n, P, x, y, left, right, d, INF)
    return dist

def print_final_dist(dist, P):
    print("%.06f" % dist[len(P)-1, 0])

def main_loop():
    while 1:
        n = get_input()
        if n == 0:
            break
        C = parse_circle_input(n)
        P = compute_circle_intersections(C)
        dist = process(P, n)
        print_final_dist(dist, P)

main_loop()