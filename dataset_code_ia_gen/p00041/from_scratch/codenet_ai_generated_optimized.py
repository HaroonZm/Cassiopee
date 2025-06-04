import sys
from itertools import permutations, product

ops = [('+', lambda x,y: x+y), ('-', lambda x,y: x-y), ('*', lambda x,y: x*y)]

# 5 formes d'expressions parenthésées avec 4 nombres et 3 opérateurs
def expressions(nums, ops_seq):
    a,b,c,d = nums
    op1, op2, op3 = ops_seq
    # ((a op b) op c) op d
    yield f"(({a} {op1[0]} {b}) {op2[0]} {c}) {op3[0]} {d}", op3[1](op2[1](op1[1](a,b), c), d)
    # (a op (b op c)) op d
    val1 = op1[1](a, op2[1](b,c))
    yield f"({a} {op1[0]} ({b} {op2[0]} {c})) {op3[0]} {d}", op3[1](val1, d)
    # a op ((b op c) op d)
    val2 = op3[1](op2[1](b,c), d)
    yield f"{a} {op1[0]} (({b} {op2[0]} {c}) {op3[0]} {d})", op1[1](a, val2)
    # a op (b op (c op d))
    val3 = op3[1](c,d)
    val4 = op2[1](b,val3)
    yield f"{a} {op1[0]} ({b} {op2[0]} ({c} {op3[0]} {d}))", op1[1](a,val4)
    # (a op b) op (c op d)
    val5 = op1[1](a,b)
    val6 = op3[1](c,d)
    yield f"({a} {op1[0]} {b}) {op2[0]} ({c} {op3[0]} {d})", op2[1](val5,val6)

for line in sys.stdin:
    if not line.strip():
        continue
    parts = line.strip().split()
    if len(parts)!=4:
        continue
    a,b,c,d = map(int, parts)
    if a==0 and b==0 and c==0 and d==0:
        break
    found = False
    for nums in permutations([a,b,c,d]):
        for ops_seq in product(ops, repeat=3):
            for expr_s, val in expressions(nums, ops_seq):
                if val == 10:
                    if len(expr_s) <= 1024:
                        print(expr_s)
                        found = True
                        break
            if found:
                break
        if found:
            break
    if not found:
        print(0)