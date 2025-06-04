import sys

def get_readline():
    return sys.stdin.readline

def get_write():
    return sys.stdout.write

def get_eps():
    return 1e-9

def get_line_values():
    return list(map(int, readline().split()))

def extract_points(L):
    x1, y1, x2, y2 = L
    return (x1, y1), (x2, y2)

def subtract_coords(a, b):
    return a[0] - b[0], a[1] - b[1]

def det2(a, b, c, d):
    return a*d - b*c

def is_zero(x):
    return -EPS < x < EPS

def distance_from_origin(x, y):
    return (x**2 + y**2) ** 0.5

def add_vectors(a, b):
    return a[0] + b[0], a[1] + b[1]

def scale_vector(a, k):
    return a[0] * k, a[1] * k

def vec_length(a):
    return (a[0]**2 + a[1]**2) ** 0.5

def line_cross_point(P1, P2, Q1, Q2):
    x0, y0 = P1
    x1, y1 = P2
    x2, y2 = Q1
    x3, y3 = Q2

    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0 - y2) * dx1 - (x0 - x2) * dy1
    sm = dx0 * dy1 - dy0 * dx1
    if is_zero(sm):
        return None
    return x0 + s * dx0 / sm, y0 + s * dy0 / sm

def make_bisector_single_set(p1, p2, q1, q2):
    dx0, dy0 = p2[0] - p1[0], p2[1] - p1[1]
    dx1, dy1 = q2[0] - q1[0], q2[1] - q1[1]
    cp = line_cross_point(p1, p2, q1, q2)
    if cp is None:
        return None
    cx, cy = cp
    d0 = (dx0**2 + dy0**2)**.5
    d1 = (dx1**2 + dy1**2)**.5
    v1 = (dx0*d1 + dx1*d0, dy0*d1 + dy1*d0)
    v2 = (dx0*d1 - dx1*d0, dy0*d1 - dy1*d0)
    return [ ((cx,cy), (cx+v1[0], cy+v1[1])),
             ((cx,cy), (cx+v2[0], cy+v2[1])) ]

def bisector(P1, P2, Q1, Q2):
    return make_bisector_single_set(P1, P2, Q1, Q2)

def get_line_points_distance_sq(p1, p2, q):
    x, y = q
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    dd = dx ** 2 + dy ** 2
    sv = (x - x1) * dy - (y - y1) * dx
    return abs(sv / dd ** .5)

def get_all_distances(LS, q):
    return [ get_line_points_distance_sq(p1, p2, q) for p1, p2 in LS ]

def distances_all_equal(ds):
    return all(abs(ds[0] - e) < EPS for e in ds)

def check(LS, q):
    ds = get_all_distances(LS, q)
    return distances_all_equal(ds)

def parse_num_lines():
    return int(readline())

def handle_input(N):
    P = []
    for _ in range(N):
        L = get_line_values()
        a, b = extract_points(L)
        P.append((a, b))
    return P

def answer_many():
    write("Many\n")

def answer_none():
    write("None\n")

def answer_point(pt):
    write("%.16f %.16f\n" % pt)

def already_in_ans(ans, pt):
    cx, cy = pt
    for ax, ay in ans:
        if abs(cx - ax) < EPS and abs(cy - ay) < EPS:
            return True
    return False

def get_two_bisectors(P):
    s = []
    N = len(P)
    for i in range(N):
        p1, p2 = P[i]
        for j in range(i):
            q1, q2 = P[j]
            bs = bisector(p1, p2, q1, q2)
            if bs is None:
                continue
            s.append(bs)
            if len(s) > 1:
                break
        else:
            continue
        break
    return s

def solve():
    N = parse_num_lines()
    if N == 0:
        return False
    P = handle_input(N)
    if N <= 2:
        answer_many()
        return True

    s = get_two_bisectors(P)
    if len(s) < 2:
        answer_none()
        return True
    ans = []
    b1, b2 = s
    for p1, p2 in b1:
        for q1, q2 in b2:
            cp = line_cross_point(p1, p2, q1, q2)
            if cp is None:
                continue
            if check(P, cp):
                if not already_in_ans(ans, cp):
                    ans.append(cp)
    if len(ans) == 0:
        answer_none()
    elif len(ans) > 1:
        answer_many()
    else:
        answer_point(ans[0])
    return True

EPS = get_eps()
readline = get_readline()
write = get_write()
while solve():
    ...