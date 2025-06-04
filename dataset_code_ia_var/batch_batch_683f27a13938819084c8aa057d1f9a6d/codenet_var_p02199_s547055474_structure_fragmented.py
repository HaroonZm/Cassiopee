def read_two_integers():
    return map(int, input().split())

def read_three_integers():
    return map(int, input().split())

def get_a():
    return read_two_integers()

def get_b():
    a, b = get_a()
    return b

def get_a_value():
    a, _ = read_two_integers()
    return a

def get_inputs():
    return get_a_value(), get_b(), read_three_integers()

def unpack_three(values):
    p, q, r = values
    return p, q, r

def compute_e(p, b):
    return p * b

def compute_b_minus_a(b, a):
    return b - a

def compute_s(diff, q):
    return diff * q

def compute_e_minus_s(e, s):
    return e - s

def compute_sum_q_r(q, r):
    return q + r

def compute_fraction(num, denom):
    return num / denom

def compute_result(b, fraction):
    return b + fraction

def main():
    a, b, triple = get_inputs()
    p, q, r = unpack_three(triple)
    e = compute_e(p, b)
    diff = compute_b_minus_a(b, a)
    s = compute_s(diff, q)
    num = compute_e_minus_s(e, s)
    denom = compute_sum_q_r(q, r)
    fraction = compute_fraction(num, denom)
    result = compute_result(b, fraction)
    print(result)

main()