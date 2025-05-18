W, a, b = map(int, raw_input().split())
if b >= a and b <= a + W:
    print 0
elif b > a + W:
    print b - (a + W)
else:
    print a - (b + W)