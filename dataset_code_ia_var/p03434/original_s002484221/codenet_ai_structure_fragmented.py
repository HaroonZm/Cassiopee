def read_input():
    return input()

def parse_integer(s):
    return int(s)

def parse_int_list(s):
    return list(map(int, s.split()))

def sort_descending(lst):
    return sorted(lst, reverse=True)

def get_even_indices(lst):
    return lst[0::2]

def get_odd_indices(lst):
    return lst[1::2]

def compute_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

def compute_difference(a_sum, b_sum):
    return a_sum - b_sum

def print_result(res):
    print(res)

def main():
    n_str = read_input()
    n = parse_integer(n_str)
    a_str = read_input()
    a = parse_int_list(a_str)
    a_sorted = sort_descending(a)
    al_list = get_even_indices(a_sorted)
    bo_list = get_odd_indices(a_sorted)
    al = compute_sum(al_list)
    bo = compute_sum(bo_list)
    diff = compute_difference(al, bo)
    print_result(diff)

main()