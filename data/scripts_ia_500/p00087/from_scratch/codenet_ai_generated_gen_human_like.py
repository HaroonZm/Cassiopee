import sys

def eval_rpn(expression):
    stack = []
    for token in expression.split():
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # token == '/'
                stack.append(a / b)
        else:
            stack.append(float(token))
    return stack[0]

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    result = eval_rpn(line)
    print(f"{result:.6f}")