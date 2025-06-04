from sys import stdin

def read_int():
    return int(stdin.readline())

def read_point():
    x, y = map(int, stdin.readline().split())
    return to_complex(x, y)

def to_complex(x, y):
    return x + y * 1j

def read_points(n):
    result = []
    for _ in range(n):
        result.append(read_single_point())
    return result

def read_single_point():
    parts = stdin.readline().split()
    return parse_point(parts)

def parse_point(parts):
    x = parse_part(parts, 0)
    y = parse_part(parts, 1)
    return to_complex(x, y)

def parse_part(parts, idx):
    return int(parts[idx])

def cross(a, b):
    return cross_calc(a, b)

def cross_calc(a, b):
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    return dot_calc(a, b)

def dot_calc(a, b):
    return a.real * b.real + a.imag * b.imag

def eq(a, b):
    return abs(a - b) < 1e-10

def on_line(p, s, e):
    d = get_d(p, s, e)
    c = get_c(p, s, e)
    return check_online(d, c, s, e)

def get_d(p, s, e):
    return dot(p - s, e - s)

def get_c(p, s, e):
    return cross(p - s, e - s)

def check_online(d, c, s, e):
    if c == 0 and is_between(d, abs(e - s) ** 2):
        return True
    return False

def is_between(d, maxvalue):
    return 0 <= d <= maxvalue

def on_polygon_line(xy, p):
    return on_polygon_line_iter(xy, p)

def on_polygon_line_iter(xy, p):
    n = get_len(p)
    for i in range(n):
        j = get_prev_index(i, n)
        if on_line(xy, p[i], p[j]):
            return True
    return False

def get_len(p):
    return len(p)

def get_prev_index(i, n):
    return i - 1

def in_polygon(xy, p):
    wn = 0
    n = get_len(p)
    for i in range(n):
        j = get_prev_index(i, n)
        if is_horizontal(p, i, j):
            continue
        vt = calc_vt(xy, p, i, j)
        tmp = calc_tmp(p, i, j, vt)
        if xy.real < tmp.real:
            wn = update_wn(wn, p, i, j, xy)
    return wn

def is_horizontal(p, i, j):
    return (p[i] - p[j]).imag == 0

def calc_vt(xy, p, i, j):
    return (xy - p[j]).imag / (p[i] - p[j]).imag

def calc_tmp(p, i, j, vt):
    return p[j] + vt * (p[i] - p[j])

def update_wn(wn, p, i, j, xy):
    if increase_case(p, i, j, xy):
        return wn + 1
    elif decrease_case(p, i, j, xy):
        return wn - 1
    else:
        return wn

def increase_case(p, i, j, xy):
    return p[j].imag <= xy.imag < p[i].imag

def decrease_case(p, i, j, xy):
    return p[i].imag <= xy.imag < p[j].imag

def main():
    n = read_int()
    p = read_points(n)
    q = read_int()
    process_queries(q, p)

def process_queries(q, p):
    for _ in range(q):
        xy = read_point()
        print(check_location(xy, p))

def check_location(xy, p):
    if on_polygon_line(xy, p):
        return 1
    elif in_polygon(xy, p):
        return 2
    else:
        return 0

main()