def read_n():
    return input()

def check_break(n):
    return n == 0

def read_int_list():
    return list(map(int, raw_input().strip().split(" ")))

def sort_and_reverse(lst):
    lst.sort()
    lst.reverse()
    return lst

def calc_sum(lst):
    total = 0
    for m in lst:
        total += m
    return total

def should_break(num, sum_val, ji):
    return ((num - 1) * (sum_val + ji)) < (num * sum_val)

def loop_for_j(j_list, n, sum_val):
    num = n
    for i in range(n-1):
        if should_break(num, sum_val, j_list[i]):
            break
        num -= 1
        sum_val += j_list[i]
    return num, sum_val

def main_loop():
    while True:
        n = read_n()
        if check_break(n):
            break
        p = read_int_list()
        j = read_int_list()
        j = sort_and_reverse(j)
        sum_val = calc_sum(p)
        num = n
        num, sum_val = loop_for_j(j, n, sum_val)
        print(num * sum_val)

main_loop()