from re import match
A = r"^>'(=+)#\1~$"
B = r"^>\^(Q=)+~~$"
for _ in xrange(input()):
    s = raw_input()
    if match(A,s) != None:
        print "A"
    elif match(B,s) != None:
        print "B"
    else:
        print "NA"