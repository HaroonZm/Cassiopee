import sys

c = 0
for s in sys.stdin:
    a, b = map(int, s.split())
    if a == b == 0:
        break
    x = []
    for i in range(a, b + 1):
        if i % 4 == 0:
            if i % 400 == 0:
                x.append(i)
            elif i % 100 != 0:
                x.append(i)
    if c:
        print
    if x == []:
        print "NA"
    else:
        for e in x:
            print e
    c = 1