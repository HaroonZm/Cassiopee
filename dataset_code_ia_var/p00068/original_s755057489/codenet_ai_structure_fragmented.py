import sys

def read_input():
    return input()

def parse_number(n):
    return int(n)

def should_break(n):
    return n == 0

def read_points(n):
    return [list(input()) for _ in range(n)]

def sort_points(D):
    return sorted(D)

def get_coordinate(p):
    y, x = p
    return y, x

def side_eval(p1, p2, p3):
    y1, x1 = get_coordinate(p1)
    y2, x2 = get_coordinate(p2)
    y3, x3 = get_coordinate(p3)
    return (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1) > 0

def initial_point(D):
    return D[0]

def clone_list(lst):
    return list(lst)

def condition_continue(p1, p2):
    return p1 == p2

def initialize_flags():
    return [0, 0]

def inner_loop(D, D1, p1, p2):
    f = initialize_flags()
    for p3 in reversed(D):
        if p1 == p3 or p2 == p3:
            continue
        idx = 1 if side_eval(p1, p2, p3) else 0
        f[idx] += 1
    return f

def break_inner_loop(f):
    return f[0] == 0

def set_next_p1(p2):
    return p2

def remove_point(D1, p2):
    D1.remove(p2)
    return D1

def check_first_point(p2, first):
    return p2 == first

def print_result(D1):
    print(len(D1))

def process_convex(D):
    p1 = initial_point(D)
    D1 = clone_list(D)
    first = D[0]
    while True:
        c = 0
        for p2 in D1:
            if condition_continue(p1, p2):
                continue
            f = inner_loop(D, D1, p1, p2)
            if break_inner_loop(f):
                break
        p1 = set_next_p1(p2)
        D1 = remove_point(D1, p2)
        if check_first_point(p2, first):
            break
    print_result(D1)

def main_loop():
    while True:
        n = read_input()
        n = parse_number(n)
        if should_break(n):
            break
        D = read_points(n)
        D = sort_points(D)
        process_convex(D)

main_loop()