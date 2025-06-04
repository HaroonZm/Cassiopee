import fractions

def read_input():
    try:
        return tuple(map(int, input().split()))
    except Exception:
        return None, None, None

def is_end_condition(a):
    return not a

def compute_discriminant(a, b, c):
    return b * b - 4 * a * c

def compute_sqrt(val):
    return val ** 0.5

def is_impossible(d):
    return isinstance(d, complex) or abs(d - int(d)) > 1e-6

def compute_numerators(b, d):
    return -b + int(d), -b - int(d)

def compute_denominator(a):
    return 2 * a

def compute_gcd(a, b):
    return fractions.gcd(a, b)

def simplify(num, den, cmn):
    return den // cmn, -num // cmn

def swap_if_needed(p, q, r, s):
    if (p, q) < (r, s):
        return r, s, p, q
    return p, q, r, s

def handle_case(a, b, c):
    d = compute_sqrt(compute_discriminant(a, b, c))
    if is_impossible(d):
        print('Impossible')
        return
    num1, num2 = compute_numerators(b, d)
    den = compute_denominator(a)
    cmn1 = compute_gcd(num1, den)
    cmn2 = compute_gcd(num2, den)
    p, q = simplify(num1, den, cmn1)
    r, s = simplify(num2, den, cmn2)
    p, q, r, s = swap_if_needed(p, q, r, s)
    print(p, q, r, s)

def main_loop():
    while True:
        a, b, c = read_input()
        if is_end_condition(a):
            break
        handle_case(a, b, c)

main_loop()