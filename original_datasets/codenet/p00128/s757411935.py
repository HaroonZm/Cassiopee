import sys
c = False
for s in sys.stdin.readlines():
    n = s.strip().zfill(5)
    if c: print
    c = True
    for i in xrange(2):
        print "".join(["*" if int(n[j])-5*i in range(5) else " " for j in xrange(5)])
    print "="*5
    for i in xrange(5):
        print "".join([" " if (int(n[j])%5)==i else "*" for j in xrange(5)])