def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def read_input():
    return map(int, input().split())

def is_termination(a):
    return a == 0

def compute_discriminant(a, b, c):
    return b ** 2 - 4 * a * c

def is_negative(n):
    return n < 0

def compute_sqrt(n):
    return n ** 0.5

def is_integer(n):
    return n.is_integer()

def convert_to_int(n):
    return int(n)

def compute_d1(b, d):
    return -b + d

def compute_d2(b, d):
    return -b - d

def compute_a2(a):
    return a << 1

def compute_g1(d1, a2):
    return compute_gcd(d1, a2)

def compute_g2(d2, a2):
    return compute_gcd(d2, a2)

def compute_p(a2, g1):
    return a2 // g1

def compute_q(d1, g1):
    return -d1 // g1

def normalize_sign(x, y):
    if x < 0:
        return -x, -y
    return x, y

def should_swap(p, q, r, s):
    return (p < r) or (p == r and q < s)

def print_result(p, q, r, s):
    print(p, q, r, s)

def print_impossible():
    print("Impossible")

def handle_case(a, b, c):
    d = compute_discriminant(a, b, c)
    if is_negative(d):
        print_impossible()
        return
    d_sqrt = compute_sqrt(d)
    if not is_integer(d_sqrt):
        print_impossible()
        return
    d_int = convert_to_int(d_sqrt)
    d1 = compute_d1(b, d_int)
    d2 = compute_d2(b, d_int)
    a2 = compute_a2(a)
    g1 = compute_g1(d1, a2)
    g2 = compute_g2(d2, a2)
    p = compute_p(a2, g1)
    q = compute_q(d1, g1)
    p, q = normalize_sign(p, q)
    r = compute_p(a2, g2)
    s = compute_q(d2, g2)
    r, s = normalize_sign(r, s)
    if should_swap(p, q, r, s):
        p, q, r, s = r, s, p, q
    print_result(p, q, r, s)

def main_loop():
    while True:
        a, b, c = read_input()
        if is_termination(a):
            break
        handle_case(a, b, c)

main_loop()