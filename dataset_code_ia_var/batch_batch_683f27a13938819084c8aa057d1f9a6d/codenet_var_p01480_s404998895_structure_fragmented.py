def read_input():
    return input()

def to_int(val):
    return int(val)

def create_list(size, value=0):
    return [value] * size

def read_test_case():
    line = raw_input()
    return tuple(map(int, line.split()))

def read_float_pair():
    line = raw_input()
    return tuple(map(float, line.split()))

def read_float_pairs(m):
    pairs = []
    for _ in range(m):
        pairs.append(read_float_pair())
    return pairs

def compute_q_value(vr):
    numerator = compute_numerator(vr)
    denominator = compute_denominator(vr)
    return numerator / denominator

def compute_numerator(vr):
    return sum([v * r for v, r in vr])

def compute_denominator(vr):
    return sum([r for v, r in vr])

def update_q_list(q, index, value):
    q[index] = value

def compute_all_q(t):
    q = create_list(t + 1)
    for i in range(t + 1):
        n, m = read_test_case()
        vr = read_float_pairs(m)
        qval = compute_q_value(vr)
        update_q_list(q, i, qval)
    return q

def compare_and_print_result(q):
    max_val = max(q[:-1])
    diff = max_val - q[-1]
    if check_greater(diff, 0.0000001):
        print_result("YES")
    else:
        print_result("NO")

def check_greater(val, threshold):
    return val > threshold

def print_result(result):
    print result

def main():
    t_raw = read_input()
    t = to_int(t_raw)
    q = compute_all_q(t)
    compare_and_print_result(q)

main()