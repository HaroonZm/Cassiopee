from collections import defaultdict

def get_input_n():
    return int(input().split()[0])

def parse_input_line():
    return list(map(int, input().split()))

def min_index(xs):
    mnx = min(xs)
    return xs.index(mnx)

def select_index(xs, xi, mnx):
    idx3 = (xi + 3) % 4
    idx2 = (xi + 2) % 4
    if xs[idx3] == mnx:
        if xs[idx2] == mnx:
            return idx2
        else:
            return idx3
    return xi

def compare_and_adjust_idx(xs, xi):
    idx1 = (xi + 1) % 4
    idx3 = (xi + 3) % 4
    if xs[idx1] > xs[idx3]:
        return (xi + 2) % 4
    return xi

def normalize(xs):
    mnx = min(xs)
    xi = min_index(xs)
    xi = select_index(xs, xi, mnx)
    xi = compare_and_adjust_idx(xs, xi)
    return tuple(xs[(xi + k) % 4] for k in range(4))

def enumerate_inputs(N):
    tuples = []
    for _ in range(N):
        tuples.append(parse_input_line())
    return tuples

def update_dicts(dd, cc, ss, x, n):
    dd[x] += 1
    cc[x] = n
    ss.append(x)

def get_n_multiplier(x):
    n = 1
    if x[0] == x[2] and x[1] == x[3]:
        n *= 2
        if x[0] == x[1]:
            n *= 2
    return n

def increment_dict(dd, x):
    dd[x] += 1

def decrement_dict(dd, x):
    dd[x] -= 1

def extract_tuple_elements(ff, gg):
    a, b, c, d = ff
    e, h, g, f = gg
    return a, b, c, d, e, h, g, f

def create_candidate_list(norm_func, a, b, c, d, e, h, g, f):
    lst = [
        norm_func([a, e, f, b]),
        norm_func([b, f, g, c]),
        norm_func([c, g, h, d]),
        norm_func([d, h, e, a])
    ]
    return lst

def process_candidate(dd, cc, norm_func, ff, gg):
    a, b, c, d, e, h, g, f = extract_tuple_elements(ff, gg)
    tl = create_candidate_list(norm_func, a, b, c, d, e, h, g, f)
    res = 1
    for cp in tl:
        if cp not in dd or dd[cp] == 0:
            res = 0
            break
        res *= dd[cp] * cc[cp]
        decrement_dict(dd, cp)
    for cp in tl:
        if cp in dd:
            increment_dict(dd, cp)
    return res

def generate_rotations(sl):
    rotations = []
    x, y, z, w = sl
    t = (x, y, z, w)
    rotations.append(t)
    t = (y, z, w, x)
    rotations.append(t)
    t = (z, w, x, y)
    rotations.append(t)
    t = (w, x, y, z)
    rotations.append(t)
    return rotations

def main():
    N = get_input_n()
    dd = defaultdict(int)
    cc = defaultdict(int)
    ss = []
    norm_func = normalize
    input_tuples = enumerate_inputs(N)
    for values in input_tuples:
        a, b, c, d = values
        x = norm_func([a, b, c, d])
        n = get_n_multiplier(x)
        update_dicts(dd, cc, ss, x, n)
    total = 0
    for i in range(N):
        ff = ss[i]
        decrement_dict(dd, ff)
        for j in range(i + 1, N):
            sl = ss[j]
            decrement_dict(dd, sl)
            for s in generate_rotations(sl):
                total += process_candidate(dd, cc, norm_func, ff, s)
            increment_dict(dd, sl)
        increment_dict(dd, ff)
    print(total // 3)

main()