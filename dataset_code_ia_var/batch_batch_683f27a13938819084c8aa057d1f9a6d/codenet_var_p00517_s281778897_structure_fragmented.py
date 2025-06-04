def read_first_line():
    return raw_input()

def parse_w_h_n(line):
    return map(int, line.split())

def read_ab_line():
    return raw_input()

def parse_a_b(line):
    return map(int, line.split())

def read_xy_line():
    return raw_input()

def parse_x_y(line):
    return map(int, line.split())

def compute_first_option(x, y, a, b):
    return abs(y - x + a - b) + min(abs(y - b), abs(x - a))

def compute_second_option(x, y, a, b):
    return abs(x - a) + abs(y - b)

def compute_increment(x, y, a, b):
    first_opt = compute_first_option(x, y, a, b)
    second_opt = compute_second_option(x, y, a, b)
    return min(first_opt, second_opt)

def update_a_b(x, y):
    return x, y

def main():
    line1 = read_first_line()
    w, h, n = parse_w_h_n(line1)
    line2 = read_ab_line()
    a, b = parse_a_b(line2)
    ans = 0
    for i in xrange(n - 1):
        xy_line = read_xy_line()
        x, y = parse_x_y(xy_line)
        inc = compute_increment(x, y, a, b)
        ans += inc
        a, b = update_a_b(x, y)
    print ans

main()