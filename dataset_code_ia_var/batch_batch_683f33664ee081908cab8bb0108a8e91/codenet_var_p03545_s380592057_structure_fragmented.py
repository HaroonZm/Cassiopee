def get_input():
    return input()

def get_length(s):
    return len(s)

def initialize_ans():
    return ''

def set_tmp():
    return ''

def get_range(n):
    return range(2 ** (n - 1))

def iter_n_1(n):
    return range(n - 1)

def get_char(s, idx):
    return s[idx]

def concat_plus(c):
    return c + '+'

def concat_minus(c):
    return c + '-'

def get_last_char(s):
    return s[-1]

def get_bit(val, j):
    return val & (1 << j)

def append_to_tmp(tmp, c):
    return tmp + c

def add_operator(tmp, c, operator_func):
    tmp = append_to_tmp(tmp, c)
    tmp = operator_func('')
    return tmp

def append_operator(tmp, add_plus):
    if add_plus:
        return tmp + '+'
    else:
        return tmp + '-'

def eval_tmp(tmp):
    return eval(tmp)

def check_seven(val):
    return val == 7

def finalize_output(tmp):
    return tmp + '=7'

def main():
    A = get_input()
    n = get_length(A)
    ans = initialize_ans()
    result_tmp = None
    for i in get_range(n):
        tmp = set_tmp()
        for j in iter_n_1(n):
            tmp = append_to_tmp(tmp, get_char(A, j))
            tmp = append_operator(tmp, get_bit(i, j))
        tmp = append_to_tmp(tmp, get_last_char(A))
        if check_seven(eval_tmp(tmp)):
            ans = tmp
            result_tmp = tmp
            break
    print(finalize_output(result_tmp))

main()