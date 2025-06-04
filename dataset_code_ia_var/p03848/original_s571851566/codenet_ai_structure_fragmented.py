import collections

def read_input():
    return int(input()), list(map(int, input().split()))

def count_elements(a):
    return collections.Counter(a)

def sort_counter_items(counter):
    return sorted(counter.items())

def check_even_case(p, n):
    for i in range(n // 2):
        if not (p[i][0] == 2 * i + 1 and p[i][1] == 2):
            return False
    return True

def check_odd_case(p, n):
    for i in range(n // 2 + 1):
        if i == 0:
            if not (p[i][0] == 0 and p[i][1] == 1):
                return False
        elif not (p[i][0] == 2 * i and p[i][1] == 2):
            return False
    return True

def power_mod2_half_n(n):
    return pow(2, n // 2, 10 ** 9 + 7)

def output_result(result):
    print(result)

def process_even(n, p):
    if check_even_case(p, n):
        output_result(power_mod2_half_n(n))
    else:
        output_result(0)

def process_odd(n, p):
    if check_odd_case(p, n):
        output_result(power_mod2_half_n(n))
    else:
        output_result(0)

def process(n, a):
    c = count_elements(a)
    p = sort_counter_items(c)
    if n % 2 == 0:
        process_even(n, p)
    else:
        process_odd(n, p)

def main():
    n, a = read_input()
    process(n, a)

main()