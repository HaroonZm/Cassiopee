def get_input_n():
    return int(input())

def get_input_list():
    return list(map(int, input().split()))

def is_divisible_by_4(x):
    return x % 4 == 0

def is_divisible_by_2_only(x):
    return x % 2 == 0 and x % 4 != 0

def count_mod_4(a):
    return sum(1 for x in a if is_divisible_by_4(x))

def count_mod_2(a):
    return sum(1 for x in a if is_divisible_by_2_only(x))

def calculate_m(mod_4, mod_2):
    if mod_2 == 0:
        return 2 * mod_4 + 1
    else:
        return 2 * mod_4 + mod_2

def is_m_enough(m, N):
    return m >= N

def print_result(result):
    if result:
        print('Yes')
    else:
        print('No')

def main():
    N = get_input_n()
    a = get_input_list()
    mod_4 = count_mod_4(a)
    mod_2 = count_mod_2(a)
    m = calculate_m(mod_4, mod_2)
    result = is_m_enough(m, N)
    print_result(result)

main()