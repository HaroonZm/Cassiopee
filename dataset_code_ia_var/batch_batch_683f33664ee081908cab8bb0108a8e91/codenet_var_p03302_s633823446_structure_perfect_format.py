a, b = map(int, raw_input().split())
if a + b == 15:
    print "+"
elif a * b == 15:
    print "*"
else:
    print "x"