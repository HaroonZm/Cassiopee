def string_to_float(s):
    return list(map(float, s.split()))

def read_lines():
    from sys import stdin
    return stdin.readlines()

def parse_n_from_lines(lines):
    return int(lines[0])

def check_break(n):
    return n == 0

def parse_circles(lines, n):
    return list(enumerate(map(string_to_float, lines[1:1+n])))

def init_cross_data(n):
    return [[] for _ in range(n)]

def init_included(n):
    return [False] * n

def compute_r_sum(lines, n):
    return sum(map(lambda x: float(x.split()[2]), lines[1:1+n]))

def init_ans(r_sum, pi):
    return 2 * pi * r_sum

def pairwise_combinations(circles):
    from itertools import combinations
    return combinations(circles, 2)

def get_circ_data(circle_tuple):
    n, xyr = circle_tuple
    x, y, r = xyr
    return n, x, y, r

def get_complex(x, y):
    return x + y * 1j

def skip_if_included(included, n1, n2):
    return included[n1] or included[n2]

def compute_distance(c1, c2):
    return abs(c2 - c1)

def check_non_intersect(d, r1, r2):
    return d >= r1 + r2

def check_contained(d, r1, r2):
    return d <= abs(r1 - r2)

def handle_containment(r1, r2, n1, n2, ans, included, pi):
    if r1 < r2:
        ans -= 2 * pi * r1
        included[n1] = True
    else:
        ans -= 2 * pi * r2
        included[n2] = True
    return ans

def acos_custom(val):
    from math import acos
    return acos(val)

def phase_custom(z):
    from cmath import phase
    return phase(z)

def insort_custom(cd, val):
    from bisect import insort
    insort(cd, val)

def handle_cross_data(cd, s, e, pi):
    if s >= -pi and e <= pi:
        insort_custom(cd, (s, -1))
        insort_custom(cd, (e, 1))
    elif s < -pi:
        insort_custom(cd, (s + 2 * pi, -1))
        insort_custom(cd, (pi, 1))
        insort_custom(cd, (-pi, -1))
        insort_custom(cd, (e, 1))
    else:
        insort_custom(cd, (s, -1))
        insort_custom(cd, (pi, 1))
        insort_custom(cd, (-pi, -1))
        insort_custom(cd, (e - 2 * pi, 1))

def process_combination(c1, c2, included, cross_data, ans, pi):
    n1, x1, y1, r1 = get_circ_data(c1)
    n2, x2, y2, r2 = get_circ_data(c2)
    if skip_if_included(included, n1, n2):
        return ans
    cn1 = get_complex(x1, y1)
    cn2 = get_complex(x2, y2)
    v12 = cn2 - cn1
    d = compute_distance(cn1, cn2)
    if check_non_intersect(d, r1, r2):
        return ans
    elif check_contained(d, r1, r2):
        ans = handle_containment(r1, r2, n1, n2, ans, included, pi)
        return ans
    a = acos_custom((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
    t = phase_custom(v12)
    s = t - a
    e = t + a
    cd = cross_data[n1]
    handle_cross_data(cd, s, e, pi)
    a = acos_custom((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))
    t = phase_custom(-v12)
    s = t - a
    e = t + a
    cd = cross_data[n2]
    handle_cross_data(cd, s, e, pi)
    return ans

def get_radius_list(lines, n):
    return list(map(lambda x: float(x.split()[2]), lines[1:1+n]))

def process_cross_data(cross_data, radius, ans):
    for cd, r in zip(cross_data, radius):
        flag = 0
        for ang, f in cd:
            if flag == 0:
                s = ang
            flag += f
            if flag == 0:
                ans -= r * (ang - s)
    return ans

def print_ans(ans):
    print(ans)

def remove_lines(lines, n):
    del lines[:1+n]

def solve():
    from math import pi
    lines = read_lines()
    while True:
        n = parse_n_from_lines(lines)
        if check_break(n):
            break
        circles = parse_circles(lines, n)
        cross_data = init_cross_data(n)
        included = init_included(n)
        r_sum = compute_r_sum(lines, n)
        ans = init_ans(r_sum, pi)
        for c1, c2 in pairwise_combinations(circles):
            ans = process_combination(c1, c2, included, cross_data, ans, pi)
        radius = get_radius_list(lines, n)
        ans = process_cross_data(cross_data, radius, ans)
        print_ans(ans)
        remove_lines(lines, n)

solve()