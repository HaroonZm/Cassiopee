import sys
sys.setrecursionlimit(9999999)
from collections import deque
import itertools
import math

def combine(a, b, op):
    # Imperative + itertools + messy type checks
    res = list()
    if op == '+':
        for x, y in itertools.product(a, b):
            res.append(x + y)
    elif op == '-':
        for x, y in itertools.product(a, b):
            res += [x - y]
    elif op == '*':
        [res.append(xx * yy) for (xx, yy) in itertools.product(a, b)]
    elif op == '/':
        def custom_div(x, y):
            if y == 0: return None
            if x * y < 0 and x % y != 0:
                return x / float(y) + 1
            else:
                return x / float(y)
        for foo, bar in itertools.product(a, b):
            v = custom_div(foo, bar)
            if v is not None: res.append(v)
    return res

def parse_tokens(seq):
    # Mutates input, mixes functional and old-style checks
    if len(seq) == 1:
        item = seq[0]
        if isinstance(item, str):
            return [int(item)]
        return item
    ans = []
    for k in range(len(seq)):
        if seq[k] in "+-*/":
            xx = parse_tokens(seq[:k])
            yy = parse_tokens(seq[k+1:])
            op = seq[k]
            ans += combine(xx, yy, op)
    return ans

def eval_brackets(X):
    pos = 0
    stack = []
    while 1:
        # Loop-and-break, side-effect arg
        if pos >= len(X) or X[pos] == ')':
            return pos, parse_tokens(stack)
        elif X[pos] == '(':
            move, val = eval_brackets(X[pos+1:])
            pos += move + 1
            stack.append(val)
        else:
            stack.append(X[pos])
        pos += 1

def tok_split(T):
    # One-pass imperative + inline conditionals
    A = ['!']
    for i in T:
        if i.isdigit() and A[-1][-1].isdigit():
            A[-1] += i
        else:
            A.append(i)
    return A[1:]

def raw_input_py2(prompt=""):  # quick compatibility fudge
    try:
        inp = raw_input
    except NameError:
        inp = input
    return inp(prompt)
        
while 1:
    s = raw_input_py2()
    if s == '#':
        break
    s2 = tok_split(s)
    out = eval_brackets(s2)[1]
    print(len(set(out)))