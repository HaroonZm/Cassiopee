while True:
    try:
        line = input()
    except EOFError:
        break
    tokens = line.split()
    stack = []
    for token in tokens:
        if token == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif token == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        else:
            stack.append(int(token))
    result = stack.pop()
    print(format(result, '.8f'))