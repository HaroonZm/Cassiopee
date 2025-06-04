def get_input_n():
    return int(input())

def get_input_list():
    return [int(i) for i in input().split()]

def sort_descending(lst):
    lst.sort()
    lst.reverse()
    return lst

def is_odd(n):
    return n % 2 == 1

def generate_even_bases_list(n):
    return [i for i in range(2, n, 2)]

def generate_odd_bases_list(n):
    return [i for i in range(1, n, 2)]

def duplicate_and_sort_reverse(lst):
    l = lst * 2
    l.sort()
    l.reverse()
    return l

def create_b_list(n):
    if is_odd(n):
        l = generate_even_bases_list(n)
        b = duplicate_and_sort_reverse(l)
        b.append(0)
    else:
        l = generate_odd_bases_list(n)
        b = duplicate_and_sort_reverse(l)
    return b

def compare_lists(a, b):
    return a == b

def power_of_two(n):
    return 2 ** (n // 2)

def result_if_equal(a, b, n):
    if compare_lists(a, b):
        return power_of_two(n)
    else:
        return 0

def mod_result(ans, mod=10**9+7):
    return ans % mod

def main():
    n = get_input_n()
    a = get_input_list()
    a = sort_descending(a)
    b = create_b_list(n)
    ans = result_if_equal(a, b, n)
    print(mod_result(ans))

main()