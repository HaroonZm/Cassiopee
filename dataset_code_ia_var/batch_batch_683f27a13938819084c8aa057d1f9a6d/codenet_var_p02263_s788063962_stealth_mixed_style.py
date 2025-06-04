from functools import reduce

def apply_operator(op, stck):
    if len(stck) > 1:
        b, a = int(stck.pop()), int(stck.pop())
        ops = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': lambda x, y: x * y}
        resul = ops[op](a, b)
        stck += [resul]

a = []
for token in input().split():
    if token in '+-*':
        apply_operator(token, a)
    else:
        (lambda x: a.append(x))(token)

r = None
for v in a:
    if r is None:
        r = v
print(r)