def read_input():
    return input()

def to_int(s):
    return int(s)

def process_input():
    return to_int(read_input())

def should_continue(n):
    return n + 1 != 0

def get_initial_point():
    return 1 + 0j

def get_iteration_range(n):
    return range(n - 1)

def get_direction(p):
    return p * 1j

def normalize_direction(d):
    return d / abs(d)

def update_position(p, d):
    return p + d

def format_real(p):
    return "{:.2f}".format(p.real)

def format_imag(p):
    return "{:.2f}".format(p.imag)

def print_results(p):
    print(format_real(p))
    print(format_imag(p))

def iterate_point(n, p):
    for _ in get_iteration_range(n):
        d = get_direction(p)
        d = normalize_direction(d)
        p = update_position(p, d)
    return p

def main():
    while True:
        n = process_input()
        if not should_continue(n):
            break
        p = get_initial_point()
        p = iterate_point(n, p)
        print_results(p)

main()