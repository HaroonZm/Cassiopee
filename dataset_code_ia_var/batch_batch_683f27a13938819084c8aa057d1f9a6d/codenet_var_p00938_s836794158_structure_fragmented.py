def read_input():
    return map(int, input().split())

def get_raySW(x, y):
    return x - y

def to_tuple(xyf):
    sx, sy, f = xyf
    return int(sx), int(sy), f

def compute_s_for_S(x, y, w):
    return get_raySW(x, y)

def compute_t_for_S(x, y, w):
    return w - get_raySW(w - x, y)

def compute_s_for_E(x, y, w, d):
    return w - get_raySW(w - x, y)

def compute_t_for_E(x, y, w, d):
    return w + d + get_raySW(w - x, d - y)

def compute_s_for_N(x, y, w, d):
    return w + d + get_raySW(w - x, d - y)

def compute_t_for_N(x, y, w, d):
    return w + d + w - get_raySW(x, d - y)

def compute_s_for_W(x, y, w, d):
    return w + d + w - get_raySW(x, d - y)

def compute_t_for_W(x, y, w, d):
    return w + d + w + d + get_raySW(x, y)

def normalize_range(s, t, w, d):
    limit = w + d + w + d
    if t <= limit:
        return (s, t)
    else:
        return (s - 2 * w - 2 * d, t - 2 * w - 2 * d)

def get_range_for_direction(x, y, f, w, d):
    if f == 'S':
        s = compute_s_for_S(x, y, w)
        t = compute_t_for_S(x, y, w)
        return (s, t)
    if f == 'E':
        s = compute_s_for_E(x, y, w, d)
        t = compute_t_for_E(x, y, w, d)
        return (s, t)
    if f == 'N':
        s = compute_s_for_N(x, y, w, d)
        t = compute_t_for_N(x, y, w, d)
        return (s, t)
    if f == 'W':
        s = compute_s_for_W(x, y, w, d)
        t = compute_t_for_W(x, y, w, d)
        return normalize_range(s, t, w, d)
    exit(-1)

def toRange(xyf, w, d):
    x, y, f = to_tuple(xyf)
    return get_range_for_direction(x, y, f, w, d)

def get_inputs(n):
    return [input().split() for _ in range(n)]

def swap_st(st):
    x, y = st
    return (y, x)

def get_sorted_ranges(xyfs, w, d):
    ranges = []
    for xyf in xyfs:
        st = toRange(xyf, w, d)
        ranges.append(swap_st(st))
    return sorted(ranges)

def shift_value(value, w, d, sign):
    return value + sign * (d + d + w + w)

def contains_impl(t, s, r):
    return t <= r <= s

def contains_variant(st_triplet, r, w, d):
    s, t = st_triplet
    if contains_impl(t, s, r):
        return True
    if contains_impl(t, s, shift_value(r, w, d, 1)):
        return True
    if contains_impl(t, s, shift_value(r, w, d, -1)):
        return True
    return False

def findMin(sts, w, d):
    c = 0
    r = 3 * (w + w + d + d)
    for s, t in sts:
        if not contains_variant((s, t), r, w, d):
            c += 1
            r = s
    return c

def generate_shifted_ranges(sts, i):
    return sts[i:] + sts[:i]

def get_all_mins(sts, n, w, d):
    mins = []
    for i in range(n):
        shifted = generate_shifted_ranges(sts, i)
        mins.append(findMin(shifted, w, d))
    return mins

def main():
    n, w, d = read_input()
    xyfs = get_inputs(n)
    sts = get_sorted_ranges(xyfs, w, d)
    mins = get_all_mins(sts, n, w, d)
    print(min(mins))

main()