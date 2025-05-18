while True:
    s = raw_input().split()
    a = int(s[0])
    op = s[1]
    b = int(s[2])
    if op == "?" :
        break
    elif op == "+" : 
        print a + b
    elif op == "-" : 
        print a - b
    elif op == "*" : 
        print a * b
    elif op == "/" : 
        print a / b