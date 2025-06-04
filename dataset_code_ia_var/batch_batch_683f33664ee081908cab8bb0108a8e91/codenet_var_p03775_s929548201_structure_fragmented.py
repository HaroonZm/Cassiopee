def read_input():
    return input()

def to_int(s):
    return int(s)

def compute_sqrt(n):
    return n ** 0.5

def to_int_from_float(f):
    return int(f)

def get_range_end(n):
    sqrt_n = compute_sqrt(n)
    return to_int_from_float(sqrt_n) + 1

def is_divisor(n, i):
    return n % i == 0

def divide(n, i):
    return n // i

def to_str(x):
    return str(x)

def get_length(s):
    return len(s)

def calc_max(a, b):
    return max(a, b)

def calc_min(a, b):
    return min(a, b)

def init_answer():
    return float('inf')

def main():
    n_raw = read_input()
    n = to_int(n_raw)
    ans = init_answer()
    range_end = get_range_end(n)
    i = 1
    while i < range_end:
        if is_divisor(n, i):
            divisor = i
            paired_divisor = divide(n, i)
            str_divisor = to_str(divisor)
            str_paired_divisor = to_str(paired_divisor)
            len_divisor = get_length(str_divisor)
            len_paired_divisor = get_length(str_paired_divisor)
            max_length = calc_max(len_divisor, len_paired_divisor)
            ans = calc_min(ans, max_length)
        i += 1
    print(ans)

main()