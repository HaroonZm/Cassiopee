import re

n = int(raw_input())
for i in range(n):
    s = raw_input()
    patternA = "^>'(=+)#\\1~$"
    patternB = "^>\\^(Q=)+~~$"
    if re.match(patternA, s):
        print "A"
    elif re.match(patternB, s):
        print "B"
    else:
        print "NA"