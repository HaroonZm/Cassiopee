def read_input():
    return input()

def parse_n_m(input_line):
    n_str, m_str = input_line.split()
    return int(n_str), int(m_str)

def parse_a(input_line):
    return list(map(int, input_line.split()))

def compute_prefix_sums(a, n, m):
    a_cs = [0] * (n + 1)
    for i in range(n):
        a_cs[i + 1] = (a_cs[i] + a[i]) % m
    return a_cs

def initialize_defaultdict():
    from collections import defaultdict
    return defaultdict(int)

def count_prefix_sums(a_cs, n, d):
    for i in range(1, n + 1):
        increment_dict(d, a_cs[i])

def increment_dict(d, key):
    d[key] += 1

def calculate_pairs(d):
    ans = 0
    for k, v in d.items():
        ans += part_contribution(d, k, v)
    return ans

def part_contribution(d, k, v):
    if k == 0:
        return v * (v + 1) // 2
    else:
        if d[k] > 1:
            return (v - 1) * v // 2
    return 0

def print_result(ans):
    print(ans)

def main():
    input_line_1 = read_input()
    n, m = parse_n_m(input_line_1)
    input_line_2 = read_input()
    a = parse_a(input_line_2)
    a_cs = compute_prefix_sums(a, n, m)
    d = initialize_defaultdict()
    count_prefix_sums(a_cs, n, d)
    ans = calculate_pairs(d)
    print_result(ans)

main()