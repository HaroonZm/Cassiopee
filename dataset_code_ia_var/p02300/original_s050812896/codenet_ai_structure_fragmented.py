import sys
from operator import attrgetter
import cmath
from math import isinf, sqrt, acos
readline = sys.stdin.readline
EPS = 1e-9
ONLINE_FRONT = -2
CLOCKWISE = -1
ON_SEGMENT = 0
COUNTER_CLOCKWISE = 1
ONLINE_BACK = 2

class Circle:
    __slots__ = ('c', 'r')
    def __init__(self, c, r):
        self.c = c
        self.r = r

class Segment:
    __slots__ = ('fi', 'se')
    def __init__(self, fi, se):
        self.fi = fi
        self.se = se

Line = Segment

def get_real(point):
    return point.real

def get_imag(point):
    return point.imag

def point_sub(a, b):
    return a - b

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def norm(base):
    return abs(base) ** 2

def get_base_segment(s):
    return s.fi - s.se

def get_diff_point_line(s, p2):
    return p2 - s.fi

def get_proj_ratio(s, p2):
    base = get_base_segment(s)
    diff = get_diff_point_line(s, p2)
    return dot(diff, base) / norm(base)

def get_projected_point(s, p2):
    base = get_base_segment(s)
    r = get_proj_ratio(s, p2)
    return s.fi + base * r

def project(s, p2):
    return get_projected_point(s, p2)

def reflect(s, p):
    return p + (project(s, p) - p) * 2.0

def get_a(p1, p2):
    return p2 - p1

def get_b(p1, p3):
    return p3 - p1

def ccw_cond1(a, b):
    return cross(a, b) > EPS

def ccw_cond2(a, b):
    return cross(a, b) < -EPS

def ccw_cond3(a, b):
    return dot(a, b) < -EPS

def ccw_cond4(a, b):
    return norm(a) < norm(b)

def ccw(p1, p2, p3):
    a = get_a(p1, p2)
    b = get_b(p1, p3)
    if ccw_cond1(a, b): return 1
    if ccw_cond2(a, b): return -1
    if ccw_cond3(a, b): return 2
    if ccw_cond4(a, b): return -2
    return 0

def ccw_wrap1(p1, p2, p3):
    return ccw(p1, p2, p3)

def ccw_wrap2(p1, p2, p4):
    return ccw(p1, p2, p4)

def ccw_wrap3(p3, p4, p1):
    return ccw(p3, p4, p1)

def ccw_wrap4(p3, p4, p2):
    return ccw(p3, p4, p2)

def intersect4(p1, p2, p3, p4):
    return (ccw_wrap1(p1, p2, p3) * ccw_wrap2(p1, p2, p4) <= 0 and
            ccw_wrap3(p3, p4, p1) * ccw_wrap4(p3, p4, p2) <= 0)

def get_seg_ends(s):
    return s.fi, s.se

def intersect2(s1, s2):
    fi1, se1 = get_seg_ends(s1)
    fi2, se2 = get_seg_ends(s2)
    return intersect4(fi1, se1, fi2, se2)

def getDistance(a, b):
    return abs(a - b)

def get_l_se(l):
    return l.se

def get_l_fi(l):
    return l.fi

def get_diff_l(l):
    return l.se - l.fi

def get_diff_p(l, p):
    return p - l.fi

def getDistanceLP(l, p):
    diff_l = get_diff_l(l)
    diff_p = get_diff_p(l, p)
    return abs(cross(diff_l, diff_p) / abs(diff_l))

def get_dot1(s, p):
    return dot(s.se - s.fi, p - s.fi)

def get_dot2(s, p):
    return dot(s.fi - s.se, p - s.se)

def getDistanceSP(s, p):
    dot1 = get_dot1(s, p)
    if dot1 < 0.0: return abs(p - s.fi)
    dot2 = get_dot2(s, p)
    if dot2 < 0.0: return abs(p - s.se)
    return getDistanceLP(s, p)

def getDistanceSP_wrap1(s1, s2):
    return getDistanceSP(s1, s2.fi)

def getDistanceSP_wrap2(s1, s2):
    return getDistanceSP(s1, s2.se)

def getDistanceSP_wrap3(s2, s1):
    return getDistanceSP(s2, s1.fi)

def getDistanceSP_wrap4(s2, s1):
    return getDistanceSP(s2, s1.se)

def getDistances(s1, s2):
    if intersect2(s1, s2): return 0.0
    return min(getDistanceSP_wrap1(s1, s2), getDistanceSP_wrap2(s1, s2),
               getDistanceSP_wrap3(s2, s1), getDistanceSP_wrap4(s2, s1))

def cross_base(base, point):
    return cross(base, point)

def get_abs_cross(base, point):
    return abs(cross_base(base, point))

def getCrossPoint(s1, s2):
    base = s2.se - s2.fi
    d1 = get_abs_cross(base, s1.fi - s2.fi)
    d2 = get_abs_cross(base, s1.se - s2.fi)
    t = d1 / (d1 + d2)
    return s1.fi + (s1.se - s1.fi) * t

def get_e(l):
    return (l.se - l.fi) / abs(l.se - l.fi)

def get_base_cl(c, pr):
    return sqrt(c.r * c.r - norm(pr - c.c))

def getCrossPointsCL(c, l):
    pr = project(l, c.c)
    e = get_e(l)
    base = get_base_cl(c, pr)
    p1 = pr + e * base
    p2 = pr - e * base
    points = [p1, p2]
    points_sorted = sorted(points, key=attrgetter('real', 'imag'))
    return Segment(*points_sorted)

def get_d_cc(c1, c2):
    return abs(c1.c - c2.c)

def get_a_cc(c1, c2, d):
    return acos((c1.r * c1.r + d * d - c2.r * c2.r) / (2.0 * c1.r * d))

def get_t_cc(c1, c2):
    return cmath.phase(c2.c - c1.c)

def getCrossPointsCC(c1, c2):
    d = get_d_cc(c1, c2)
    a = get_a_cc(c1, c2, d)
    t = get_t_cc(c1, c2)
    p1 = c1.c + cmath.rect(c1.r, t + a)
    p2 = c1.c + cmath.rect(c1.r, t - a)
    points = [p1, p2]
    points_sorted = sorted(points, key=attrgetter('real', 'imag'))
    return Segment(*points_sorted)

def contains_shapepoint(g, i, p):
    a = g[i] - p
    b = g[(i + 1) % len(g)] - p
    return a, b

def contains_cross_cond(a, b):
    return abs(cross(a, b)) < EPS and dot(a, b) < EPS

def contains_swap_cond(a, b):
    return a.imag > b.imag

def contains_y_cond(a, b):
    return a.imag < EPS and EPS < b.imag and cross(a, b) > EPS

def contains(g, p):
    n = len(g)
    x = False
    for i in range(n):
        a, b = contains_shapepoint(g, i, p)
        if contains_cross_cond(a, b): return 1
        if contains_swap_cond(a, b): a, b = b, a
        if contains_y_cond(a, b): x = not x
    return 2 if x else 0

def sort_key_by_imag(pt):
    return pt.imag

def sort_points_imag(s):
    return sorted(s, key=sort_key_by_imag)

def create_u_l(s):
    u = s[0:2]
    l = s[-2:][::-1]
    return u, l

def append_point(u, i):
    u.append(i)

def pop_point(u):
    u.pop()

def pop_check(u, i):
    for q in range(len(u), 1, -1):
        _ccw = ccw(u[q - 2], u[q - 1], i)
        if not (_ccw != CLOCKWISE and _ccw != ONLINE_FRONT): break
        pop_point(u)
    append_point(u, i)

def pop_check_reverse(l, i):
    for q in range(len(l), 1, -1):
        _ccw = ccw(l[q - 2], l[q - 1], i)
        if not (_ccw != CLOCKWISE and _ccw != ONLINE_FRONT): break
        pop_point(l)
    append_point(l, i)

def build_upper(s, u):
    for i in s[2:]:
        pop_check(u, i)

def build_lower(s, l):
    for i in s[:-2][::-1]:
        pop_check_reverse(l, i)

def join_hull(l, u):
    return l[::-1] + u[1:len(u) - 1][::-1]

def andrewScan(s):
    if len(s) < 3: return s
    s = sort_points_imag(s)
    u, l = create_u_l(s)
    build_upper(s, u)
    build_lower(s, l)
    return join_hull(l, u)

def parse_int(val):
    return int(val)

def parse_complex_from_str(s):
    return complex(*map(parse_int, s.split()))

def readline_strip():
    return readline().strip()

def make_pg_list(n):
    return [parse_complex_from_str(readline_strip()) for _ in [0] * n]

def print_len(ans):
    print(len(ans))

def print_point(p):
    print(int(p.real), int(p.imag))

def print_ans(ans):
    for i in range(len(ans)):
        print_point(ans[i])

def main():
    n = parse_int(readline_strip())
    pg = make_pg_list(n)
    ans = andrewScan(pg)
    print_len(ans)
    print_ans(ans)

main()