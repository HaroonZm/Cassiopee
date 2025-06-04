from collections import Counter

def get_input():
    return int(input())

def get_numbers():
    return input().split()

def mod_four_map(numbers):
    return list(map(lambda x: int(x) % 4, numbers))

def get_counter(mod_numbers):
    return Counter(mod_numbers)

def get_count_for_key(counter, key):
    return counter[key]

def is_two_greater_than_zero(counter):
    return counter[2] > 0

def checked_sum(c1, c2_flag, c3):
    return c1 + int(c2_flag) + c3

def check_condition(sum_val, c0):
    return sum_val <= c0 + 1

def print_yes():
    print('Yes')

def print_no():
    print('No')

def main():
    N = get_input()
    numbers = get_numbers()
    mod_numbers = mod_four_map(numbers)
    counter = get_counter(mod_numbers)
    c1 = get_count_for_key(counter, 1)
    c2_flag = is_two_greater_than_zero(counter)
    c3 = get_count_for_key(counter, 3)
    c0 = get_count_for_key(counter, 0)
    s = checked_sum(c1, c2_flag, c3)
    if check_condition(s, c0):
        print_yes()
    else:
        print_no()

main()