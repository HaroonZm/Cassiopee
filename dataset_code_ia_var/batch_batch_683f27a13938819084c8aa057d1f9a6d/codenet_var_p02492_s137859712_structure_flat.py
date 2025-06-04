while True:
    s = raw_input().split()
    if s[1] == "?":
        break
    a = int(s[0])
    b = int(s[2])
    if s[1] == "+":
        print a + b
    if s[1] == "-":
        print a - b
    if s[1] == "*":
        print a * b
    if s[1] == "/":
        print a / b