def get_n():
    return int(input())

def get_a():
    return [int(i) for i in input().split()]

def compute_start(a, n):
    return max(0, sum(a) - n * (n - 1))

def get_upper_bound():
    return 51 * (10 ** 16)

def add_values(i, x, n):
    return (i + x - n) // (n + 1) + 1

def compute_k_for_x(x, a, n):
    k = 0
    for i in a:
        k += add_values(i, x, n)
    return k

def satisfies_condition(x, a, n):
    return compute_k_for_x(x, a, n) <= x

def find_min_x(a, n):
    start = compute_start(a, n)
    upper = get_upper_bound()
    for i in range(start, upper):
        if satisfies_condition(i, a, n):
            return i
    return -1  # Should not occur

def main():
    n = get_n()
    a = get_a()
    result = find_min_x(a, n)
    print(result)

main()