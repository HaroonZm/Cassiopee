from collections import defaultdict

def read_int():
    return int(input().split()[0])

def read_input_line():
    return list(map(int, input().split()))

def generate_rotations(xs):
    return [tuple(xs[j:] + xs[:j]) for j in range(1, 5)]

def find_canonical(cnd):
    return min(cnd)

def update_norm(norm, cnd, canonical):
    for item in cnd:
        norm[item] = canonical

def get_cc(x):
    if x[0] == x[2] and x[1] == x[3]:
        return 4 if x[0] == x[1] else 2
    return 1

def process_input(N, dd, cc, norm, ss):
    for _ in range(N):
        xs = read_input_line()
        cnd = generate_rotations(xs)
        x = find_canonical(cnd)
        update_norm(norm, cnd, x)
        dd[x] += 1
        cc[x] = get_cc(x)
        ss.append(x)

def tuple_from_indices(tpl, indices):
    return tuple(tpl[i] for i in indices)

def build_tile_list(ff, gg):
    a, b, c, d = ff
    e, h, g, f = gg
    return [(a, e, f, b), (b, f, g, c), (c, g, h, d), (d, h, e, a)]

def normalize_tile_list(tl, norm):
    normalized = []
    for tile in tl:
        if tile not in norm:
            return None
        normalized.append(norm[tile])
    return normalized

def tile_list_product(tl, dd, cc):
    r = 1
    for cp in tl:
        r *= dd[cp] * cc[cp]
        dd[cp] -= 1
    return r

def restore_dd_counts(tl, dd):
    for cp in tl:
        dd[cp] += 1

def compute_f(ff, gg, norm, dd, cc):
    tl = build_tile_list(ff, gg)
    normalized = normalize_tile_list(tl, norm)
    if normalized is None:
        return 0
    r = tile_list_product(normalized, dd, cc)
    restore_dd_counts(normalized, dd)
    return r

def get_rotations(t):
    return [tuple(t[i:] + t[:i]) for i in range(4)]

def total_result(N, ss, dd, norm, cc):
    r = 0
    for i in range(N):
        ff = ss[i]
        dd[ff] -= 1
        for j in range(i+1, N):
            sl = ss[j]
            dd[sl] -= 1
            sls = get_rotations(list(sl))
            for s in sls:
                r += compute_f(ff, s, norm, dd, cc)
            dd[sl] += 1
        dd[ff] += 1
    return r

def main():
    N = read_int()
    dd = defaultdict(int)
    cc = dict()
    norm = dict()
    ss = []
    process_input(N, dd, cc, norm, ss)
    result = total_result(N, ss, dd, norm, cc)
    print(result // 3)

main()