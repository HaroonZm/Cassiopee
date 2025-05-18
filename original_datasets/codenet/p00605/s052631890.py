while True:
    n,k=map(int, raw_input().split())
    if n==0 and k==0:
         break
    s = map(int, raw_input().split())
    for i in xrange(n):
        b = map(int, raw_input().split())
        for j in xrange(k):
            s[j] -= b[j]
    print "Yes" if len(filter(lambda x:x<0, s))==0 else "No"