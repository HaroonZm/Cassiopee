import sys
readline = sys.stdin.readline
write = sys.stdout.write
from string import digits

def add_trailing_dollar(S):
    return S + "$"

def is_operator_char(c):
    return c in '+-'

def is_end_fact_char(c):
    return c in '+-$)'

def is_space(c):
    return c == ' '

def skip_spaces(S, cur):
    while S[cur] == ' ':
        cur += 1
    return cur

def parse_number(S, cur):
    v = 0
    while S[cur] in digits:
        v = 10 * v + int(S[cur])
        cur += 1
    return v, cur

def get_current_char(S, cur):
    return S[cur]

def merge_exponents(es0, es1):
    d = {}
    for k, v in es0:
        d[k] = d.get(k, 0) + v
    for k, v in es1:
        d[k] = d.get(k, 0) + v
    es = list(d.items())
    es.sort()
    return es

def filter_non_zero_terms(r):
    return list(filter(lambda x: x[0] != 0, r))

def sort_result(res):
    res.sort()
    return res

def combine_like_terms(res):
    r = []
    for e0 in res:
        k0, es0 = e0
        for e1 in r:
            k1, es1 = e1
            if es0 == es1:
                e1[0] += k0
                break
        else:
            r.append(e0)
    res = filter_non_zero_terms(r)
    res = sort_result(res)
    return res

def parse_identifier(S, cur):
    c = S[cur]
    cur += 1
    cur = skip_spaces(S, cur)
    if S[cur] == '^':
        cur += 1
        cur = skip_spaces(S, cur)
        v, cur = parse_number(S, cur)
    else:
        v = 1
    r = [[1, [(c, v)]]]
    return r, cur

def parse_paren_expr(expr_func, S, cur):
    cur += 1  # skip '('
    r, cur = expr_func(S, cur)
    cur += 1  # skip ')'
    return r, cur

def idt_expr(expr_func, number_func, S, cur):
    cur = skip_spaces(S, cur)
    if S[cur] == '(':
        r, cur = parse_paren_expr(expr_func, S, cur)
    elif S[cur] in digits:
        v, cur = number_func(S, cur)
        r = [[v, []]]
    else:
        r, cur = parse_identifier(S, cur)
    return r, cur

def fact_expr(expr_func, number_func, idt_func, S, cur):
    res = [[1, []]]
    while True:
        r, cur = idt_func(expr_func, number_func, S, cur)
        r0 = []
        for v0, es0 in res:
            for v1, es1 in r:
                es = merge_exponents(es0, es1)
                r0.append([v0*v1, es])
        res = r0
        cur = skip_spaces(S, cur)
        if is_end_fact_char(S[cur]):
            break
    return res, cur

def expr_expr(expr_func, fact_func, S, cur):
    res = []
    op = '+'
    while True:
        r, cur = fact_func(expr_func, parse_number, idt_expr, S, cur)
        if op == '-':
            for e in r:
                e[0] *= -1
        res.extend(r)
        if not is_operator_char(S[cur]):
            break
        op = S[cur]
        cur += 1
    res = combine_like_terms(res)
    return res, cur

def convert(S):
    S = add_trailing_dollar(S)
    def expr_wrapper(S, cur):
        return expr_expr(expr_wrapper, fact_wrapper, S, cur)
    def fact_wrapper(S, cur):
        return fact_expr(expr_wrapper, parse_number, idt_wrapper, S, cur)
    def idt_wrapper(expr_func, number_func, S, cur):
        return idt_expr(expr_func, number_func, S, cur)
    res, _ = expr_wrapper(S, 0)
    return res

def parse_first_input():
    s0 = readline().strip()
    return s0

def process_input_line():
    s = readline().strip()
    return s

def compare_polynomials(d0, d):
    return d0 == d

def output_yes():
    write("yes\n")

def output_no():
    write("no\n")

def output_end():
    write(".\n")

def solve():
    s0 = parse_first_input()
    if s0 == '.':
        return False
    d0 = convert(s0)
    while True:
        s = process_input_line()
        if s == '.':
            break
        d = convert(s)
        if compare_polynomials(d0, d):
            output_yes()
        else:
            output_no()
    output_end()
    return True

def main_loop():
    while solve():
        pass

main_loop()