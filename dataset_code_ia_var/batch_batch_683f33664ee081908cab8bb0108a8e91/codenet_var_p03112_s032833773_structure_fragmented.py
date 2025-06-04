def read_inputs():
    A, B, Q = map(int, input().split())
    return A, B, Q

def get_inf():
    return 10 ** 11

def read_list(n):
    return [int(input()) for _ in range(n)]

def build_extended_list(lst, inf):
    return [-inf] + lst + [inf]

def prepare_all_lists():
    A, B, Q = read_inputs()
    inf = get_inf()
    S_raw = read_list(A)
    T_raw = read_list(B)
    X = read_list(Q)
    S = build_extended_list(S_raw, inf)
    T = build_extended_list(T_raw, inf)
    return S, T, X, Q

def get_positions(lst, x):
    import bisect
    p1 = bisect.bisect_right(lst, x)
    p2 = p1 - 1
    return p1, p2

def get_values(lst, idx1, idx2):
    return lst[idx1], lst[idx2]

def compute_distance(a, b, c):
    return abs(a - b) + abs(b - c)

def all_distances(x, s1, s2, t1, t2):
    res = []
    res.append(compute_distance(x, s1, t1))
    res.append(compute_distance(x, s2, t2))
    res.append(compute_distance(x, t1, s1))
    res.append(compute_distance(x, t2, s2))
    res.append(compute_distance(x, s1, t2))
    res.append(compute_distance(x, s2, t1))
    res.append(compute_distance(x, t1, s2))
    res.append(compute_distance(x, t2, s1))
    return res

def process_query(x, S, T):
    s1_idx, s2_idx = get_positions(S, x)
    t1_idx, t2_idx = get_positions(T, x)
    s1, s2 = get_values(S, s1_idx, s2_idx)
    t1, t2 = get_values(T, t1_idx, t2_idx)
    distances = all_distances(x, s1, s2, t1, t2)
    return min(distances)

def main():
    S, T, X, Q = prepare_all_lists()
    for i in range(Q):
        res = process_query(X[i], S, T)
        print(res)

main()