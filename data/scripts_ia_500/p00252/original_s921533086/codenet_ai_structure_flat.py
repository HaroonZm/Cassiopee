b1, b2, b3 = map(int, raw_input().split())
if (b1 and b2 and (not b3)) or ((not b1) and (not b2) and b3):
    print "Open"
else:
    print "Close"