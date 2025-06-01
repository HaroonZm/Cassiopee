t = [[1,2],[-1,3],[1,-1],[4,5],[5,2],[2,1]]
while 1:
    s = raw_input()
    if s=='#': break
    q = 0
    for i in xrange(len(s)):
        if q==-1: break
        q = t[q][int(s[i])]
    print "Yes" if q==5 else "No"