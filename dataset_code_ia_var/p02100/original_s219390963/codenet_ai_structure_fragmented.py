import re

def read_input():
    return input()

def replace_x(expr):
    return expr.replace('x', '*({0})')

def replace_power(expr):
    return expr.replace('^', '**')

def simplify_operators(expr):
    return re.sub(r'([+-])\*', r'\1', expr)[1:]

def generate_range():
    return range(2000, -2001, -1)

def eval_at(expr, value):
    return eval(expr.format(value))

def is_zero(val):
    return val == 0

def format_root(i):
    return '(x{:+})'.format(-i)

def print_root(root):
    print(root, end='')

def print_newline():
    print()

def process(expr):
    for i in generate_range():
        if is_zero(eval_at(expr, i)):
            print_root(format_root(i))
    else:
        print_newline()

def main():
    S = read_input()
    S = replace_x(S)
    S = replace_power(S)
    S = simplify_operators(S)
    process(S)

main()