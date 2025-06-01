from functools import reduce

def read_input():
    return input()

def is_termination_code(n):
    return n == '0000'

def normalize_length(n):
    if len(n) < 4:
        n = n.zfill(4)
    return n

def all_digits_equal(n):
    digits_equal_list = [n[0] == s for s in n]
    return reduce(lambda x, y: x and y, digits_equal_list)

def sort_desc(n):
    return ''.join(sorted(n, reverse=True))

def sort_asc(n):
    return ''.join(sorted(n))

def calc_difference(l, s):
    return str(int(l) - int(s))

def kaprekar_routine(n):
    cnt = 0
    while n != '6174':
        l = sort_desc(n)
        s = sort_asc(n)
        n = calc_difference(l, s)
        n = normalize_length(n)
        cnt += 1
    return cnt

def process_number(n):
    n = normalize_length(n)
    if all_digits_equal(n):
        print('NA')
    else:
        cnt = kaprekar_routine(n)
        print(cnt)

def main_loop():
    while True:
        n = read_input()
        if is_termination_code(n):
            break
        process_number(n)

main_loop()