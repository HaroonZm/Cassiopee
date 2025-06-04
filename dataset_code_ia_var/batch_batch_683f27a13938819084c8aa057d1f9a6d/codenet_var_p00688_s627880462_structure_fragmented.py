from fractions import gcd

def read_input():
    return map(int, raw_input().split())

def is_termination_case(a, b, c):
    return (a, b, c) == (0, 0, 0)

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def compute_sqrt(value):
    return value**0.5

def is_perfect_square(value):
    return int(value) == value

def compute_quadratic_roots(b, d):
    return map(int, (-b + d, -b - d))

def get_double_a(a):
    return 2 * a

def safe_gcd(x, y):
    return gcd(x, y)

def normalize_values(a, b):
    if a < 0:
        return (-a, -b)
    return a, b

def process_pair(e, g):
    h = safe_gcd(e, g)
    return h

def get_normalized_root_pair(g, e):
    h = process_pair(e, g)
    return normalize_values(g / h, -e / h)

def is_first_greater(p, q, r, s):
    return (p < r) or (p == r and q < s)

def print_roots(p, q, r, s):
    print p, q, r, s

def print_impossible():
    print "Impossible"

def process_case(a, b, c):
    try:
        disc = calculate_discriminant(a, b, c)
        sqrt_disc = compute_sqrt(disc)
        if not is_perfect_square(sqrt_disc):
            raise Exception()
        e, f = compute_quadratic_roots(b, sqrt_disc)
        g = get_double_a(a)
        p, q = get_normalized_root_pair(g, e)
        r, s = get_normalized_root_pair(g, f)
        if is_first_greater(p, q, r, s):
            p, q, r, s = r, s, p, q
        print_roots(p, q, r, s)
    except:
        print_impossible()

def main_loop():
    while True:
        a, b, c = read_input()
        if is_termination_case(a, b, c):
            break
        process_case(a, b, c)

main_loop()