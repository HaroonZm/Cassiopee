import sys

ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    stack = []
    for token in line.split():
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(float(token))
    print(f"{stack[0]:.6f}")