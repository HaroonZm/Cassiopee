def read_input_line():
    return input()

def split_line(line):
    return line.split()

def convert_to_ints(strs):
    return list(map(int, strs))

def get_first_pair():
    line = read_input_line()
    parts = split_line(line)
    return convert_to_ints(parts)

def get_second_triplet():
    line = read_input_line()
    parts = split_line(line)
    return convert_to_ints(parts)

def extract_a_b(pair):
    return pair[0], pair[1]

def extract_p_q_r(triplet):
    return triplet[0], triplet[1], triplet[2]

def calculate_b_minus_a(b, a):
    return b - a

def calculate_p_times_b(p, b):
    return p * b

def calculate_b_minus_a_times_q(b_minus_a, q):
    return b_minus_a * q

def calculate_numerator(p_b, b_minus_a_q):
    return p_b - b_minus_a_q

def calculate_denominator(q, r):
    return q + r

def compute_result(numerator, denominator, b):
    return numerator / denominator + b

def print_result(result):
    print(result)

def main():
    pair = get_first_pair()
    triplet = get_second_triplet()

    a, b = extract_a_b(pair)
    p, q, r = extract_p_q_r(triplet)

    b_minus_a = calculate_b_minus_a(b, a)
    p_b = calculate_p_times_b(p, b)
    b_minus_a_q = calculate_b_minus_a_times_q(b_minus_a, q)
    numerator = calculate_numerator(p_b, b_minus_a_q)
    denominator = calculate_denominator(q, r)

    result = compute_result(numerator, denominator, b)
    print_result(result)

main()