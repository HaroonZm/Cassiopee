import sys

def set_recursion_limit():
    sys.setrecursionlimit(2*10**5)

def get_symbols():
    return {'?': 1, '&': -1, '|': -2, '(': -3, ')': -4}

def get_constants():
    return 1, -1, -2, -3, -4

def parse_input(tr):
    s = input().strip()
    return [tr[c] for c in s]

def create_stack():
    return []

def evalor_single(L):
    return L[0]

def evalor_multiple(L):
    x0, x1 = L[0]
    for i in range(1, len(L)):
        y0, y1 = L[i]
        x0, x1 = x0 + y0, min(x1, x0 + y1)
    return (x0, x1)

def evalor_dispatch(L):
    if len(L) == 1:
        return evalor_single(L)
    else:
        return evalor_multiple(L)

def andeval(p, s):
    x0, x1 = p
    y0, y1 = s
    return (min(x0, x1 + y0), x1 + y1)

def push_and_eval(f, p, s):
    return push_stack(f, andeval(p, s))

def push_stack(f, s):
    if check_and_on_top(f):
        f.pop()
        p = f.pop()
        return push_and_eval(f, p, s)
    else:
        append_stack(f, s)
        return f

def check_and_on_top(f):
    return f and f[-1] == (-1, -1)

def append_stack(f, s):
    f.append(s)

def is_question(s, question):
    return s == question

def is_and_or_left(s, AND, left):
    return s == AND or s == left

def is_right(s, right):
    return s == right

def pop_until_left(f, left):
    stack = []
    while f[-1] != (left, left):
        sp = f.pop()
        assert sp[0] > 0 and sp[1] > 0
        stack.append(sp)
    assert f.pop() == (left, left)
    return stack

def process_right(f, left):
    stack = pop_until_left(f, left)
    res = evalor_dispatch(stack[::-1])
    return push_stack(f, res)

def process_input_symbols(S, question, AND, left, right):
    f = []
    for s in S:
        if is_question(s, question):
            f = push_stack(f, (s, s))
        elif is_and_or_left(s, AND, left):
            append_stack(f, (s, s))
        elif is_right(s, right):
            f = process_right(f, left)
    return f

def print_result(f):
    print(*f)

def main():
    set_recursion_limit()
    tr = get_symbols()
    question, AND, OR, left, right = get_constants()
    S = parse_input(tr)
    f = process_input_symbols(S, question, AND, left, right)
    f = evalor_dispatch(f)
    print_result(f)

main()