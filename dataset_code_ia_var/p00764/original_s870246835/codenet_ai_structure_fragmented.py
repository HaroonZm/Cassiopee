def read_input():
    from sys import stdin
    return stdin

def read_n(file_input):
    return int(file_input.readline())

def read_circle_params(file_input, n):
    return [tuple(map(int, file_input.readline().split())) for _ in range(n)]

def make_circle_map(circle_params):
    for params in circle_params:
        yield params

def calc_cross_points(C, n):
    from math import acos
    from cmath import phase, rect
    P = []
    circle_iter = iter(C)
    x, y, r1 = next(circle_iter)
    c1 = x + y * 1j
    P.append(c1)
    for x, y, r2 in circle_iter:
        c2 = x + y * 1j
        base = c2 - c1
        d = abs(base)
        a = acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
        t = phase(base)
        cp1 = c1 + rect(r1, t + a)
        cp2 = c1 + rect(r1, t - a)
        P.append(cp1)
        P.append(cp2)
        c1, r1 = c2, r2
    return P, c1

def init_dist(n, lim=5000):
    dist = [lim] * (2 * n)
    dist[0] = 0
    return dist

def get_g_idx(n):
    return 2 * n - 1

def build_indices(g_idx):
    for i in range(g_idx):
        yield (i + (i % 2) + 1, i + (i % 2) + 2)

def phase_ge_0(x):
    from cmath import phase
    return phase(x) >= 0

def phase_le_0(x):
    from cmath import phase
    return phase(x) <= 0

def phase_lt_0(x):
    from cmath import phase
    return phase(x) < 0

def update_distances(indices, P, dist, g_idx, goal):
    for tpl_idx, cp, d in zip(indices, P, dist):
        process_update(tpl_idx, cp, d, P, dist, g_idx, goal)

def process_update(tpl_idx, cp, d, P, dist, g_idx, goal):
    j, k = tpl_idx
    s1 = None
    s2 = None
    p_s1 = None
    p_s2 = None
    loop_range = list(range(j, g_idx, 2))
    for l, cp1, cp2 in zip(loop_range, P[j::2], P[k::2]):
        t_s1 = cp1 - cp
        t_s2 = cp2 - cp
        if s1 is None or phase_ge_0(s1 / t_s1):
            s1 = t_s1
        if s2 is None or phase_le_0(s2 / t_s2):
            s2 = t_s2
        if phase_lt_0(s1 / s2):
            break
        if p_s1 != s1:
            dist[l] = min(dist[l], d + abs(s1))
            p_s1 = s1
        if p_s2 != s2:
            dist[l+1] = min(dist[l+1], d + abs(s2))
            p_s2 = s2
    else:
        update_goal_dist(s1, s2, cp, goal, dist, g_idx, d)

def update_goal_dist(s1, s2, cp, goal, dist, g_idx, d):
    from cmath import phase
    gs = goal - cp
    if (s1 is None and s2 is None) or \
       (s1 is not None and s2 is not None and phase(s1 / gs) >= 0 and phase(s2 / gs) <= 0):
        dist[g_idx] = min(dist[g_idx], d + abs(gs))

def solve_problem(n, circle_params):
    map_gen = make_circle_map(circle_params)
    P, goal = calc_cross_points(map_gen, n)
    dist = init_dist(n)
    g_idx = get_g_idx(n)
    indices = build_indices(g_idx)
    update_distances(indices, P, dist, g_idx, goal)
    print(dist[g_idx])

def solve():
    file_input = read_input()
    while True:
        n = read_n(file_input)
        if n == 0:
            break
        circle_params = read_circle_params(file_input, n)
        solve_problem(n, circle_params)