def get_input():
    return input()

def get_length(s):
    return len(s)

def init_cur():
    return 0

def init_P(size):
    return [0]*size

def is_digit(c):
    return c in "0123456789"

def get_char(s, i):
    return s[i]

def advance(index, step=1):
    return index + step

def parse_num(S, L, cur):
    v = 0
    while cur < L and is_digit(get_char(S, cur)):
        v = 10*v + int(get_char(S, cur))
        cur = advance(cur)
    return v, cur

def check_x(S, L, cur):
    return cur < L and get_char(S, cur) == "x"

def check_caret(S, L, cur):
    return cur < L and get_char(S, cur) == '^'

def update_P(P, d, k, op):
    if op == '+':
        P[d] = k
    else:
        P[d] = -k

def parse_term(S, L, cur, P, op):
    k = 1
    if get_char(S, cur) != 'x':
        k, cur = parse_num(S, L, cur)
    d = 0
    if check_x(S, L, cur):
        cur = advance(cur)
        d = 1
        if check_caret(S, L, cur):
            cur = advance(cur)
            d, cur = parse_num(S, L, cur)
    update_P(P, d, k, op)
    return cur

def parse_expr(S, L, cur, P):
    op = "+"
    while True:
        cur = parse_term(S, L, cur, P, op)
        if cur == L:
            break
        op = get_char(S, cur)
        cur = advance(cur)
    return P

def poly_eval(P, x):
    res = 0
    for i in range(len(P)):
        res += P[i] * (x ** i)
    return res

def get_degree(P):
    d = len(P) - 1
    while d >= 0 and P[d] == 0:
        d -= 1
    return d

def add_root(R, x):
    R.append(x)

def find_roots(P):
    R = []
    for x in range(2000, -2001, -1):
        if poly_eval(P, x) == 0:
            add_root(R, x)
    return R

def format_roots(R):
    return "".join("(x%+d)" % -x for x in R)

def main():
    S = get_input()
    L = get_length(S)
    cur = init_cur()
    P = init_P(6)
    P = parse_expr(S, L, cur, P)
    d = get_degree(P)
    R = find_roots(P)
    output = format_roots(R)
    print(output)

main()