from itertools import product, starmap
from operator import add, sub

num = list(input())
ops = {'+': add, '-': sub}

for op_seq in product(ops, repeat=3):
    expr_elements = [num[0]]
    get_val = lambda acc, tpl: ops[tpl[0]](acc, int(tpl[1]))
    vals = zip(op_seq, num[1:])
    res = starmap(lambda o,n: o+n, zip(['']+list(op_seq), num))
    expr = ''.join(res) + "=7"
    total = int(num[0])
    for op, n in zip(op_seq, num[1:]):
        total = ops[op](total, int(n))
    if total == 7:
        print(expr)
        exit()