b1, b2, b3 = raw_input().split()
b1 = int(b1)
b2 = int(b2)
b3 = int(b3)

if (b1 == 1 and b2 == 1 and b3 == 0) or (b1 == 0 and b2 == 0 and b3 == 1):
    print "Open"
else:
    print "Close"