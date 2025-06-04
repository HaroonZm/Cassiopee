import math

def read_input():
    return [int(x) for x in raw_input().split()]

def check_termination(a):
    return a == 0

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def is_impossible(discriminant):
    return discriminant < 0

def square_root(val):
    return math.sqrt(val)

def get_bunbo(a):
    return 2 * a

def calculate_bunsi(a, b, d):
    sqrt_d = square_root(d)
    return [-b + sqrt_d, -b - sqrt_d]

def is_integer(num):
    return int(num) == num

def get_bunsi_gcds(bunbo, bunsi):
    return [get_gcd(bunbo, abs(x)) for x in bunsi]

def get_gcd(a, b):
    a, b = min(a, b), max(a, b)
    while a != 0:
        a, b = b % a, a
    return b

def get_fraction_parts(bunbo, bunsi, gcds):
    p = int(bunbo / gcds[0])
    q = -int(bunsi[0] / gcds[0])
    r = int(bunbo / gcds[1])
    s = -int(bunsi[1] / gcds[1])
    return [p, q, r, s]

def print_impossible():
    print 'Impossible'

def is_bunsi_integer(bunsi):
    return is_integer(bunsi[0])

def sorting_cond(p, q, r, s):
    if p > r:
        return [(p, q), (r, s)]
    elif p < r:
        return [(r, s), (p, q)]
    else:
        if q < s:
            return [(r, s), (p, q)]
        else:
            return [(p, q), (r, s)]

def print_result(pair1, pair2):
    print pair1[0], pair1[1], pair2[0], pair2[1]

def process_case(a, b, c):
    bunbo = get_bunbo(a)
    discriminant = calculate_discriminant(a, b, c)
    if is_impossible(discriminant):
        print_impossible()
        return
    bunsi = calculate_bunsi(a, b, discriminant)
    if not is_bunsi_integer(bunsi):
        print_impossible()
        return
    gcds = get_bunsi_gcds(bunbo, bunsi)
    p, q, r, s = get_fraction_parts(bunbo, bunsi, gcds)
    pair1, pair2 = sorting_cond(p, q, r, s)
    print_result(pair1, pair2)

def main_loop():
    while True:
        inputs = read_input()
        a, b, c = inputs
        if check_termination(a):
            break
        process_case(a, b, c)

main_loop()