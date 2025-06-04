while True:
    line = raw_input()
    parts = line.split()
    a = int(parts[0])
    b = parts[1]
    c = int(parts[2])
    if b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    elif b == '*':
        print(a * c)
    elif b == '/':
        print(a / c)
    else:
        break