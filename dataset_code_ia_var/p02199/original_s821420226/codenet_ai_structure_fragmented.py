def read_input():
    return input()

def parse_two_ints(s):
    return map(int, s.split())

def parse_three_ints(s):
    return map(int, s.split())

def get_a_b():
    s = read_input()
    return parse_two_ints(s)

def get_p_q_r():
    s = read_input()
    return parse_three_ints(s)

def compute_p_b(p, b):
    return p * b

def compute_q_a(q, a):
    return q * a

def compute_r_b(r, b):
    return r * b

def sum_terms(x, y, z):
    return x + y + z

def sum_two(x, y):
    return x + y

def divide(numerator, denominator):
    return numerator / denominator

def main():
    a, b = get_a_b()
    p, q, r = get_p_q_r()
    term1 = compute_p_b(p, b)
    term2 = compute_q_a(q, a)
    term3 = compute_r_b(r, b)
    numerator = sum_terms(term1, term2, term3)
    denominator = sum_two(q, r)
    result = divide(numerator, denominator)
    print(result)

main()