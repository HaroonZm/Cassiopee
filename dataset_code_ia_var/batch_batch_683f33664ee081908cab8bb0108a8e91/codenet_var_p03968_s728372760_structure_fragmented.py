from collections import defaultdict

def read_single_int():
    return int(input().strip())

def read_int_list():
    return list(map(int, input().split()))

def generate_rotations(xs):
    return [tuple(xs[j:] + xs[:j]) for j in range(4)]

def find_minimal_rotation(cnd):
    return min(cnd)

def normalize_candidates(cnd, minimal, nrm):
    for item in cnd:
        nrm[item] = minimal

def update_counts(minimal, dd):
    dd[minimal] += 1

def compute_code(x):
    if x[0] == x[2] and x[1] == x[3]:
        return 4 if x[0] == x[1] else 2
    else:
        return 1

def update_code_dict(minimal, cc):
    cc[minimal] = compute_code(minimal)

def process_input(N):
    dd = defaultdict(int)
    cc = dict()
    nrm = dict()
    ss = []
    for _ in range(N):
        xs = read_int_list()
        cnd = generate_rotations(xs)
        minimal = find_minimal_rotation(cnd)
        normalize_candidates(cnd, minimal, nrm)
        update_counts(minimal, dd)
        update_code_dict(minimal, cc)
        ss.append(minimal)
    return dd, cc, nrm, ss

def form_tuples(ff, gg):
    a, b, c, d = ff
    e, h, g, f = gg
    return [
        (a, e, f, b),
        (b, f, g, c),
        (c, g, h, d),
        (d, h, e, a)
    ]

def count_quads(tuples, nrm, dd, cc):
    q = defaultdict(int)
    for p in tuples:
        if p not in nrm:
            return 0
        q[nrm[p]] += 1
    return q

def prod_count(q, dd, cc):
    r = 1
    for p, c in q.items():
        for i in range(c):
            r *= dd[p] - i
        r *= cc[p]**c
    return r

def f(ff, gg, nrm, dd, cc):
    tl = form_tuples(ff, gg)
    q = count_quads(tl, nrm, dd, cc)
    if not q:
        return 0
    return prod_count(q, dd, cc)

def rotate_tuple(tup, j):
    return tuple(tup[j:] + tup[:j])

def inner_loop(i, N, ff, ss, dd, nrm, cc):
    res = 0
    for j in range(i + 1, N):
        sl = ss[j]
        dd[sl] -= 1
        for k in range(4):
            rotated = rotate_tuple(sl, k)
            res += f(ff, rotated, nrm, dd, cc)
        dd[sl] += 1
    return res

def main():
    N = read_single_int()
    dd, cc, nrm, ss = process_input(N)
    r = 0
    for i in range(N):
        ff = ss[i]
        dd[ff] -= 1
        r += inner_loop(i, N, ff, ss, dd, nrm, cc)
    print(r)

main()