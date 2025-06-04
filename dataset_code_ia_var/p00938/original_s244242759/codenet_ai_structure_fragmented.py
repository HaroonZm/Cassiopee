def read_input():
    return map(int, input().split())

def parse_direction_data():
    x, y, f = input().split()
    return int(x), int(y), f

def min_positive_boundary(x0, dx, W):
    if dx >= 0:
        return W - x0
    else:
        return x0

def min_positive_boundary_y(y0, dy, D):
    if dy >= 0:
        return D - y0
    else:
        return y0

def boundary_s(x0, y0, dx, dy, W, D):
    return min(min_positive_boundary(x0, dx, W), min_positive_boundary_y(y0, dy, D))

def update_coords(x0, y0, dx, dy, s):
    return x0 + dx * s, y0 + dy * s

def is_on_boundary(x, y, W, D):
    return x == 0 or x == W or y == 0 or y == D

def assert_on_boundary(x, y, W, D):
    assert is_on_boundary(x, y, W, D), (x, y)

def boundary_value(x, y, W, D):
    if y == 0:
        return x
    if x == W:
        return W + y
    if y == D:
        return 2 * W + D - x
    return 2 * W + 2 * D - y

def calc(x0, y0, dx, dy, W, D):
    s = boundary_s(x0, y0, dx, dy, W, D)
    x, y = update_coords(x0, y0, dx, dy, s)
    assert_on_boundary(x, y, W, D)
    return boundary_value(x, y, W, D)

def direction_vectors(f):
    if f == 'N':
        return [(1,1), (-1,1)]
    elif f == 'E':
        return [(1,-1), (1,1)]
    elif f == 'S':
        return [(-1,-1), (1,-1)]
    else:
        return [(-1,1), (-1,-1)]

def adjust_t1_t2(t1, t2, W, D):
    if t1 >= t2:
        t1 -= 2 * (W + D)
    return t1, t2

def process_all_segments(N, W, D):
    S = []
    for _ in range(N):
        x, y, f = parse_direction_data()
        (dx1, dy1), (dx2, dy2) = direction_vectors(f)
        t1 = calc(x, y, dx1, dy1, W, D)
        t2 = calc(x, y, dx2, dy2, W, D)
        t1, t2 = adjust_t1_t2(t1, t2, W, D)
        S.append((t1, t2))
    return S

def sort_segments(S):
    return sorted(S, key=lambda x: x[1])

def update_base(base, idx, N, W, D):
    if idx % N == 0 and idx != 0:
        base += 2 * (W + D)
    return base

def process_segments(S, N, W, D):
    ans = N
    INF = 10 ** 9
    for i in range(N):
        r = 0
        cur = -INF
        base = 0
        for j in range(N):
            idx = (i + j) % N
            a, b = S[idx]
            base = update_base(base, idx, N, W, D)
            if a + base <= cur:
                continue
            cur = b + base
            r += 1
        ans = min(r, ans)
    return ans

def main():
    N, W, D = read_input()
    S = process_all_segments(N, W, D)
    S = sort_segments(S)
    ans = process_segments(S, N, W, D)
    print(ans)

main()