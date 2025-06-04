def read_integers():
    return list(map(int, input().split()))

def read_positions_and_velocities():
    a, v = read_integers()
    b, w = read_integers()
    return a, v, b, w

def read_T():
    return int(input())

def print_yes():
    print("YES")

def print_no():
    print("NO")

def positions_equal(a, b):
    return a == b

def first_before_second(a, b):
    return a < b

def velocities_comparison(v, w):
    return v <= w

def can_catch_up(a, v, b, w, T):
    return a + v * T >= b + w * T

def can_catch_down(a, v, b, w, T):
    return a - v * T <= b - w * T

def handle_equal_positions():
    print_yes()

def handle_first_before(a, v, b, w, T):
    if velocities_comparison(v, w):
        print_no()
    else:
        if can_catch_up(a, v, b, w, T):
            print_yes()
        else:
            print_no()

def handle_first_after(a, v, b, w, T):
    if velocities_comparison(v, w):
        print_no()
    else:
        if can_catch_down(a, v, b, w, T):
            print_yes()
        else:
            print_no()

def main():
    a, v, b, w = read_positions_and_velocities()
    T = read_T()
    if positions_equal(a, b):
        handle_equal_positions()
    elif first_before_second(a, b):
        handle_first_before(a, v, b, w, T)
    else:
        handle_first_after(a, v, b, w, T)

main()