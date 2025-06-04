def sort_list(l):
    return sorted(l)

def sum_list(l):
    return sum(l)

def compute_difference(a, b):
    return sum_list(a) - sum_list(b)

def is_difference_even(d):
    return d % 2 == 0

def get_diff_half(d):
    return d // 2 if d % 2 == 0 else d / 2

def find_swap(a, b, diff_half):
    for x in a:
        for y in b:
            if x - y == diff_half:
                return format_result(x, y)
            if x - y < diff_half:
                break
    return -1

def format_result(x, y):
    return " ".join(map(str, [x, y]))

def prepare_lists(s, n):
    return s[:n], s[n:]

def get_input_pair():
    n, m = map(int, raw_input().split())
    return n, m

def get_input_values(total):
    return [int(raw_input()) for _ in range(total)]

def solve(a, b):
    a = sort_list(a)
    b = sort_list(b)
    d = compute_difference(a, b)
    if not is_difference_even(d):
        return -1
    diff_half = d / 2
    return find_swap(a, b, diff_half)

def main_loop():
    while True:
        n, m = get_input_pair()
        if n == 0 and m == 0:
            break
        s = get_input_values(n + m)
        a, b = prepare_lists(s, n)
        print solve(a, b)

main_loop()