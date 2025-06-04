def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def build_count_dict(lst):
    cnt = {}
    for i in range(len(lst)):
        add_count(cnt, lst[i])
    return cnt

def add_count(dic, value):
    if value not in dic:
        dic[value] = 1
    else:
        dic[value] += 1

def find_max(lst):
    return max(lst)

def set_initial_min():
    return 10000000000

def calculate_diameter(max_a):
    return max_a + 1

def try_reduce_counts(cnt, a, max_a):
    min_ = set_initial_min()
    diameter = calculate_diameter(max_a)
    for i in range(diameter):
        tmp = max(max_a - i, i)
        min_ = update_min(min_, tmp)
        if not key_in_dict(cnt, tmp):
            print_impossible_and_exit()
        if count_is_zero(cnt, tmp):
            print_impossible_and_exit()
        decrement_count(cnt, tmp)
    return min_

def update_min(current, new_val):
    return min(current, new_val)

def key_in_dict(dic, key):
    return key in dic

def print_impossible_and_exit():
    print("Impossible")
    exit()

def count_is_zero(dic, key):
    return dic[key] == 0

def decrement_count(dic, key):
    dic[key] -= 1

def check_remaining_counts(cnt, min_):
    for i in cnt:
        if count_is_positive_and_leq_min(cnt, i, min_):
            print_impossible_and_exit()

def count_is_positive_and_leq_min(dic, key, min_):
    return dic[key] > 0 and key <= min_

def print_possible():
    print("Possible")

def main():
    n = read_int()
    a = read_int_list()
    cnt = build_count_dict(a)
    max_a = find_max(a)
    min_ = try_reduce_counts(cnt, a, max_a)
    check_remaining_counts(cnt, min_)
    print_possible()

main()