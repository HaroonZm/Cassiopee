def has_100(li):
    return 100 in li

def return_1():
    return 1

def return_0():
    return 0

def a1(li):
    if has_100(li):
        return return_1()
    else:
        return return_0()

def get_first(li):
    return li[0]

def get_second(li):
    return li[1]

def sum_two(a, b):
    return a + b

def average_two(a, b):
    return sum_two(a, b) / 2

def check_a2_condition(val):
    return val >= 90

def a2(li):
    a = get_first(li)
    b = get_second(li)
    avg = average_two(a, b)
    if check_a2_condition(avg):
        return return_1()
    else:
        return return_0()

def get_sum(li):
    return sum(li)

def divide_by_3(n):
    return n / 3

def check_a3_condition(val):
    return val >= 80

def a3(li):
    total = get_sum(li)
    avg = divide_by_3(total)
    if check_a3_condition(avg):
        return return_1()
    else:
        return return_0()

def or_func(a, b):
    return a or b

def isA(li):
    a1_res = a1(li)
    a2_res = a2(li)
    a3_res = a3(li)
    if or_func(a1_res, or_func(a2_res, a3_res)):
        return return_1()
    else:
        return return_0()

def check_b1_condition(val):
    return val >= 70

def b1(li):
    total = get_sum(li)
    avg = divide_by_3(total)
    if check_b1_condition(avg):
        return return_1()
    else:
        return return_0()

def check_b2_avg(val):
    return val >= 50

def check_b2_eighty(n):
    return n >= 80

def b2(li):
    total = get_sum(li)
    avg = divide_by_3(total)
    a = get_first(li)
    b = get_second(li)
    if check_b2_avg(avg) and (check_b2_eighty(a) or check_b2_eighty(b)):
        return return_1()
    else:
        return return_0()

def isB(li):
    b1_res = b1(li)
    b2_res = b2(li)
    if or_func(b1_res, b2_res):
        return return_1()
    else:
        return return_0()

def isX_A(li):
    return 'A'

def isX_B(li):
    return 'B'

def isX_C(li):
    return 'C'

def isX(li):
    if isA(li):
        return isX_A(li)
    elif isB(li):
        return isX_B(li)
    else:
        return isX_C(li)

def input_int():
    return int(input())

def should_break(n):
    return n == 0

def input_line():
    return input()

def split_line(line):
    return line.split()

def map_ints(strs):
    return list(map(int, strs))

def process_and_print(li):
    print(isX(li))

def read_and_process_one():
    l = input_line()
    parts = split_line(l)
    l_int = map_ints(parts)
    process_and_print(l_int)

def loop_n_times(N):
    for _ in range(N):
        read_and_process_one()

def main_loop():
    while True:
        N = input_int()
        if should_break(N):
            break
        loop_n_times(N)

main_loop()