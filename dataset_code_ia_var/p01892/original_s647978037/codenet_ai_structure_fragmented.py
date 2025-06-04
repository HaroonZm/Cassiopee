INF = 2 ** 63 - 1

def get_div_and_mod(b, l):
    return divmod(b, l)

def is_exact_division(m):
    return m == 0

def compute_candidate(d, k):
    return k * d

def compute_abs_diff(candidate, a):
    return abs(candidate - a)

def update_min_x(x, candidate_diff):
    return min(x, candidate_diff)

def get_x_for_l(a, b, n, l):
    d, m = get_div_and_mod(b, l)
    if not is_exact_division(m):
        return INF
    min_x = INF
    for k in range(1, n + 1):
        candidate = compute_candidate(d, k)
        candidate_diff = compute_abs_diff(candidate, a)
        min_x = update_min_x(min_x, candidate_diff)
    return min_x

def solve(a, b, n):
    x = INF
    for l in range(1, n + 1):
        candidate_x = get_x_for_l(a, b, n, l)
        x = update_min_x(x, candidate_x)
    return x

def read_input():
    return map(int, input().split())

def print_output(result):
    print(result)

def main():
    a, b, n = read_input()
    result = solve(a, b, n)
    print_output(result)

if __name__ == '__main__':
    main()