import sys

def set_recursion_limit():
    sys.setrecursionlimit(10**5)

def parse_int_list():
    return [int(x) for x in input().split()]

def parse_float_list():
    return [float(x) for x in input().split()]

def parse_neg_int_list():
    return [-1 * int(x) for x in input().split()]

def parse_single_int():
    return int(input())

def parse_single_float():
    return float(input())

def parse_list_map(func, n):
    return [[func(x) for x in input().split()] for _ in range(n)]

def get_mod():
    return 1000000007

def get_inf():
    return float('INF')

def is_cat(S):
    return _is_cat_start(S)

def _is_cat_empty(S):
    return len(S) == 0

def _is_cat_bad_ends(S):
    return S[0] != "m" or S[-1] != "w"

def _is_cat_count(S):
    c = 0
    i = 0
    for idx in range(1, len(S) - 1):
        if S[idx] == 'm':
            c += 1
        elif S[idx] == 'w':
            c -= 1
        if c == 0:
            break
        i = idx
    return i, c

def _is_cat_e_case(S, i):
    return S[1] == 'e', i

def _is_cat_check_recursion(S, i):
    return S[i+1] == 'e' and is_cat(S[1:i+1]) and is_cat(S[i+2:-1])

def _is_cat_start(S):
    if _is_cat_empty(S):
        return True
    if _is_cat_bad_ends(S):
        return False
    i, _ = _is_cat_count(S)
    ecase, new_i = _is_cat_e_case(S, i)
    if ecase:
        new_i = 0
    else:
        new_i = i
    return _is_cat_check_recursion(S, new_i)

def read_input_string():
    return input()

def print_cat():
    print("Cat")

def print_rabbit():
    print("Rabbit")

def main():
    set_recursion_limit()
    S = read_input_string()
    if is_cat(S):
        print_cat()
    else:
        print_rabbit()

main()