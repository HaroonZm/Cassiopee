def solve(expression):
    parts = expression.split()
    stack = []
    for part in parts:
        if part == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif part == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif part == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif part == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        else:
            stack.append(float(part))
    return stack[0]

while True:
    try:
        s = raw_input()
        print solve(s)
    except:
        break