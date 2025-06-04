a, b, c = [int(n) for n in raw_input().split()]
if a > b:
    if b > c:
        print c, b, a
    elif a > c:
        print b, c, a
    else:
        print b, a, c
else:
    if a > c:
        print c, a, b
    elif b > c:
        print a, c, b
    else:
        print a, b, c