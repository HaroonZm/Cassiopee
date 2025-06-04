while True:
    s = raw_input()
    parts = s.split()
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "?":
        break
    if op == "+":
        print a + b
    elif op == "-":
        print a - b
    elif op == "*":
        print a * b
    elif op == "/":
        print a / b