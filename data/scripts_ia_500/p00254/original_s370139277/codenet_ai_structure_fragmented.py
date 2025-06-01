import copy

def is_termination_condition(n):
    return n == ["0", "0", "0", "0"]

def input_to_list():
    return list(input())

def list_to_int(n):
    return int(n[0])*1000 + int(n[1])*100 + int(n[2])*10 + int(n[3])

def is_all_digits_equal(n):
    tmp = list_to_int(n)
    return tmp % 1111 == 0

def sort_descending(n):
    n_sorted = copy.deepcopy(n)
    n_sorted.sort(reverse=True)
    return n_sorted

def sort_ascending(n):
    n_sorted = copy.deepcopy(n)
    n_sorted.sort()
    return n_sorted

def subtract_lists(l, s):
    li = list_to_int(l)
    si = list_to_int(s)
    result = li - si
    result_str = str(result).zfill(4)
    return list(result_str)

def is_goal_reached(n):
    return n == ["6", "1", "7", "4"]

def main_loop():
    n = input_to_list()
    while not is_termination_condition(n):
        if is_all_digits_equal(n):
            print("NA")
        else:
            cnt = process_number(n)
            print(cnt)
        n = input_to_list()

def process_number(n):
    cnt = 0
    while not is_goal_reached(n):
        l = sort_descending(n)
        s = sort_ascending(n)
        n = subtract_lists(l, s)
        cnt += 1
    return cnt

main_loop()