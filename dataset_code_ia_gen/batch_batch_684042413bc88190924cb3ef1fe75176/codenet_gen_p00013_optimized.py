stack = []
try:
    while True:
        x = input()
        if x == '':
            break
        n = int(x)
        if n != 0:
            stack.append(n)
        else:
            print(stack.pop())
except EOFError:
    pass