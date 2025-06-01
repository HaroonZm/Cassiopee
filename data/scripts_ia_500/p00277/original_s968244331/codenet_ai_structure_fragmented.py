import sys

def read_input():
    f = sys.stdin
    return f

def parse_initial_line(f):
    line = f.readline()
    n, r, l = map(int, line.split())
    return n, r, l

def initialize_lists(n):
    appearance = [0] * n
    point = [0] * n
    return appearance, point

def parse_line(line):
    d, t, x = map(int, line.split())
    return d, t, x

def adjust_d_index(d):
    return d - 1

def update_appearance(appearance, top, t, pre_t):
    appearance[top] += t - pre_t

def update_points(point, d, x):
    point[d] += x

def maybe_update_top(top, d, x, point, n):
    if 0 < x and top != d:
        if point[top] < point[d]:
            top = d
        elif point[top] == point[d] and d < top:
            top = d
    elif x < 0 and top == d:
        top = point.index(max(point))
    return top

def process_lines(f, appearance, point, top, pre_t, l):
    for line in f:
        d, t, x = parse_line(line)
        d = adjust_d_index(d)
        update_appearance(appearance, top, t, pre_t)
        pre_t = t
        update_points(point, d, x)
        top = maybe_update_top(top, d, x, point, len(point))
    update_appearance(appearance, top, l, pre_t)
    return appearance

def find_winner(appearance):
    max_appearance = max(appearance)
    winner_index = appearance.index(max_appearance)
    return winner_index + 1

def main():
    f = read_input()
    n, r, l = parse_initial_line(f)
    appearance, point = initialize_lists(n)
    top = 0
    pre_t = 0
    appearance = process_lines(f, appearance, point, top, pre_t, l)
    print(find_winner(appearance))

main()