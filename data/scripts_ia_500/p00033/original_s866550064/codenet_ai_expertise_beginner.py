def s(a):
    b = 0
    c = 0
    for i in a:
        if i > b:
            b = i
        elif i > c:
            c = i
        else:
            return 0
    return 1

t = int(raw_input())
for _ in range(t):
    line = raw_input()
    numbers = map(int, line.split())
    if s(numbers):
        print "YES"
    else:
        print "NO"