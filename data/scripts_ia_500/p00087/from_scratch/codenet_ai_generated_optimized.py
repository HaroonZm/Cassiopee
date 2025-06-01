import sys

ops = {'+': lambda b,a: a+b, '-': lambda b,a: a-b, '*': lambda b,a: a*b, '/': lambda b,a: a/b}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    stack = []
    for token in line.split():
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](b,a))
        else:
            stack.append(float(token))
    print(f"{stack.pop():.6f}")