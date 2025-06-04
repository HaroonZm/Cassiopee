import sys

def read_input():
    return input()

def get_digit(S, idx):
    return S[idx]

def int_of(ch):
    return int(ch)

def format_expression(A, op1, B, op2, C, op3, D):
    return f"{A}{op1}{B}{op2}{C}{op3}{D}=7"

def eval_expr(a, op1, b, op2, c, op3, d):
    val1 = a if op1 == '+' else -a
    val2 = b if op2 == '+' else -b
    val3 = c if op3 == '+' else -c
    return val1 + val2 + val3 + d

def ops_combinations():
    return [
        ('+', '+', '+'),
        ('-', '+', '+'),
        ('+', '-', '+'),
        ('-', '-', '+'),
        ('+', '+', '-'),
        ('-', '+', '-'),
        ('+', '-', '-'),
        ('-', '-', '-'),
    ]

def convert_digits(A, B, C, D):
    return int_of(A), int_of(B), int_of(C), int_of(D)

def check_and_output(A, B, C, D, op1, op2, op3):
    a, b, c, d = convert_digits(A, B, C, D)
    res = a
    if op1 == '+':
        res += b
    else:
        res -= b
    if op2 == '+':
        res += c
    else:
        res -= c
    if op3 == '+':
        res += d
    else:
        res -= d
    if res == 7:
        print(format_expression(A, op1, B, op2, C, op3, D))
        sys.exit()

def main():
    S = read_input()
    A = get_digit(S, 0)
    B = get_digit(S, 1)
    C = get_digit(S, 2)
    D = get_digit(S, 3)
    for op1, op2, op3 in ops_combinations():
        check_and_output(A, B, C, D, op1, op2, op3)

main()