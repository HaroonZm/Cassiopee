def parse_ints_from_string(s):
    return list(map(int, s.split()))

def parse_four_ints(s):
    a, b, c, d = parse_ints_from_string(s)
    return a, b, c, d

def build_complex(a, b):
    return a + b * 1j

def string_to_complex_tuple(s):
    a, b, c, d = parse_four_ints(s)
    return build_complex(a, b), build_complex(c, d)

def real_part(z):
    return z.real

def imag_part(z):
    return z.imag

def dot_product(c1, c2):
    return real_part(c1) * real_part(c2) + imag_part(c1) * imag_part(c2)

def cross_product(c1, c2):
    return real_part(c1) * imag_part(c2) - imag_part(c1) * real_part(c2)

def subtract_complex(p1, p2):
    return p1 - p2

def point_equals(p1, p2):
    return p1 == p2

def all_points_equal(p1, p3, p4):
    return point_equals(p1, p3) or point_equals(p1, p4)

def any_point_equals(p2, p3, p4):
    return point_equals(p2, p3) or point_equals(p2, p4)

def handle_colinear_points(p1, p2, p3, p4):
    if all_points_equal(p1, p3, p4):
        return p1
    elif any_point_equals(p2, p3, p4):
        return p2
    else:
        return None

def are_colinear(crs1, crs2):
    return crs1 == 0 and crs2 == 0

def cross_point_side(base, hypo):
    return abs(cross_product(base, hypo))

def cross_point_base(p3, p4):
    return subtract_complex(p4, p3)

def cross_point_hypo(p1, p3):
    return subtract_complex(p1, p3)

def cross_point_ratio(d1, d2):
    return d1 / (d1 + d2)

def cross_point_segment(p1, p2, ratio):
    return p1 + ratio * (p2 - p1)

def are_crossing(crs1, crs2, crs3, crs4):
    return crs1 * crs2 <= 0 and crs3 * crs4 <= 0

def compute_cross_point_if_possible(p1, p2, p3, p4, crs1, crs2, crs3, crs4):
    if are_crossing(crs1, crs2, crs3, crs4):
        base = cross_point_base(p3, p4)
        hypo1 = cross_point_hypo(p1, p3)
        hypo2 = cross_point_hypo(p2, p3)
        abs_base = abs(base)
        d1 = cross_point_side(base, hypo1) / abs_base
        d2 = cross_point_side(base, hypo2) / abs_base
        ratio = cross_point_ratio(d1, d2)
        return cross_point_segment(p1, p2, ratio)
    else:
        return None

def cross_point(p1, p2, p3, p4):
    crs1 = cross_product(subtract_complex(p2, p1), subtract_complex(p3, p1))
    crs2 = cross_product(subtract_complex(p2, p1), subtract_complex(p4, p1))
    if are_colinear(crs1, crs2):
        return handle_colinear_points(p1, p2, p3, p4)
    crs3 = cross_product(subtract_complex(p4, p3), subtract_complex(p1, p3))
    crs4 = cross_product(subtract_complex(p4, p3), subtract_complex(p2, p3))
    return compute_cross_point_if_possible(p1, p2, p3, p4, crs1, crs2, crs3, crs4)

def get_polygon_edges(polygon):
    return list(zip(polygon[0:], polygon[1:] + [polygon[0]]))

def swap_if_needed(a, b):
    if imag_part(a) > imag_part(b):
        return b, a
    return a, b

def edge_crosses_axis(a, b):
    return imag_part(a) <= 0 and imag_part(b) > 0 and cross_product(a, b) > 0

def toggle_flag(flag):
    return not flag

def contain(polygon):
    flag = False
    for a, b in get_polygon_edges(polygon):
        a, b = swap_if_needed(a, b)
        if edge_crosses_axis(a, b):
            flag = toggle_flag(flag)
    return flag

def last_element(seq):
    return seq[-1]

def is_goal_reached(goal, next_edge):
    return next_edge == goal

def update_edges(edges, next_edge):
    edges.append(next_edge)

def update_cross_points(cross_points, next_cp):
    cross_points.append(next_cp)

def remove_last_from_edges(edges):
    return edges.pop()

def set_dp_false(DP, e):
    DP[e] = False

def remove_last_from_cross_points(cross_points):
    cross_points.pop()

def dfs_contain(goal, edges, cross_points, adj_edge, DP):
    cur_edge = last_element(edges)
    for next_edge, next_cp in adj_edge[cur_edge]:
        if is_goal_reached(goal, next_edge):
            if contain(cross_points + [next_cp]):
                break
        elif next_edge not in edges and DP[next_edge]:
            update_edges(edges, next_edge)
            update_cross_points(cross_points, next_cp)
            if dfs_contain(goal, edges, cross_points, adj_edge, DP):
                break
            e = remove_last_from_edges(edges)
            set_dp_false(DP, e)
            remove_last_from_cross_points(cross_points)
    else:
        return False
    return True

def read_input_lines():
    from sys import stdin
    return stdin.readlines()

def readline_int(lines, idx):
    return int(lines[idx])

def build_edges(lines, n, offset):
    lst = [string_to_complex_tuple(lines[offset + i]) for i in range(n)]
    return list(enumerate(lst))

def build_empty_adj_edge(n):
    return [[] for _ in range(n)]

def connect_edges_combinations(edges, adj_edge):
    from itertools import combinations
    for e1, e2 in combinations(edges, 2):
        n1, t1 = e1
        n2, t2 = e2
        cp = cross_point(*t1, *t2)
        if cp:
            adj_edge[n1].append((n2, cp))
            adj_edge[n2].append((n1, cp))
    return adj_edge

def prune_leaves(adj_edge):
    n = len(adj_edge)
    flag = True
    while flag:
        for i, ae in enumerate(adj_edge):
            if len(ae) == 1:
                ne, cp = ae.pop()
                adj_edge[ne].remove((i, cp))
                break
        else:
            flag = False

def initialize_DP_before_e(e, n):
    return [False] * e + [True] * (n - e)

def process_edges(n, adj_edge):
    for e in range(n):
        DP = initialize_DP_before_e(e, n)
        if dfs_contain(e, [e], [], adj_edge, DP):
            print('yes')
            return
    print('no')

def solve():
    lines = read_input_lines()
    idx = 0
    while True:
        n = readline_int(lines, idx)
        if n == 0:
            break
        offset = idx + 1
        edges = build_edges(lines, n, offset)
        adj_edge = build_empty_adj_edge(n)
        adj_edge = connect_edges_combinations(edges, adj_edge)
        prune_leaves(adj_edge)
        process_edges(n, adj_edge)
        idx += 1 + n

solve()