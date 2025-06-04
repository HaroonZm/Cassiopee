def parse_input_string(s):
    return list(map(int, s.split()))

def parse_to_a(s):
    return parse_input_string(s)[0]

def parse_to_b(s):
    return parse_input_string(s)[1]

def parse_to_c(s):
    return parse_input_string(s)[2]

def parse_to_d(s):
    return parse_input_string(s)[3]

def tuple_to_complex(a, b):
    return a + b * 1j

def string_to_first_complex(s):
    a = parse_to_a(s)
    b = parse_to_b(s)
    return tuple_to_complex(a, b)

def string_to_second_complex(s):
    c = parse_to_c(s)
    d = parse_to_d(s)
    return tuple_to_complex(c, d)

def string_to_complex_tuple(s):
    return (string_to_first_complex(s), string_to_second_complex(s))

def string_to_complex(s):
    return string_to_complex_tuple(s)

def get_real_part(c):
    return c.real

def get_imag_part(c):
    return c.imag

def dot_components(r1, r2, i1, i2):
    return r1 * r2 + i1 * i2

def dot(c1, c2):
    r1 = get_real_part(c1)
    r2 = get_real_part(c2)
    i1 = get_imag_part(c1)
    i2 = get_imag_part(c2)
    return dot_components(r1, r2, i1, i2)

def cross_components(r1, r2, i1, i2):
    return r1 * i2 - i1 * r2

def cross(c1, c2):
    r1 = get_real_part(c1)
    r2 = get_real_part(c2)
    i1 = get_imag_part(c1)
    i2 = get_imag_part(c2)
    return cross_components(r1, r2, i1, i2)

def points_are_equal(p1, p2):
    return p1 == p2

def cross_point_colinear(crs1, crs2):
    return crs1 == 0 and crs2 == 0

def cross_point_get(crs1, crs2, p1, p2, p3, p4):
    if cross_point_colinear(crs1, crs2):
        if points_are_equal(p1, p3) or points_are_equal(p1, p4):
            return p1
        elif points_are_equal(p2, p3) or points_are_equal(p2, p4):
            return p2
        else:
            return None
    return 'non-colinear'

def cross_point_main_body(crs1, crs2, crs3, crs4):
    return crs1 * crs2 <= 0 and crs3 * crs4 <= 0

def cross_point_calculation(p1, p2, p3, p4):
    base = p4 - p3
    hypo1 = p1 - p3
    hypo2 = p2 - p3
    den = abs(base)
    d1 = abs(cross(base, hypo1)) / den
    d2 = abs(cross(base, hypo2)) / den
    return p1 + d1 / (d1 + d2) * (p2 - p1)

def cross_point(p1, p2, p3, p4):
    delta_p2_p1 = p2 - p1
    delta_p3_p1 = p3 - p1
    delta_p4_p1 = p4 - p1
    crs1 = cross(delta_p2_p1, delta_p3_p1)
    crs2 = cross(delta_p2_p1, delta_p4_p1)
    colinear_result = cross_point_get(crs1, crs2, p1, p2, p3, p4)
    if colinear_result != 'non-colinear':
        return colinear_result
    delta_p4_p3 = p4 - p3
    delta_p1_p3 = p1 - p3
    delta_p2_p3 = p2 - p3
    crs3 = cross(delta_p4_p3, delta_p1_p3)
    crs4 = cross(delta_p4_p3, delta_p2_p3)
    if cross_point_main_body(crs1, crs2, crs3, crs4):
        return cross_point_calculation(p1, p2, p3, p4)
    else:
        return None

def make_zip_polygon(polygon):
    return zip(polygon[0:], polygon[1:] + [polygon[0]])

def compare_order_for_contain(a, b):
    if a.imag > b.imag:
        return b, a
    else:
        return a, b

def condition_contain(a, b):
    return a.imag <= 0 and b.imag > 0 and cross(a, b) > 0

def toggle_flag(flag):
    return not flag

def contain(polygon):
    flag = False
    for a, b in make_zip_polygon(polygon):
        a, b = compare_order_for_contain(a, b)
        if condition_contain(a, b):
            flag = toggle_flag(flag)
    return flag

def get_next_edge_from_ae(adj_edge, i):
    return adj_edge[i]

def remove_edge_from_adj(adj_edge, ne, i, cp):
    adj_edge[ne].remove((i, cp))

def prune_leaves(adj_edge):
    flag = True
    while flag:
        for i, ae in enumerate(adj_edge):
            if len(ae) == 1:
                ne, cp = ae.pop()
                remove_edge_from_adj(adj_edge, ne, i, cp)
                break
        else:
            flag = False

def make_unchecked_list(n):
    return [True] * n

def check_goal_contain(goal, cross_points, next_cp):
    return contain(cross_points + [next_cp])

def need_break(on_break):
    return on_break

def pop_and_unset(edges, cross_points, DP, e):
    e = edges.pop()
    DP[e] = False
    cross_points.pop()

def dfs_contain_inner(goal, edges, cross_points, adj_edge, unchecked, DP):
    cur_edge = edges[-1]
    for next_edge, next_cp in adj_edge[cur_edge]:
        if next_edge == goal:
            if check_goal_contain(goal, cross_points, next_cp):
                return True
        elif next_edge not in edges and unchecked[next_edge] and DP[next_edge]:
            edges.append(next_edge)
            cross_points.append(next_cp)
            if dfs_contain_inner(goal, edges, cross_points, adj_edge, unchecked, DP):
                return True
            pop_and_unset(edges, cross_points, DP, next_edge)
    return False

def dfs_contain(goal, edges, cross_points, adj_edge, unchecked, DP):
    return dfs_contain_inner(goal, edges, cross_points, adj_edge, unchecked, DP)

def get_n_from_lines(lines):
    return int(lines[0])

def get_edges(lines, n):
    return enumerate(map(string_to_complex, lines[1:1+n]))

def get_adj_edge(n):
    return [[] for _ in range(n)]

def combination_edges(edges):
    from itertools import combinations
    return combinations(edges, 2)

def append_cross_point(adj_edge, n1, n2, cp):
    adj_edge[n1].append((n2, cp))
    adj_edge[n2].append((n1, cp))

def get_cross_point_from_edges(t1, t2):
    return cross_point(*t1, *t2)

def handle_edges_and_adjacency(edges, adj_edge):
    for e1, e2 in combination_edges(edges):
        n1, t1 = e1
        n2, t2 = e2
        cp = get_cross_point_from_edges(t1, t2)
        if cp:
            append_cross_point(adj_edge, n1, n2, cp)

def lines_slice(lines, n):
    del lines[:1+n]

def process_edges_with_dfs(n, adj_edge):
    unchecked = make_unchecked_list(n)
    for e in range(n):
        unchecked[e] = False
        DP = [True] * n
        if dfs_contain(e, [e], [], adj_edge, unchecked, DP):
            print('yes')
            return
    print('no')

def main_loop(lines):
    while True:
        n = get_n_from_lines(lines)
        if n == 0:
            break
        edges = list(get_edges(lines, n))
        adj_edge = get_adj_edge(n)
        handle_edges_and_adjacency(edges, adj_edge)
        prune_leaves(adj_edge)
        process_edges_with_dfs(n, adj_edge)
        lines_slice(lines, n)

def solve():
    from sys import stdin
    lines = stdin.readlines()
    main_loop(lines)

solve()