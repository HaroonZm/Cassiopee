import sys
for x in sys.stdin:
    s = 0
    a = float(x)
    i = 0
    while i < 10:
        s = s + a
        if i % 2 == 0:
            a = a * 2
        else:
            a = a / 3
        i = i + 1
    print s