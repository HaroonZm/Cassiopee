import sys
for line in sys.stdin:
    parts = line.split()
    stack = []
    for item in parts:
        if item == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(y + x)
        elif item == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif item == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(y * x)
        elif item == '/':
            x = stack.pop()
            y = stack.pop()
            stack.append(y / x)
        else:
            stack.append(float(item))
    print(stack[0])